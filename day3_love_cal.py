# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1 = name1.lower()
name2 = name2.lower()
names = name1 +  name2

letter_t = names.count('t')
letter_r = names.count('r')
letter_u = names.count('u')
letter_e = names.count('e')
true  = letter_t + letter_r + letter_u +letter_e
letter_l = names.count('l')
letter_o = names.count('o')
letter_v = names.count('v')
letter_ee = names.count('e')
love = letter_l + letter_o + letter_v +letter_ee
number = str(true)+str(love)
number = int(number)

if (number<10 or number>90):
  print(f"Your score is {number} you go together like coke and mentos. ")
elif(40 <= number <= 50):
  print(f"Your score is {number} you are alright together")
else:
  print(f"Your score is {number}")