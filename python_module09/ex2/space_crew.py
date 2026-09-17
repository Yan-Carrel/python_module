#!/usr/bin/python3
from datetime import datetime
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


class Rank(Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank = Field(...)
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime = Field(...)
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def check_space_mission(self) -> Self:
        correct_ranks = False
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID should start with 'M'")

        for crew in self.crew:
            if (
                crew.rank.value == "commander" or
                crew.rank.value == "captain"
                    ):
                correct_ranks = True
        if not correct_ranks:
            raise ValueError("Must have at least one Commander or Captain")

        if self.duration_days > 365:
            experienced = [
                crew for crew in self.crew if crew.years_experience >= 5
                ]
            if len(experienced) < (len(self.crew) / 2):
                raise ValueError(
                    "At least 50% of crew should have 5+ years experience"
                    )

        for crew in self.crew:
            if not crew.is_active:
                raise ValueError("All crew members must be active")
        return self


def main() -> None:
    try:
        commander = CrewMember(
            member_id="M1945",
            name="Sarah Connor",
            rank=Rank.commander,
            age=56,
            specialization="Mission Command",
            years_experience=25,
            is_active=True
        )
    except ValidationError as e:
        error_list = e.errors()
        print(error_list[0]['msg'].replace("Value error, ", ""))

    try:
        lieutenant = CrewMember(
            member_id="M7457",
            name="John Smith",
            rank=Rank.lieutenant,
            age=42,
            specialization="Navigation",
            years_experience=13,
            is_active=True
        )
    except ValidationError as e:
        error_list = e.errors()
        print(error_list[0]['msg'].replace("Value error, ", ""))

    try:
        officer = CrewMember(
            member_id="M4637",
            name="Alice Johnson",
            rank=Rank.officer,
            age=37,
            specialization="Engineering",
            years_experience=15,
            is_active=True
        )
    except ValidationError as e:
        error_list = e.errors()
        print(error_list[0]['msg'].replace("Value error, ", ""))

    try:
        crew_members = [commander, lieutenant, officer]
    except UnboundLocalError as e:
        print(e)
        sys.exit(1)

    try:
        space_mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2026, 2, 17),
            duration_days=900,
            crew=crew_members,
            mission_status="planned",
            budget_millions=2500.0
        )
        print("Space Mission Crew Validation")
        print("=========================================")
        print("Valid mission created:")
        print(f"Mission: {space_mission.mission_name}")
        print(f"ID: {space_mission.mission_id}")
        print(f"Destination: {space_mission.destination}")
        print(f"Duration: {space_mission.duration_days} days")
        print(f"Budget: ${space_mission.budget_millions}M")
        print(f"Crew size: {len(space_mission.crew)}")
        print("Crew members:")
        for member in space_mission.crew:
            print(
                f"- {member.name} ({member.rank.value})"
                f" - {member.specialization}"
                )
    except ValidationError as e:
        error_list = e.errors()
        print(error_list[0]['msg'].replace("Value error, ", ""))

    print("\n========================================")
    print("Expected validation error:")
    new_members = [lieutenant, officer]

    try:
        space_mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2026, 2, 17),
            duration_days=900,
            crew=new_members,
            mission_status="planned",
            budget_millions=2500.0
        )
    except ValidationError as e:
        error_list = e.errors()
        print(error_list[0]['msg'].replace("Value error, ", ""))


if __name__ == "__main__":
    main()
