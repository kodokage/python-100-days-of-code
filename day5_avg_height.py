# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

height = 0
counter = 0
for student in student_heights:
  height += int(student)
  counter += 1
#Write your code below this row 👇

print(height/counter)

