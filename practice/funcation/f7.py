def stringCheker(s):

    d={"UPPERCASE":0,"LOWERCASE":0}

    for c in s:
        if c.isupper():
            d["UPPERCASE"]+=1
        elif c.islower():
            d["LOWERCASE"]+=1
        else:
            pass
    print("The original string :",s)
    print("No of uppercase letter :",d["UPPERCASE"])
    print("No of Lowercase letter :",d["LOWERCASE"])

stringCheker("Ajitvaghela")
        