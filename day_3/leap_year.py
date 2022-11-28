year = int(input("Which year do you want to check? "))

if year % 4 != 0:
    print("Not leap")
elif year % 100 != 0:
    print("Leap")
elif year % 400 == 0:
    print("Leap")
else: 
    print("Not leap")
