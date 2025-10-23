from time import sleep

for i in range(1, 8):
    for j in range(1, 8):
        if i < 5 and j < 5:
            if i == 4 or j == 4:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        elif i < 5 and j > 4:
            if j - 3 <= i:
                print("*", end=" ")
        if i>4 and j<5:
            if i - 3 <=j:
                print("*", end=" ")  
    print()
    
sleep(5)

for i in range(1, 8):
    for j in range(1, 8):
        if i < 5 and j < 5:
            if i == 4 or j == 4:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        elif i < 5 and j > 4:
            if j - i == 3 or i==4:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        if i>4 and j<5:
            if j==1 or i+j==8:
                print("*", end=" ")  
            else:
                print(" ", end=" ")
    print()
    
sleep(5)

for i in range(1,8):
    for j in range(1,8):
        if j>3 and i<5:
            if j+i<=8:
                print("*", end=" ")
        elif i>4 and j<5:
            if j==4 or i==7 or i+j>=8:
                print("*", end=" ")
            else:
                print(" ", end=" ")      
        else:
            print(" ", end=" ")          
    print()

print('\n')
sleep(5)
for i in range(1,8):
    for j in range(1,8):
        if j>3 and i<5:
            if i==1 or j==4 or j+i==8:
                print("*", end=" ")
            else:
                print(" ", end=" ") 
        elif i>4 and j<5:
            if j==4 or i==7 or i+j==8:
                print("*", end=" ")
            else:
                print(" ", end=" ")      
        else:
            print(" ", end=" ")          
    print()