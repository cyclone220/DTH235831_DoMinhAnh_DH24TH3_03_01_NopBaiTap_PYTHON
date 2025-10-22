from math import sqrt
def TinhNCan(n):
    if n == 1:
        return sqrt(2)
    return sqrt(2+TinhNCan(n-1))

n=int(input("Nhập n: "))

print(f"Kết quả = {(TinhNCan(n)):.2f}")