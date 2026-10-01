from unittest import TestCase
from sageware.script import Person, filter_by_age, filter_by_name, filter_by_location


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


class PersonTestCase(PersonModuleTestCase):
    """Person class test case."""

    def setUp(self) -> None:
        """Run this setUp before each test."""
        super().setUp()
        self.name = "Edchel Stephen"
        self.age = 35
        self.location = "CDO"
        self.person_1 = Person(name=self.name, age=self.age, location=self.location)

    def test__str__returns_expected_string(self) -> None:
        """test __str__ method returns expected string."""
        actual = str(self.person_1)
        expected = self.name

        self.assertEqual(actual, expected)

    def test__repr__returns_expected_string(self) -> None:
        """test __repr__ method returns expected string."""
        actual = repr(self.person_1)
        expected = f"Person(name={self.name}, age={self.age}, location={self.location})"

        self.assertEqual(actual, expected)

    def test_person_with_negative_age_raises_ValueError(self) -> None:
        """Person with negative age raises Value Error."""

        with self.assertRaises(ValueError):
            Person(name="Benjamin", age=-1, location="USA")

    def test_person_with_over_possible_age_raises_ValueError(self) -> None:
        """Person with over possible age raises Value Error."""

        with self.assertRaises(ValueError):
            Person(name="Benjamin", age=121, location="USA")


class FilterByAgeFunctionTestCase(PersonModuleTestCase):
    """Testcase for filter_by_age() function."""

    def setUp(self) -> None:
        """Run this setUp before each test."""
        super().setUp()
        self.age_lower_bound = 28
        self.age_upper_bound = 35

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


class FilterByNameFunctionTestCase(PersonModuleTestCase):
    """Testcase for filter_by_name() function."""

    def setUp(self) -> None:
        """Run this setUp before each test."""
        super().setUp()
        self.starting_string = "Ed"

    def test_filter_by_name_correctly_filters_by_starting_string(self) -> None:
        """Filter by name correctly filters by starting string."""

        output_list = filter_by_name(
            list_of_people=self.list_of_people, starting_string=self.starting_string
        )

        all_person_have_starting_string = [
            person.name.startswith(self.starting_string) for person in output_list
        ]

        self.assertTrue(all_person_have_starting_string)


class FilterByLocationFunctionTestCase(PersonModuleTestCase):
    """Testcase for filter_by_location() function."""

    def setUp(self) -> None:
        """Run this setUp before each test."""
        super().setUp()
        self.search_location = "CDO"

    def test_filter_by_location_correctly_filters_by_location(self) -> None:
        """Filter by location correctly filters by location."""

        output_list = filter_by_location(
            list_of_people=self.list_of_people, location=self.search_location
        )

        all_person_have_location = [
            person.location == self.search_location for person in output_list
        ]

        self.assertTrue(all_person_have_location)
