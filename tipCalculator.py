print("Welcome to the tip calculator")
bill = float(input('What was the total bill? Ksh'))
tipPercentage = int(input('What percentage tip would you like to give? 10, 12, 15? '))
people = int(input("How many people to split the bill? "))

tip = (tipPercentage/100)+1
individualBill = (bill / people) * tip
finalAmount = "{:.2f}".format(individualBill)
print(f"Each person should pay: Ksh{finalAmount}")

