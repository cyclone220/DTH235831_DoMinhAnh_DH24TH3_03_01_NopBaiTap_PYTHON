def HinhVuong(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i==n-1 or j == 0 or j==n-1:
                print("*", end = " ")
            else: print(" ", end = " ")
        print()
        
def TamGiac(n):
    for i in range(n):
        for j in range(n):
            if i + j >= n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
def DoubleTG(n):
    for i in range(n*2):
        for j in range(n*2):
            if i <n and j<n:
                if j == 0 or i==j or i==n-1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            else: 
                if j == n*2-1 and i>=n or i==j or i==n-1:
                        print("*", end=" ")
                else:
                    print(" ", end=" ")
        print()


n=int(input("Nhập số N: "))
HinhVuong(n)
print("\n============\n")
TamGiac(n)
print("\n============\n")
DoubleTG(n)
    