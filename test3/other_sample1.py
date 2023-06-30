def calculate_grade(score):
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'

    # if grade == 'A' or grade == 'B':
    #     message = 'Great job!'
    # elif grade == 'C':
    #     message = 'Not bad!'
    # elif grade == 'D':
    #     message = 'You can do better.'
    # else:
    #     message = 'You need to work harder.'

    return grade, message


# Usage
score = 85
grade, message = calculate_grade(score)
print(f"Your score: {score}")
print(f"Grade: {grade}")
print(f"Message: {message}")