So_dict = {
    0: "",
    1: "Một",
    2: "Hai",
    3: "Ba",
    4: "Bốn",
    5: "Năm",
    6: "Sáu",
    7: "Bảy",
    8: "Tám",
    9: "Chín",
    10: "Mười"
}

print("Chương trình đọc số") 
while True:
    try:
        n = int(input("Nhập một số có tối đa 2 chữ số: "))
        if 0 <= abs(n) <= 99:  
            break
        else:
            print("Vui lòng nhập số không quá 2 chữ số.")
    except ValueError:
        print("Vui lòng nhập một số hợp lệ.")

if n <= 10:
    print(So_dict.get(n))
elif n < 20:
    dvi = n % 10
    print("Mười", So_dict.get(dvi))
else:
    chuc = n // 10
    dvi = n % 10
    if dvi==1:
        print(So_dict.get(chuc), "Mươi Mốt")
    else:
        print(So_dict.get(chuc), "Mươi", So_dict.get(dvi))
