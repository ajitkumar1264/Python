def first_2char(str,n):
    flen=2
    if flen >len(str):
        flen=len(str)
    substr=str[:flen]
    result=""
    for x in range(n):
        result=result+substr
    return result

print(first_2char("ajitk",5))
print(first_2char("a",5))