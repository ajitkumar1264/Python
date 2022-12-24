def count_list(nums):
    count=0
    for x in nums:
        if x is 4:
            count=count +1
    return count

print(count_list([1,2,3,4,5,6,4,5,9]))
print(count_list([1,2,3,4,5,4,4,4,9]))