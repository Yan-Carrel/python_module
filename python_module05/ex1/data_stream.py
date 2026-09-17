#!/usr/bin/python3
import typing
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.parsed_data: list[str] = []
        self.rank: int = 0

    @abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        rank: int = self.rank
        self.rank += 1
        return (rank, self.parsed_data.pop(0))


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        self.ingested = 0

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, list):
            for item in data:
                if not isinstance(item, int) and not isinstance(item, float):
                    return False
        else:
            if not isinstance(data, int) and not isinstance(data, float):
                return (False)
        return (True)

    def ingest(self, data: int | float | typing.Sequence[int | float]) -> None:
        if self.validate(data):
            if isinstance(data, list):
                for item in data:
                    if isinstance(item, int) or isinstance(item, float):
                        self.parsed_data.append(f"{item}")
                        self.ingested += 1
            else:
                self.parsed_data.append(f"{data}")
                self.ingested += 1
        else:
            raise Exception("Improper numeric data")


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        self.ingested = 0

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, list):
            for item in data:
                if not isinstance(item, str):
                    return False
        else:
            if not isinstance(data, str):
                return (False)
        return (True)

    def ingest(self, data: str | list[str]) -> None:
        if self.validate(data):
            if isinstance(data, list):
                for item in data:
                    self.parsed_data.append(f"{item}")
                    self.ingested += 1
            else:
                self.parsed_data.append(f"{data}")
                self.ingested += 1
        else:
            raise Exception("Improper string data")


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        self.ingested = 0

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, list):
            for item in data:
                if not isinstance(item, dict):
                    return False
                for key in item.keys():
                    if not isinstance(key, str):
                        return False
                for value in item.values():
                    if not isinstance(value, str):
                        return False
        else:
            if not isinstance(data, dict):
                return (False)
            else:
                for key in data.keys():
                    if not isinstance(key, str):
                        return False
                for value in data.values():
                    if not isinstance(value, str):
                        return False
        return (True)

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if self.validate(data):
            if isinstance(data, list):
                for item in data:
                    result = ""
                    values = list(item.values())
                    for i in range(0, len(values)):
                        if i + 1 <= len(values) - 1:
                            result += f"{values[i]}: "
                        else:
                            result += f"{values[i]}"
                    self.parsed_data.append(result)
                    self.ingested += 1

            else:
                values = list(data.values())
                result = ""
                for i in range(len(values)):
                    if i + 1 <= len(values) - 1:
                        result += f"{values[i]}: "
                    else:
                        result += f"{values[i]}"
                self.parsed_data.append(result)
                self.ingested += 1
        else:
            raise Exception("Improper dict value")


class DataStream:
    def __init__(self) -> None:
        self.processors: dict[
            str, NumericProcessor | TextProcessor | LogProcessor
            ] = {}
        self.data: list[object] | None = None

    def register_processor(
            self, proc: NumericProcessor | TextProcessor | LogProcessor
            ) -> None:
        if proc.validate(5):
            self.processors.setdefault('numeric_processor', proc)
        elif proc.validate('x'):
            self.processors.setdefault('text_processor', proc)
        elif proc.validate({'k': 'v'}):
            self.processors.setdefault('log_processor', proc)
        else:
            self.processors.setdefault(proc.__class__.__name__, proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        ingested = 0
        for data in stream:
            found_processor = False
            for proc in self.processors.values():
                if proc.validate(data):
                    proc.ingest(data)
                    found_processor = True
                    ingested += 1
                    break
            if not found_processor:
                print(
                    "DataStream error - "
                    f"Can't process element in stream: {data}"
                    )

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
            return
        else:
            if 'numeric_processor' in self.processors.keys():
                numeric_processor = self.processors['numeric_processor']
                print(
                    "Numeric Processor: "
                    f"total {numeric_processor.ingested} items processed, "
                    f"remaining {len(numeric_processor.parsed_data)} "
                    "on processor"
                    )

            if 'text_processor' in self.processors.keys():
                text_processor = self.processors['text_processor']
                print(
                    "Text Processor: total "
                    f"{text_processor.ingested} items processed, "
                    f"remaining {len(text_processor.parsed_data)} "
                    "on processor")

            if 'log_processor' in self.processors.keys():
                log_processor = self.processors['log_processor']
                print(
                    f"Log Processor: total {log_processor.ingested} "
                    "items processed, remaining "
                    f"{len(log_processor.parsed_data)} "
                    "on processor"
                    )


if __name__ == "__main__":
    stream = [
        'Hello world', [3.14, -1, 2.71],
        [
            {
                'log_level': 'WARNING',
                'log_message': 'Telnet access! Use ssh instead'
                },
            {
                'log_level': 'INFO',
                'log_message': 'User wil isconnected'}
        ], 42, ['Hi', 'five']
            ]

    num_proc: NumericProcessor = NumericProcessor()
    text_proc: TextProcessor = TextProcessor()
    log_proc: LogProcessor = LogProcessor()

    print("=== Code Nexus - Data Stream ===\n")

    print("Initialize Data Stream...")
    data_stream = DataStream()
    try:
        data_stream.print_processors_stats()
    except Exception as e:
        print(e)

    print("")

    print("Registering Numeric Processor")
    print()
    data_stream.register_processor(num_proc)

    print("Send first batch of data on stream: ", stream)
    data_stream.data = stream

    try:
        data_stream.process_stream(stream)
    except Exception as e:
        print(e)

    data_stream.print_processors_stats()

    print("\nRegistering other data processors")
    data_stream.register_processor(text_proc)
    data_stream.register_processor(log_proc)

    print("Send the same batch again")
    try:
        data_stream.process_stream(stream)
    except Exception as e:
        print(e)

    data_stream.print_processors_stats()

    print()

    print(
        "Consume some elements from the data "
        "processors: Numeric 3, Text 2, Log 1"
        )

    if 'numeric_processor' in data_stream.processors:
        for _ in range(3):
            try:
                data_stream.processors['numeric_processor'].output()
            except Exception:
                break
    if 'text_processor' in data_stream.processors:
        for _ in range(2):
            try:
                data_stream.processors['text_processor'].output()
            except Exception:
                break
    if 'log_processor' in data_stream.processors:
        for _ in range(1):
            try:
                data_stream.processors['log_processor'].output()
            except Exception:
                break

    data_stream.print_processors_stats()
