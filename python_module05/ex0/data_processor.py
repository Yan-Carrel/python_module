#!/usr/bin/python3
from typing import Any
from typing import Sequence
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.parsed_data: list[str] = []
        self.rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        rank: int = self.rank
        self.rank += 1
        return (rank, self.parsed_data.pop(0))


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            for item in data:
                if not isinstance(item, int) or isinstance(item, float):
                    return False
        else:
            if not isinstance(data, int) and not isinstance(data, float):
                return (False)
        return (True)

    def ingest(self, data: int | float | Sequence[int | float]) -> None:
        if self.validate(data):
            if isinstance(data, list):
                for item in data:
                    if isinstance(item, int) or isinstance(item, float):
                        self.parsed_data.append(f"{item}")
            else:
                self.parsed_data.append(f"{data}")
        else:
            raise Exception("Improper numeric data")


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
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
            else:
                self.parsed_data.append(f"{data}")
        else:
            raise Exception("Improper string data")


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
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

            else:
                values = list(data.values())
                result = ""
                for i in range(len(values)):
                    if i + 1 <= len(values) - 1:
                        result += f"{values[i]}: "
                    else:
                        result += f"{values[i]}"
                self.parsed_data.append(result)
        else:
            raise Exception("Improper dict value")


if __name__ == "__main__":
    num_proc = NumericProcessor()
    text_proc = TextProcessor()
    log_proc = LogProcessor()

    print("=== Code Nexus - Data Processor ===\n")

    print("Testing Numeric Processor...")
    print(f" Trying to validate input '42': {num_proc.validate(42)}")
    print(f" Trying to validate input 'Hello': {num_proc.validate('Hello')}")

    print(
        " Test invalid ingestion of string 'foo' without prior validation:"
        )
    try:
        num_proc.ingest("foo")
    except Exception as e:
        print(f"Caught exception: {e}")

    print("Processing data: [1, 2, 3, 4, 5]")
    num_data = [1, 2, 3, 4, 5]
    print("Extracting 3 values...")
    for _ in range(3):
        try:
            num_proc.ingest(num_data)
        except Exception:
            break
        i, value = num_proc.output()
        print(f"Numeric value {i}: {value}")

    print("\nTesting Text Processor...")
    print(f" Trying to validate input '42': {text_proc.validate(42)}")

    print("Processing data: ['Hello', 'Nexus', 'World']")
    text_data = ['Hello', 'Nexus', 'World']
    print("Extracting 1 value...")
    text_proc.ingest(text_data)
    i, value = text_proc.output()
    print(f"Text Value {i}: {value}")

    print("\nTesting Log Processor...")
    print(f" Trying to validate input 'Hello': {log_proc.validate('Hello')}")
    log_data = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
        ]
    print(
        "Processing data: [{'log_level': 'NOTICE', "
        "'log_message': 'Connection to server'}, "
        "{'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]"
        )

    print("Extracting 2 values...")
    log_proc.ingest(log_data)

    for _ in range(2):
        i, value = log_proc.output()
        print(f"Log entry {i}: {value}")
