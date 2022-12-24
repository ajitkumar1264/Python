def max(a,b):
    if a<b:
        return b
    return a

def max_of_there(a,b,c):
    return max(a,max(b,c))

print(max_of_there(9,8,6))