def addition(a,b):
    return a+b
def substractor(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a//b
    
while True:
    print("calculator")
    print("0:for addition \n1:for substraction \n2:for multiplication \n3:for division \n4:exit")
    k=int(input("Enter the choice here : "))

    if(k==4):
        exit()
    else:
        num1=int(input("enter the first number : "))
        num2=int(input("Enter the second number here : "))

        if(k==0):
            i=addition(num1,num2)
            print("the addition of {} and {} is {}".format(num1,num2,i))
        elif(k==1):
            l=substractor(num1,num2)
            print("the substarction of {} and {} is {}".format(num1,num2,l))
        elif(k==2):
            l=multiply(num1,num2)
            print("the multiplication of {} and {} is {}".format(num1,num2,l))
        elif(k==3):
            l=divide(num1,num2)
            print("the division of {} and {} is {}".format(num1,num2,l))
