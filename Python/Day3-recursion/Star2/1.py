def max_num(my_num,index):
    if index == len(my_num):
        return 0
    big=max_num(my_num,index+1)
    if my_num[index]>big:
        return my_num[index]
    return big

nums = [1,8,3,4,5]
print(max_num(nums,0))