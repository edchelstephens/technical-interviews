"""This module is a module that captures the requirements below:


Requirments:
Create a **module/library** that has **three (3) functions ****that operate on an ***Array<Person>***.
| Requirements |
| --- |
| A function that filters by age given a lower-bound and an upper-bound. |
| A function that filters by name given a starting string. |
| A function that filters by location given a name of a location. |


"""

from pprint import pprint


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

    def __str__(self) -> str:
        """String representation of the object."""
        return f"Person(name={self.name}, age={self.age}, location={self.location})"

    def __repr__(self) -> str:
        """String representation of the object."""
        return f"Person(name={self.name}, age={self.age}, location={self.location})"


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


print()
print(" ****************** Sample Run ****************** ")
print()

person_1 = Person(name="Edchel Stephen", age=35, location="CDO")
person_2 = Person(name="Joy Cristy", age=36, location="CDO")
person_3 = Person(name="Mark", age=28, location="Bukidnon")
person_4 = Person(name="Eddie", age=61, location="Aloran")
person_5 = Person(name="Cherily", age=59, location="Aloran")
person_6 = Person(name="Edchelyn Stephanie", age=38, location="Aloran")
person_7 = Person(name="Cheddie Jay", age=29, location="Cebu")

age_lower_bound = 28
age_upper_bound = 35

list_of_people = [
    person_1,
    person_2,
    person_3,
    person_4,
    person_5,
    person_6,
    person_7,
]

print(" =========== list_of_people  =========== ")
pprint(list_of_people)
print()


lower_age_bound = 28
upper_age_bound = 35

filtered_by_age = filter_by_age(
    list_of_people=list_of_people, lower_bound=28, upper_bound=35
)

print(f"=========== filter_by_age() output =========== ")
print(f"\nlower_age_bound={lower_age_bound}")
print(f"upper_age_bound={upper_age_bound}")
print("\nOutput: \n")
pprint(filtered_by_age)
print()

starting_name_string = "Ed"
filtered_by_name = filter_by_name(
    list_of_people=list_of_people, starting_string=starting_name_string
)

print("=========== filter_by_name() output =========== ")
print(f"\nstarting_name_string={starting_name_string}")
print("\nOutput: \n")
pprint(filtered_by_name)
print()


search_location = "CDO"
filtered_by_location = filter_by_location(
    list_of_people=list_of_people, location=search_location
)

print(f"=========== filter_by_location() output =========== ")
print(f"\nsearch_location={search_location}")
print("\nOutput: \n")
pprint(filtered_by_location)
print()
