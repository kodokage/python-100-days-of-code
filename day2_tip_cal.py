#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator")

bill = input("What was the total bill ? ")
total_bill = float(bill)

tip = input("How much tip would you like to give ? 10, 12, 0r 15 ? ")

tip_per = round((int(tip)/100), 2)

people = input("How many people to split the bill ? ")
people_int = int(people)

tip_final = (total_bill/people_int) * tip_per

print(f"Thus everyone's share of the total bill is ${total_bill} plus a ${tip_final} tip.")
