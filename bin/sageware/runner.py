from sageware.script import Person, filter_by_age, filter_by_name, filter_by_location


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
