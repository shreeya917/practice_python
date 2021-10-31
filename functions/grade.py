def grade_marks(computer, maths, science):
    total_marks = computer + maths + science
    percentage = total_marks / 300 * 100

    if (percentage < 40):
        return 'fail'

    elif (percentage < 60):
        return 'second division'

    elif (percentage < 80):
        return 'first division'

    else:
        return 'distinction'


computer = float(input('Enter your marks for computer: '))
maths = float(input('Enter your marks for maths: '))
science = float(input('Enter your marks for science: '))


grade = grade_marks(computer, maths, science)
print(grade)
