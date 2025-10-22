from math import log

def TinhLog(a,x):
    return log(x)/log(a)

check = False
while not check:
    a = float(input("Nhập số thực a (a > 0 và a != 1): "))
    x = float(input("Nhập số thực x (x > 0): "))

    if a > 0 and x > 0 and a != 1:
        check = True
    else:
        print("Giá trị không hợp lệ, vui lòng nhập lại!\n")
        
print(f"alogx={(TinhLog(a,x)):.2f}")