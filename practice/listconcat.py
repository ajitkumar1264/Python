def concat_list(nums):
    result=""
    for x in nums:
        result=result+str(x)
    return result

print(concat_list([1,2,3]))