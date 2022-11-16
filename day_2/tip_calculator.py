print("Welcome to the tip calculator")

bill = input("What was the total bill? $")
percentage = input("What percentage tip would you like to give? 15, 18, or 20? ")
people = input("How many people to split the bill? ")

bill_amount = float(bill)
given_percent = int(percentage) / 100 + 1
bill_and_tip = bill_amount * given_percent
total_pp = bill_and_tip / int(people)
total = round(total_pp, 2)
print(f"Each person owes: ${total}")
