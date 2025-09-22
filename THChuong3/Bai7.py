print("Chương trình tìm ngày kế tiếp")
day=int(input("Nhập ngày: "))
month=int(input("Nhập tháng: "))
year=int(input("Nhập năm: "))

print(f"Ngày đã nhập: {day}/{month}/{year}")
days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30,
                 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    days_in_month[2] = 29

if day < days_in_month[month]:
    day += 1
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1

print(f"Ngày tiếp theo là: {day}/{month}/{year}")