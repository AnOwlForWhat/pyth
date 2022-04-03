'''Viết chương trình Python cho phép nhập vào 3 số thực là điểm số của 3 môn thi.
 In ra màn hình “Qua mon” nếu điểm trung bình >= 5.0 ngược lại in ra “Khong qua mon”.
  Điểm trung bình lấy 4 chữ số thập phân. '''

toan = float(input('nhap diem toan: '))
tin = float(input('nhap diem tin: '))
ly = float(input('nhap diem ly: '))
avg = ((toan+ly + tin)/3)
print(round(avg,4))
print("qua mon") if avg>=5 else print("khong qua mon") if avg <= 5 else print("nhap loi")
