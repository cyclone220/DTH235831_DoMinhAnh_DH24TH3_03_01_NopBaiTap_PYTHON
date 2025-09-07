import sys

if len(sys.argv) > 1:
    input_str = " ".join(sys.argv[1:])
    print("Chuỗi nhập vào:", input_str)
else:
    print("Bạn chưa nhập chuỗi nào từ tham số dòng lệnh.")
