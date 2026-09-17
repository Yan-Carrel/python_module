#!/usr/bin/python3
from datetime import datetime
from typing import Optional
import sys
try:
    from pydantic import BaseModel, Field, ValidationError
except ImportError:
    print("Error, you need to install pydantic module")
    print("Run the following commands:")
    print("python3 -m venv .venv")
    print("source .venv/bin/activate")
    print("python3 -m pip install pydantic")
    sys.exit(1)


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime = Field(...)
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")
    print("Valid station created:")
    try:
        model = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime(2026, 1, 6),
            is_operational=True,
            notes=None
        )

        print(f"ID: {model.station_id}")
        print(f"Name: {model.name}")
        print(f"Crew: {model.crew_size} people")
        print(f"Power: {model.power_level}%")
        print(f"Oxygen: {model.oxygen_level}%")
        print(
            "Status: "
            f"{'Operational' if model.is_operational else 'Not Operational'}"
            )
    except ValidationError as e:
        error_list = e.errors()
        print(error_list[0]['msg'])

    print("\n========================================")
    print("Expected validation error:")
    try:
        model = SpaceStation(
            station_id="LGW125",
            name="Titan Mining Outpost",
            crew_size=21,
            power_level=90.0,
            oxygen_level=98.3,
            last_maintenance=datetime(2026, 1, 6),
            is_operational=True
        )
    except ValidationError as e:
        error_list = e.errors()
        print(error_list[0]['msg'])


if __name__ == "__main__":
    main()
