from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
import sys


BOUNDARIES = [18, 25, 35, 45, 60, 80, 100]


@dataclass(order=True)
class Person:
    """
    This class stores information about one person.
    It keeps the full name and the age.
    """
    age: int
    full_name: str

    def __str__(self) -> str:
        """Return a simple string with name and age."""
        return f"{self.full_name} ({self.age})"


@dataclass
class AgeGroup:
    """
    This class describes one age group.
    The group has a lower and upper limit and a list of persons.
    """
    label: str
    lower: int
    upper: Optional[int]
    persons: List[Person] = field(default_factory=list)

    def fits(self, age: int) -> bool:
        """
        Check if the given age fits inside this age group.
        """
        if age < self.lower:
            return False
        if self.upper is not None and age > self.upper:
            return False
        return True

    def add_person(self, person: Person) -> None:
        """
        Add a person into this group if the age fits.
        """
        if self.fits(person.age):
            self.persons.append(person)

    def sort_persons(self) -> None:
        """
        Sort persons in the group.
        First by age (high to low), then by full name (A to Z).
        """
        self.persons.sort(key=lambda p: (-p.age, p.full_name))


class SurveyGrouper:
    """
    This class groups people by age.
    It uses predefined age boundaries to build age groups.
    """
    def __init__(self, boundaries: List[int] = None):
        """
        Create age groups using the given boundaries.
        If no boundaries are given, the default list is used.
        """
        if boundaries is None:
            boundaries = BOUNDARIES

        boundaries = sorted(boundaries)
        self.groups = self._build_groups(boundaries)

    @staticmethod
    def _build_groups(boundaries: List[int]) -> List[AgeGroup]:
        """
        Build a list of AgeGroup objects from boundaries.
        """
        groups: List[AgeGroup] = []

        first_upper = boundaries[0]
        groups.append(AgeGroup(label=f"0-{first_upper}", lower=0, upper=first_upper))

        for i in range(1, len(boundaries)):
            lower = boundaries[i - 1] + 1
            upper = boundaries[i]
            groups.append(AgeGroup(label=f"{lower}-{upper}", lower=lower, upper=upper))

        last = boundaries[-1]
        groups.append(AgeGroup(label=f"{last + 1}+", lower=last + 1, upper=None))

        return groups

    def add_person(self, full_name: str, age: int) -> None:
        """
        Create a Person object and put it into the correct age group.
        """
        person = Person(age=age, full_name=full_name.strip())
        for group in self.groups:
            if group.fits(age):
                group.add_person(person)
                break

    def format_output(self) -> List[str]:
        """
        Create output lines for all non-empty age groups.
        Groups are printed from older to younger.
        """
        for g in self.groups:
            g.sort_persons()

        non_empty = [g for g in self.groups if g.persons]
        non_empty.sort(key=lambda g: g.lower, reverse=True)

        lines = []
        for group in non_empty:
            people = ", ".join(str(p) for p in group.persons)
            lines.append(f"{group.label}: {people}")
        return lines


def main():
    """
    It reads input lines, adds persons, and prints the result.
    """
    grouper = SurveyGrouper()

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        if line == "END":
            break

        try:
            name_part, age_part = line.rsplit(",", 1)
        except ValueError:
            continue

        name = name_part.strip()
        try:
            age = int(age_part.strip())
        except ValueError:
            continue

        grouper.add_person(name, age)

    for out in grouper.format_output():
        print(out)


if __name__ == "__main__":
    main()
