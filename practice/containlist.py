def contains_key(listword,n):
    for x in listword:
        if n==x:
            return True
    return False

print(contains_key([1,2,3,4,5],-5))