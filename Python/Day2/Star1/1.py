def show_sum(num):
    result = 0
    for number in num:
        if type(number) == int:
            result = result + number
    return result

mynum = [1, 2, 3,4,"sdfsdf",{1,2,3},6]
print(show_sum(mynum))