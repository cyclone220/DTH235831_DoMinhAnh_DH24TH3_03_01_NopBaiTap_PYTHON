import math
x = int(input("Nhập x: "))
n = int(input("Nhập n: "))

s = 0
for i in range(n+1):
    s += float(x**(2*i + 1) / math.factorial(2*i + 1))
    
print(f"S = {s:.2f}")