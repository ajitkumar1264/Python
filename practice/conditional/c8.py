row_num=int(input("enter the row entry here"))
col_num=int(input("enter the column entry here"))

multi_list=[[0 for col in range(col_num)]for row in range(row_num)]

for row in range(row_num):
    for col in range(col_num):
        multi_list[row][col]=row*col


print(multi_list)