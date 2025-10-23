def tongUoc(n):
    sum=0
    for i in range(1,n-1):
        if n%i==0:
            sum+=i
    return sum
    
def isPerf(n):
    return tongUoc(n) == n

def isAbd(n):
    return tongUoc(n) > n
    
n=-1
while(n<=0): 
    n=int(input("Nhập số nguyên dương n: "))
    if n<=0:
        print("N phải là số nguyên dương")

perf=""
if isPerf(n):
    perf="là số hoàn thiện."
else:
    perf="không là số hoàn thiện."
    
abd=""
if isAbd(n):
    abd="là số thịnh vượng."
else:
    abd="không là số thịnh vượng."
    
print("a) "+f"{n} "+perf)
print("b) "+f"{n} "+abd)