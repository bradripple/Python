student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

# Solution using max and min functions
# print("The highest score in the class is: " + str(max(student_scores)))
# print("The lowest score in the class is: " + str(min(student_scores)))

# My solution
max = 0

for score in student_scores:
    if max < score:
        max = score
print(f"The highest score in the class is: {max}")

# Course solution
highest_score = 0

for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")