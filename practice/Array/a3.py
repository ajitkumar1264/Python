from array import *

num=[10,20,30]

array_num=array("i",[])

print("In This We will learn how to add list data to the array")

array_num.fromlist(num)

print(array_num)

print("Insert items ar specific Locations")

array_num.insert(0,40)

print(array_num)

print("Pop the items in the Array")

array_num.pop(0)

print(array_num)

print("Remove the items from the Array")

array_num.remove(20)

print(array_num)

print("Convert our array to a list")

list1=array_num.tolist()

print(list1)