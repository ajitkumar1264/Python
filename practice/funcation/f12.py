def palidrone(str):

    left_str=0
    right_str=len(str)-1
 
    while left_str<=right_str:

        if str[left_str]==str[right_str]:
            return True
        left_str+=1
        right_str-=1

    return False

print(palidrone("AjA"))