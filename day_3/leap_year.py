year = int(input("Which year do you want to check? "))

# elif statement logic
if year % 4 != 0:
    print("Not leap")
elif year % 100 != 0:
    print("Leap")
elif year % 400 == 0:
    print("Leap")
else: 
    print("Not leap")

# nested conditional logic statement
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year.")
#         else:
#             print("Not leap year.")
#     else:
#         print("Leap year.")
# else:
#     print("Not leap year.")