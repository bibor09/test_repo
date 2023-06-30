def calculate_grade(score):
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    else:
        grade = 'F'

    if grade == 'A' or grade == 'B':
        message = 'Great job!'
    elif grade == 'C':
        message = 'Not bad!'
    else:
        message = 'You need to work harder.'

    return grade, message


# Usage
score = 85
grade, message = calculate_grade(score)
print(f"Your score: {score}")
print(f"Grade: {grade}")
print(f"Message: {message}")