def Test_duplicate(array_nums):
    nums_set=set(array_nums)
    return len(nums_set)!=len(array_nums)

print(Test_duplicate([10,20,40,40,50]))