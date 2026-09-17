#!/usr/bin/python3
from datetime import datetime
from typing import Optional
from enum import Enum
from typing_extensions import Self
import sys
try:
    from pydantic import BaseModel, Field, ValidationError, model_validator
except ImportError:
    print("Error, you need to install pydantic module")
    print("Run the following commands:")
    print("python3 -m venv .venv")
    print("source .venv/bin/activate")
    print("python3 -m pip install pydantic")
    sys.exit(1)


class ContactType(Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime = Field(...)
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType = Field(...)
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def custom_rules(self) -> Self:
        if not self.contact_id.startswith("AC"):
            raise ValueError("contact_id must start with 'AC'")
        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError(
                "Physical contact reports must be verified"
                )
        if (
            self.contact_type == ContactType.telepathic
            and self.witness_count < 3
                ):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
                )
        if self.signal_strength > 7.0 and self.message_received is None:
            raise ValueError(
                "Strong signals (>7.0) should include received messages"
                )
        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("========================================")
    print("Valid contact report:")
    try:
        model = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime(2026, 1, 6),
            location="Area 51, Nevada",
            contact_type=ContactType.radio,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
            is_verified=True
        )
        print(
            f"ID: {model.contact_id}\nType: {model.contact_type.value}\n"
            f"Location: {model.location}\nSignal: {model.signal_strength}/10\n"
            f"Duration: {model.duration_minutes} minutes\n"
            f"Witnesses: {model.witness_count}\n"
            f"Message: {model.message_received}"
            )
    except ValidationError as e:
        error_list = e.errors()
        print(error_list[0]['msg'].replace("Value error, ", ""))

    print("\n========================================")
    print("Expected validation error:")
    try:
        model = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime(2026, 1, 6),
            location="Area 51, Nevada",
            contact_type=ContactType.telepathic,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=2,
            message_received="Greetings from Zeta Reticuli",
            is_verified=True
        )
    except ValidationError as e:
        error_list = e.errors()
        print(error_list[0]['msg'].replace("Value error, ", ""))


if __name__ == "__main__":
    main()
