from random import randrange
while True:
    somay = randrange(1,100)
    win=False
    count=0
    while count<7:
        count+=1
        doan=int(input("Máy đoán [1..100], mời bạn đoán: "))
        print("Bạn đoán lần thứ",count)
        if doan==somay:
            win=True
            break
        elif doan > somay:
            print("Số bạn đoán lớn hơn số máy.")
        else: 
            print("Số bạn đoán bé hơn số máy.")
    if win:
        print("Bạn đã thắng.")
    else:
        print("Bạn thua, số máy =",somay)
    cont = input("Bạn có muốn tiếp tục không? c/k: ")
    if cont == 'k':
        print("Hẹn gặp lại")
        break
    else:
        print("\n===========\n")