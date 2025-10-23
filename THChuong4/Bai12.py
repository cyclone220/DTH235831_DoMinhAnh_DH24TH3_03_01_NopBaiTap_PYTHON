def oscillate(start, end):
    kq=[]
    for i in range(start,end):
        kq.append(i)
        kq.append(-i)
    return kq

for n in oscillate(-3,5):
    print(n,end=' ')
print()