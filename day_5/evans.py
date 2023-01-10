
# My solution
count = 0

for number in range(0, 101, 2):
    count += number
print(count)

# Course solution 1
total = 0

for number in range(2, 101, 2):
    total += number
print(total)


# Course solution 2
total2 = 0

for number in range(1, 101):    
    if number % 2 == 0:
        total2 += number
print(total2)