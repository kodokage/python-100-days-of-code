#Write your code below this row 👇
for i in range(1,101):
  if (i%3) and (i%5) != 0:
    print(i)
  if(i%3 == 0) and (i%5 != 0):
    print('fizz')
  if(i%3 != 0) and (i%5 == 0):
    print('buzz')
  if(i%3 == 0) and (i%5 == 0):
    print('fizzbuzz')
