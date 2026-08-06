"""This module is a module that captures the requirements below:


Requirments:
Create a **module/library** that has **three (3) functions ****that operate on an ***Array<Person>***.
| Requirements |
| --- |
| A function that filters by age given a lower-bound and an upper-bound. |
| A function that filters by name given a starting string. |
| A function that filters by location given a name of a location. |


"""


class Person:
    """A person class."""

    def __init__(self, name: str, age: int, location: str) -> None:
        """Initialize the Person object."""
        self.name = name
        self.location = location
        if not 0 < age <= 120:
            raise ValueError(
                "Person mage must be a realistic human age between 1 and 120 years old."
            )
        self.age = age


def filter_by_age(
    list_of_people: list[Person], lower_bound: int, upper_bound: int
) -> list[Person]:
    """A function that filters by age given a lower-bound and an upper-bound."""

    filtered_list = [
        person for person in list_of_people if lower_bound <= person.age <= upper_bound
    ]
    return filtered_list


def filter_by_name(list_of_people: list[Person], starting_string: str) -> list[Person]:
    """A function that filters by name given a starting string preserving the letter case."""

    filtered_list = [
        person for person in list_of_people if person.name.startswith(starting_string)
    ]
    return filtered_list


def filter_by_location(list_of_people: list[Person], location: str) -> list[Person]:
    """A function that filters by location given a name of a location, preserving the letter case."""

    filtered_list = [person for person in list_of_people if person.location == location]
    return filtered_list
