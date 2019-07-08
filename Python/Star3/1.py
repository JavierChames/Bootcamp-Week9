def analyze_number_digits():
    number = input("What is your number?")
    print("You entered number:" + number)
    sum=0
    for i in range(len((number))):
        print (number[i], end=",")
        sum=int(sum)+int(number[i])
    print("The sum of the digits of " + number + " is:" +str(sum))

analyze_number_digits()


