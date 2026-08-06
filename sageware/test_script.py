from unittest import TestCase
import unittest
from script import Person, filter_by_age, filter_by_name, filter_by_location


class PersonModuleTestCase(TestCase):
    """Person module test case."""

    def setUp(self) -> None:
        """Run this setUp before each test."""
        person_1 = Person(name="Edchel Stephen", age=35, location="CDO")
        person_2 = Person(name="Joy Cristy", age=36, location="CDO")
        person_3 = Person(name="Mark", age=28, location="Bukidnon")
        person_4 = Person(name="Eddie", age=61, location="Aloran")
        person_5 = Person(name="Cherily", age=59, location="Aloran")
        person_6 = Person(name="Edchelyn Stephanie", age=38, location="Aloran")
        person_7 = Person(name="Cheddie Jay", age=29, location="Cebu")

        self.age_lower_bound = 28
        self.age_upper_bound = 35

        self.list_of_people = [
            person_1,
            person_2,
            person_3,
            person_4,
            person_5,
            person_6,
            person_7,
        ]
        return super().setUp()


class FilterByAgeFunctionTestCase(PersonModuleTestCase):
    """Testcase for filter_by_age() function."""

    def setUp(self) -> None:
        """Run this setUp before each test."""
        return super().setUp()

    def test_filter_by_age_correctly_filters_list_based_on_lower_bound(self) -> None:
        """Filter by age correctly filters by age on lower bound."""

        output_list = filter_by_age(
            list_of_people=self.list_of_people,
            lower_bound=self.age_lower_bound,
            upper_bound=self.age_upper_bound,
        )

        all_person_have_greater_or_equal_to_lower_bound_age = [
            person.age >= self.age_lower_bound for person in output_list
        ]

        self.assertTrue(all_person_have_greater_or_equal_to_lower_bound_age)

    def filter_by_age_correctly_filters_list_based_on_upper_bound(self) -> None:
        """Filter by age correctly filters by age on upper bound."""

        output_list = filter_by_age(
            list_of_people=self.list_of_people,
            lower_bound=self.age_lower_bound,
            upper_bound=self.age_upper_bound,
        )

        all_person_have_greater_or_equal_to_lower_bound_age = [
            person.age <= self.age_upper_bound for person in output_list
        ]

        self.assertTrue(all_person_have_greater_or_equal_to_lower_bound_age)


if __name__ == "__main__":
    unittest.main()
