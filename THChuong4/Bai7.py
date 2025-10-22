from math import sqrt
def TinhLen(a,b):
    return sqrt((b["x"]-a["x"])**2+(b["y"]-a["y"])**2)

a = {"x": 0, "y": 0}
b = {"x": 0, "y": 0}

print("==== NHẬP TOẠ ĐỘ A ====")
a["x"]=int(input("Nhập X: "))
a["y"]=int(input("Nhập Y: "))

print("\n==== NHẬP TOẠ ĐỘ B ====")
b["x"]=int(input("Nhập X: "))
b["y"]=int(input("Nhập Y: "))

print(f"\nĐộ dài AB = {(TinhLen(a,b)):.2f}")