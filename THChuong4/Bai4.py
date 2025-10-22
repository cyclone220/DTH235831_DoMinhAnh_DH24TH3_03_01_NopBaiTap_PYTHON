def TinhRoi(dt,chiphi):
    roi = dt - chiphi
    return roi

dt = int(input("Nhập doanh thu: "))
cp = int(input("Nhập chi phí: "))

roi=TinhRoi(dt,cp)

print(f"Tỉ lệ ROI = {roi:.2f}")
if roi >= 0.75:
    print("Nên đầu tư dự án.")
else:
    print("Không nên đầu tư dự án.")