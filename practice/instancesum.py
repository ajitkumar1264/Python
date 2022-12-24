from numpy import blackman


def instance_sum(a,b):
    if not isinstance(a,int) and isinstance(b,int):
        return print("Type error is in that")
    else:
        sum=a+b
        return sum

print(instance_sum(5.0,10))