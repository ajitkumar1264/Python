print("enter the height")
h_ft=int(input("enter the Feet :"))
h_inch=int(input("enter the inches :"))

h_inch=h_inch+h_ft*12
h_cm=round(h_inch*2.54,1)

print(h_cm,"cm")
