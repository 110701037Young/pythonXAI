# 比較運算子

print(1 == 2)
print(1 != 2)
print(1 >= 2)
print(1 <= 2)
print(1 > 2)
print(1 < 2)

# 邏輯運算子

print(not True)
print(not False)

print(False and False)
print(False and True)
print(True and False)
print(True and True)  # True

print(False or False)
print(False or True)  # True
print(True or False)  # True
print(True or True)  # True

# 練習: 密碼驗證
password = input("請輸入密碼: ")

if password == "1234":
    print("密碼正確")

if password == "1234":
    print("密碼正確")
else:
    print("密碼錯誤")

if password == "1234":
    print("歡迎Ray")
elif password == "5678":
    print("歡迎Mike")
elif password == "abcd":
    print("歡迎Alice")
else:
    print("密碼錯誤")

year = int(input("請輸入年份: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "是閏年")
        else:
            print(year, "不是閏年")
    else:
        print(year, "是閏年")
else:
    print(year, "不是閏年")

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(year, "是閏年")
else:
    print(year, "不是閏年")
