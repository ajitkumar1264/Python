l={}
def display():
    print("--------details--------------\n")
    for x in l:
        print("{} and number {}\n\n".format(x,l.get(x)))
while True:
    print("Contact number Data\n")
    print("0:Add new number \n1:Display all Numbers \n2:Find number \n3:delete Number \n4:Update Number \n5:exit \n")
    u=int(input("Enter your choice here : "))
    
    if u==0:
        name=input("Enter the Name : ")
        no=int(input("Enter the number : "))
        if(len(l)>11):
            print("Please enter the valid number")
        else:
            l[name]=no
            print("Successfully added !")
    elif u==1:
        if len(l)>0:
         display()
        else:
            print('contact list is empty')
    elif u==2:
        search_name=input("Enter the name : ")
        if search_name in l:
            print("\n",search_name," contact number is ",l[search_name],"\n")
        else:
            print("Name is not found in the contact number list \n")
    elif u==3:
        dele_name=input("Enter the Name : ")
        if dele_name in l:
            print("the current contact number is {} deleted\n".format(l[dele_name]))
            l.pop(dele_name)
            
        else:
            print("the name is not found")
         
    elif u==4:
         update_name=input("enter the name : ")
         if update_name in l:
            print("the contact no is {} \n".format(l[update_name]))
            tr=True
            while tr==True:
                update_no=int(input("Enter the new no : "))
                confirm_no=int(input("Enter the confirm no : "))
                if update_no !=confirm_no:
                    print("Please enter the same number as above")
                else:
                    l[update_name]=confirm_no
                    tr=False
                    print("Successfully updated the contact")

         else:
            print("Name is not found in the list") 

    elif u==5:
        exit()
