import random
import math
continue_answer = ["yes", "Yes", "y", "Y"]
stop_answer = [ "no","No","n","N"]
wrong_answer_array = []
count_good_answer = 0
count_bad_answer = 0

def check_if_continue(answ):  # Check user answer
    if answ in continue_answer or answ in stop_answer:
        if answ in continue_answer:
            return True
        else:
            return False
    else:
        return False

exercise_counter = 0
print("Welcome to our Elementary Math, lets start")

def randomize_exercise():
    # Randomize exercise,num1,num2 & operator
    operator_sign = random.randrange(1, 5)
    num1 = random.randrange(1, 11)
    num2 = random.randrange(1, 11)

    if operator_sign == 1:
        exercise = str(num1) + "+" + str(num2)
    if operator_sign == 2:
        if num1 < num2:
          tmp = num1
          num1 = num2
          num2 = tmp
          exercise = str(num1) + "-" + str(num2)
    if operator_sign == 3:
        exercise = str(num1) + "*" + str(num2)
    if operator_sign == 4:
        while (num1 %num2) != 0 :
            num1 = random.randrange(1, 11)
            num2 = random.randrange(1, 11)
        exercise = str(num1) + "/" + str(num2)    
    return exercise

def check_user_answer(exercise):
    global count_good_answer
    global count_bad_answer
    answer = input("Enter your answer:")
    while answer.isdigit() == False:
        answer = input("Enter your answer:")
    if eval(exercise) == int(answer):
        count_good_answer += 1
        return True
    else:
        exercise = exercise + "=" + str(answer) + "(" + str(int(eval(exercise))) + ")"
        count_bad_answer += 1
        wrong_answer_array.append(exercise)
        return False


def main_flow():
    global exercise_counter
    exercise_counter += 1
    print("Question number " + str(exercise_counter))
    exercise = randomize_exercise()
    print(exercise + "=?")

    if check_user_answer(str(exercise)) == True:
        print("You Rigth")
    else:
        print("Wrong answer")

main_flow()
user_answer = input("Would you like to play again?")

while check_if_continue(user_answer) == True:
    main_flow()
    user_answer = input("Would you like to play again?")

print("here are your results: you answered correctly:" +
      str(count_good_answer) + " of " + str(exercise_counter) + " problems " +
      str(round((count_good_answer / exercise_counter) * 100)) + "%")
for i in range(len(wrong_answer_array)):
    print(wrong_answer_array[i])