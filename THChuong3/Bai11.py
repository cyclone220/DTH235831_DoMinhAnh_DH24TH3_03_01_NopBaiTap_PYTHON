while True:
    n=int(input("Nhập một số nguyên dương: "))
    isPrime=True
    for i in range(2,n):
        if n%i==0:
            isPrime=False
            break
    if n==1 or n==2 or isPrime:
        print(n,"là số nguyên tố")
    else:
        print(n,"không phải là số nguyên tố")
        
    check=input("Tiếp tục? (c/k): ")
    if check == "k":
        break