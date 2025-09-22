import math

print("Chuong trinh giai phuong trinh bac hai") 
a=float(input("Nhap a: "))
b=float(input("Nhap b: "))
c=float(input("Nhap c: "))

delta=b*b-4*a*c

if a==c==b==0:
    print("Phuong trinh co vo so nghiem.")
elif delta<0:
    print("Phuong trinh vo nghiem.")
elif delta==0:
    x=-b/2*a
    print(f"Phuong trinh co nghiem kep x={x:.2f}")
else:
    x1=(-b-math.sqrt(delta))/2*a
    x2=(-b+math.sqrt(delta))/2*a
    print(f"Phuong trinh co 2 nghiem x1={x1:.2f}, x2={x2:.2f}")