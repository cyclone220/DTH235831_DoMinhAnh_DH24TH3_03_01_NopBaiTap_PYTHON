def TinhSoGio():
    t = int(input("Nhập số giây: "))
    m = t%3600%24
    h = (int)(t/3600)%24
    s = t%3600%60
    buoi = " pm" if h >=12 else " am"
    print(h,":",m,":",s,buoi)

TinhSoGio()