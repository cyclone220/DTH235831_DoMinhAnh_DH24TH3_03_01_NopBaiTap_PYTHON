def nhap_diem(mon):
    while True:
        try:
            diem = float(input(f"Nhập điểm {mon} (0-10): "))
            if 0 <= diem <= 10:
                return diem
            else:
                print("Điểm phải nằm trong khoảng 0 đến 10.")
        except ValueError:
            print("Vui lòng nhập số hợp lệ.")

def TinhDiemTrungBinh():
    diemToan = nhap_diem("Toán")
    diemLy   = nhap_diem("Lý")
    diemHoa  = nhap_diem("Hoá")
    
    
    
    dtb = (diemHoa+diemLy+diemToan)/3
    print(f"Điểm trung bình: {dtb:.2f}")
    
TinhDiemTrungBinh()
