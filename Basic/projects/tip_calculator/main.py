print("Welcome to the tip calculator")
total_bill = int(input("What was the total bill : "))
tip = int(input("How much tip would you like to give, 10 , 12 or 15 : "))
people = int(input("How many people would split the bill?: "))
per_person = round(((tip/100+1)*total_bill)/people,2)
print(f"Each one is paying {per_person}")

