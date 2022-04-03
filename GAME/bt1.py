m = int(input('nhap hang m=  '))
n = int(input('nhap n='))
a=[]
for i in range(n):
    tam=[]
    for i in range(n):
        tam.append(int(input('nhap gia tri:')))
    a.append(tam)
print('a=',a)