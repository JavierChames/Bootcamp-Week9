import random

continue_answer = ["yes", "Yes", "y", "Y"]
stop_answer = ["no","No","n","N",]


def check_if_continue(answ):  # Check user answer
    if answ in continue_answer or answ in stop_answer:
        if answ in continue_answer:
            return True
        else:
            return False
    else:
        print("bye")
        return False


exercise_counter = 0
print("Welcome to our Elementary Math, lets start")


def randomize_exercise(): 
    exercise_counter+=1 # Randomize exercise,num1,num2 & operator
    operator_sign = random.randrange(1, 4)
    num1 = random.randrange(1, 11)
    num2 = random.randrange(1, 11)

    if operator_sign == 1:
        exercise = str(num1) + "+" + str(num2)
    if operator_sign == 2:
        exercise = str(num1) + "-" + str(num2)
    if operator_sign == 3:
        exercise = str(num1) + "*" + str(num2)
    return exercise


print("Question number " + str(exercise_counter))
print(randomize_exercise())


# while check_if_continue(user_answer) == True:
# user_answer=input("Would you like to aster our math tests?")
