以下是一份**適合國小同學看得懂**的 Python 上課筆記，幫助你複習今天學到的內容：

---

## 🗂️ 字典（Dictionary）

就像一本小字典一樣，我們可以用「關鍵字」找到對應的「值」。

```python
d2 = {"apple": "蘋果"}
d3 = {1: "one", 2: "two", 3: "three"}

print(d2["apple"])  # 會印出 蘋果
print(d3[2])        # 會印出 two
```

---

## 🔑 字典常用功能

- **列出所有 key（關鍵字）**

```python
for key in d3.keys():
    print(key)
```

- **列出所有值（value）**

```python
for value in d3.values():
    print(value)
```

- **列出 key 和 value**

```python
for key, value in d3.items():
    print(f"{key}: {value}")
```

- **修改值或新增**

```python
d3[2] = "二"    # 把 key=2 的值改掉
d3[4] = "four" # 新增一個 key=4
```

- **刪除值**

```python
v = d3.pop(1)  # 刪除 key=1
print(f"刪掉的值: {v}")
```

- **長度**

```python
print("d3的長度", len(d3))
```

- **檢查有沒有某個 key**

```python
print(2 in d3)       # True
print("three" in d3) # False，因為 "three" 是值不是 key
```

---

## 📦 清單（List）的判斷

```python
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits) # True
print("orange" in fruits) # False
```

---

## 🖼️ Streamlit - 做小網站

### 顯示圖片

```python
import streamlit as st
import os

files = os.listdir("image")  # 找出 image 資料夾裡所有檔案
st.write(files)

img_size = st.number_input("圖片大小", min_value=50, max_value=500, value=300, step=50)

for img in files:
    st.image(f"image/{img}", width=img_size)
```

---

### 做一個簡單的購物平台

- 可以看到每個商品的圖片、價格和庫存
- 可以按按鈕購買，庫存就會減少
- 還可以新增庫存

重點：用 `st.session_state` 記住所有商品的資料。

---

## 👋 函式（Function）

就像做工具，寫好一次可以重複用。

```python
def hello():
    print("hello")

def hello2(name):
    print("hello " + name)

def my_max(a, b):
    if a > b:
        return a
    else:
        return b

def calculate_circle_area(r, pi=3.14, scale=1):
    return (r * scale) ** 2 * pi
```

---

## 🧪 函式的使用

```python
hello()                        # 印出 hello
hello2("Tom")                  # 印出 hello Tom
print(my_max(10, 20))          # 比較大小
print(calculate_circle_area(10))       # 計算圓面積
print(calculate_circle_area(10, scale=2)) # 放大後再算
```

---

## 🔧 區域變數和全域變數

- 在函式裡面用的變數，外面用不到。
- 如果想要在外面也能用，要用 `global`。

---

## 📏 計算距離

```python
def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
```

輸入兩個座標，就能算出它們的距離。

---

## 🎲 模擬擲骰子

```python
import random

def roll_dice(n):
    save = []
    for i in range(n):
        number = random.randint(1, 6)
        save.append(number)
    return save

N = int(input("次數:"))
outcome = roll_dice(N)
print("結果:", outcome)
```

再用迴圈去數每個點數出現了幾次。

---

## ✨ 今天學到的重點

✅ 字典的增刪改查
✅ Streamlit 做小網站
✅ 自訂函式
✅ 全域變數和區域變數
✅ 計算距離
✅ 擲骰子和統計

---

如果還想要更詳細或加圖片解釋，也可以再跟我說！ 🌟
