a = float(input("Nhập giá trị a: "))
b = float(input("Nhập giá trị b: "))
phep = input("Nhập phép toán (+, -, *, /): ")

if phep == '+':
    print(f"Kết quả: {a} + {b} = {a + b}")
elif phep == '-':
    print(f"Kết quả: {a} - {b} = {a - b}")
elif phep == '*':
    print(f"Kết quả: {a} * {b} = {a * b}")
elif phep == '/':
    if b != 0:
        print(f"Kết quả: {a} / {b} = {a / b}")
    else:
        print("Lỗi: Không thể chia cho 0")
else:
    print("Phép toán không hợp lệ")
