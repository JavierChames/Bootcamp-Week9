for i in range(1,41):
     print(i)

a=1
while a <= 40:
    print (a)
    a=a+1


for i in range(1,101):
    if i %3 == 0:
        print("Fizz ")
    if i %5 == 0:
        print("Buzz ")
    if i %5 ==0 and i %3 == 0 :
         print("FizzBuzz ")
    else:
        print(str(i))