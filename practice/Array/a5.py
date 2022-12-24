def first_duplicate(nums):
    num=set()

    for x in range(len(nums)):

        if nums[x] in num:
            return nums[x]
        else:
            num.add(nums[x])
    
    return -1


print(first_duplicate([10,10,40,60,50,50]))