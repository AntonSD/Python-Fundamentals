employee_one = int(input())
employee_two = int(input())
employee_three = int(input())
number_of_students = int(input())

students_per_hour = employee_two + employee_three + employee_one
hours = 0
while number_of_students > 0:
    hours += 1

    if hours % 4 == 0:
        continue

    number_of_students -= students_per_hour

print(f"Time needed: {hours}h")