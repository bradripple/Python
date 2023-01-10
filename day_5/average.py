student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

print(student_heights)

# count = 0
# height = 0

# for heights in student_heights:
#     count = count + 1
#     height = height + heights
# print(round(height / count))

# Solved usinig  sum and len
# total_height = sum(student_heights)
# number_of_students = len(student_heights)
# average_height = round(total_height / number_of_students)

total_height = 0
for height in student_heights:
    total_height += height
# print(total_height)

number_of_students = 0
for student in student_heights:
  number_of_students += 1
# print(number_of_students)

average_height = round(total_height / number_of_students)

print(average_height)