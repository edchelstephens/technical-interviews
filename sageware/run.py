from sageware.script import Person, filter_by_age, filter_by_name, filter_by_location

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


filtered_by_age = filter_by_age(
    list_of_people=list_of_people, lower_bound=28, upper_bound=35
)

print(" =========== filter_by_age() output =========== ")
print(filtered_by_age)
print()

filtered_by_name = filter_by_name(list_of_people=list_of_people, starting_string="Ed")

print(" =========== filter_by_name() output =========== ")
print(filtered_by_name)
print()


filtered_by_location = filter_by_location(list_of_people=list_of_people, location="CDO")

print(" =========== filter_by_location() output CDO =========== ")
print(filtered_by_location)
print()
