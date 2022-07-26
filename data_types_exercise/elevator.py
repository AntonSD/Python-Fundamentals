from math import ceil

number_of_people = int(input())
elevetor_capacity = int(input())

courses = 0
if elevetor_capacity != 0:
    courses = ceil(number_of_people / elevetor_capacity)
print(courses)
