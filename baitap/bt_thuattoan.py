m = int(input('nhap nam m :'))
n = int(input('nhap nam n :'))
a = []
for i in range(m,n+1):
	if i %4 == 0:
		a.append(str(i))
print(','.join(a))
