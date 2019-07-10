def sums(my_num,position):
    if position == len(my_num)-1:
        return my_num[0]
    tmp=sums(my_num,position+1)
    return tmp+my_num[position+1]

nums = [1,2,3,4,5]
print(sums(nums,0))