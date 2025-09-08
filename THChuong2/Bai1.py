import math

def TinhDienTichHinhTron():
    r = float(input("Nhập bán kính r: "))
    cv = 2 * math.pi * r
    dt = math.pi * r * r
    print("Diện tích hình tròn: ",dt)
    print("Chu vi hình tròn: ",cv)
    
TinhDienTichHinhTron()
