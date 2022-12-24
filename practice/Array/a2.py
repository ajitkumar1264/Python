from array import *

array_num=array("i",[10,20,30,40,50])

print(array_num)

print("After append the item in array")

array_num.append(40)

print(array_num)

print("Reverse the current array using Reverse function")

array_num.reverse()

print(array_num)

print("The Current Array Length find using the itemSize function "+str(array_num.itemsize))

print("The Current Buffer Information is "+str(array_num.buffer_info()))
print("The Current Memory Information is "+str(array_num.buffer_info()[1]*array_num.itemsize))

print("Count the item or Number Repeat the  ")

print("the 40 Number is Occur in the Array "+str(array_num.count(40))+ "Times")

array_num.extend(array_num)

print(array_num)

print("Conver array items in means Bytes to String")

s=array_num.tobytes()

print(s)

