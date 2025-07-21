"""
這
是
多
行
註
解
"""

# 這是單行註解

print(123)  # 輸出整數
print(3.141592653589793)  # 輸出浮點數
print(True)  # 輸出布林值
print(False)  # 輸出布林值
print("Hello world")  # 輸出字串

a = 10  # 建立變數
print(a)
a = 20  # 重新賦值
print(a)
a = "apple"  # 變更為字串
print(a)

x = 4
x = x + 3
print(x)
x = x * 2
print(x)

print(7 + 3)  # 加法
print(7 - 3)  # 減法
print(7 * 3)  # 乘法
print(7 / 3)  # 除法
print(7 // 3)  # 整數除法
print(7 % 3)  # 取餘數
print(2**3)  # 指數運算

s1 = "Hello"
s2 = "World"
s3 = s1 + " " + s2
print(s1 + s2)  # 字串連接
print(s3)
print(s1 + s2 * 3)  # 字串重複

name = "Python"
age = 31
new_str = f"我是{name}, 今年{age}歲"
print(new_str)

print(len(""))  # 輸出空字串的長度
print(len("Hello"))  # 輸出字串的長度

print(type(True))  # 布林值類型
print(type(123))  # 整數類型
print(type(123.0))  # 浮點數類型
print(type("hello"))  # 字串類型

print(int(True))
print(int("123"))
# print(int("hello")) # 這行會報錯，因為無法將字串轉換為整數

print(float(True))
print(float("123"))
# print(float("hello")) # 這行會報錯，因為無法將字串轉換為浮點數

print(bool(0))  # False
print(bool(1))  # True
print(bool(-2))  # True
print(bool("hello"))  # True
print(bool(""))  # False

print(str(True))
print(str(1000))
print(str("yes"))

# get = input()
get = input("請輸入一些內容: ")  # 使用 input 函數獲取用戶輸入
print(get)
print(type(get))

r = int(input("請輸入圓的半徑:"))
area = 3.14 * r**2  # 計算圓的面積
print(f"圓的面積為: {area}")  # 使用 f-string 輸出結果
print("圓的面積為: " + str(area))  # 使用字串連接輸出結果
print("圓的面積為:", area)  # 使用格式化字串輸出結果
