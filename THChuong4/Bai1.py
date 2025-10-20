from math import sqrt

a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

if (a<=0 or b <=0 or c <=0) or (a+b)<=c or (a+c)<=b or b+c<=a:
 print("Tam giác không hợp lệ")
else:
    cv = a+b+c
    p = cv/2
    dt = sqrt(p*(p-a)*(p-b)*(p-c))

    print(f"Chu vi = {cv:.3f}, Diện tích = {dt:.3f}")