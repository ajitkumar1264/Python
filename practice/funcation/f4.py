def string_reverse(str1):
    str2=''
    index=len(str1)
    while index>0:
        str2+=str1[index-1]
        index=index-1
    return str2

print(string_reverse("ajitkumar"))