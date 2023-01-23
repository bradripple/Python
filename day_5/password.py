import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = []


for letter in letters:
    if nr_letters > 0:
        nr_letters -= 1
        password += letter

for symbol in symbols:
    if nr_symbols > 0:
        nr_symbols -= 1
        password += symbol

for num in numbers:
    if nr_numbers > 0:
        nr_numbers -= 1
        password += num

random.shuffle(password)

randomized_password = ""

for char in password:
    randomized_password += char

print(f"Your password is: {randomized_password}")

# Course solution

# password = ""

# for char in range(1, nr_letters + 1):
#     # 1 - 4
#     password += random.choice(letters)

# for char in range(1, nr_symbols + 1):
#     password += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#     password += random.choice(numbers)

# print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
# password1 = ""
# random.shuffle(letters)
# random.shuffle(symbols)
# random.shuffle(numbers)

# print(symbols)

# for letter in letters:
#     if nr_letters > 0:
#         nr_letters -= 1
#         password1 += letter
#         print(password1)

# for symbol in symbols:
#     if nr_symbols > 0:
#         nr_symbols -= 1
#         password1 += symbol

# for num in numbers:
#     if nr_numbers > 0:
#         nr_numbers -= 1
#         password1 += num
        


# print(random.shuffle(password1))

# Course Hard solution

# password_list = []

# for char in range(1, nr_letters + 1):
#     # 1 - 4
#     password_list.append(random.choice(letters))

# for char in range(1, nr_symbols + 1):
#     password_list.append(random.choice(symbols))

# for char in range(1, nr_numbers + 1):
#     password_list.append(random.choice(numbers))


# random.shuffle(password_list)

# password = ""

# for char in password_list:
#     password += char


# print(f'Your password is: {password}')