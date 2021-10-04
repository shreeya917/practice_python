computer = float(input('Enter your marks for computer: '))
maths = float(input('Enter your marks for maths: '))
science = float(input('Enter your marks for science: '))

total_marks = computer + maths + science
percentage = total_marks / 300 * 100

if (percentage < 40):
    grade = "fail"


elif (percentage < 60):
    grade = 'second division'


elif (percentage < 80):
    grade = 'first division'


else:
    grade = 'distinction'

print(f"Your percentage is {percentage}.")
print(f"Your grade is {grade}.")
