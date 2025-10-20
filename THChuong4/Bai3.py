def BMI(h,w):
    return w/(h**2)

def PhanLoai(bmi):
    if bmi < 18.5:
        return "Gầy"
    elif bmi<=24.9:
        return "Bình thường"
    elif bmi<=29.9:
        return "Hơi béo"
    elif bmi<=34.9:
        return "Béo phì cấp độ 1"
    elif bmi<=39.9:
        return "Béo phì cấp độ 2"
    else:
        return "Béo phì cấp độ 3"
    
h=float(input("Nhập chiều cao: "))
w=float(input("Nhập cân nặng: "))
print(PhanLoai(BMI(h,w)))
    
