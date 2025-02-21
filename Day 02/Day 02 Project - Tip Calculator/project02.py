# Project 02

# This is what I came up with for this project
# print("Welcome to the tip calculator!")
# bill = input("What was the total bill? $")
# tip_percentage = input("How much tip would you like to give? 10, 12, or 15?") #12% = 12 / 100 = 0.12
# tip = float(bill) * float(1 + (float(tip_percentage) / 100))
# split = input("How many people to split the bill?")


# total = round(float(tip)/int(split), 2)
# print(f"Each person should pay: ${total}")

# This is the solution
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill?"))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

print(f"Each person should pay: ${final_amount}")