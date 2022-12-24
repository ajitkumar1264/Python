yy=int(input("Enter the Year :"))
if (yy%4==0 and yy%100!=0 or yy%400==0):
    print(" this year is leap year")
else:
    print("The year is not leap year!")