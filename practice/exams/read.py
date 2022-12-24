"""with open("E:/Python/practice/exams/ajit.txt","a") as f:
    
    f.write("hello world!")
    """

"""f=open("E:/Python/practice/exams/ajit.txt","rt")
list=f.readline()
for l in list:
    print(l)
    """
with open("E:/Python/practice/exams/book.csv") as f:
    rows=f.readlines()
    iffirstline=True
    print(rows)
    for r in rows:
        if iffirstline:
            iffirstline=False
            continue
        cols=r.split(",")
        print('student name',cols[1])