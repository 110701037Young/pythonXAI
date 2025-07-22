下面是一份**用很簡單、適合國小同學看得懂**的 Python 上課筆記，幫助你回想今天學到的東西：

---

## 🐍 Python 是什麼？

Python 是一種電腦程式語言，就像人類說中文、英文，電腦也要用程式語言溝通。

---

## ✏️ 註解

- `#` 開頭的是 **單行註解**，是寫給人看的，電腦不會執行。
- 用 `"""` 包起來的則是 **多行註解**，可以寫很多行的說明。

---

## 📢 輸出（用 print）

可以用 `print()` 把東西顯示在螢幕上：

```python
print(123)         # 顯示數字
print(3.14)        # 顯示小數
print(True)        # 顯示布林值 True（代表「是」）
print(False)       # 顯示布林值 False（代表「不是」）
print("Hello")     # 顯示文字
```

---

## 📦 變數

變數就像一個盒子，可以放東西，也可以換東西：

```python
a = 10
print(a)      # 顯示 10
a = 20
print(a)      # 顯示 20
a = "apple"
print(a)      # 顯示 apple
```

---

## ➕➖✖️➗ 算數運算

Python 可以做加、減、乘、除：

```python
print(7 + 3)   # 10
print(7 - 3)   # 4
print(7 * 3)   # 21
print(7 / 3)   # 2.333...
print(7 // 3)  # 2，只要整數部分
print(7 % 3)   # 1，取餘數
print(2**3)    # 8，2 的 3 次方
```

---

## 🪄 字串（文字）

- 字串可以用 `+` 連接起來，也可以用 `*` 重複：

```python
s1 = "Hello"
s2 = "World"
print(s1 + s2)          # HelloWorld
print(s1 + " " + s2)    # Hello World
print(s2 * 3)           # WorldWorldWorld
```

- f-string：把變數放進文字裡：

```python
name = "Python"
age = 31
new_str = f"我是{name}, 今年{age}歲"
print(new_str)  # 我是Python, 今年31歲
```

- `len()` 可以看字串長度：

```python
print(len("Hello"))  # 5
print(len(""))       # 0
```

---

## 📚 型別（type）

可以用 `type()` 看一個東西是什麼型別：

```python
print(type(123))     # int（整數）
print(type(3.14))    # float（小數）
print(type("hi"))    # str（字串）
print(type(True))    # bool（布林值）
```

---

## 🔄 型別轉換

- 把 True / False 變成數字：

```python
print(int(True))     # 1
print(int(False))    # 0
```

- 把數字變成字串：

```python
print(str(1000))     # "1000"
```

- 把數字變成小數：

```python
print(float(123))    # 123.0
```

- 布林值的特別規則：

```python
print(bool(0))       # False
print(bool(1))       # True
print(bool(""))      # False
print(bool("hi"))    # True
```

---

## ⌨️ 輸入（input）

可以請使用者輸入資料：

```python
get = input("請輸入一些內容: ")
print(get)
print(type(get))  # 注意：輸入進來的都是字串型別
```

還可以算圓面積：

```python
r = int(input("請輸入圓的半徑:"))
area = 3.14 * r**2
print(f"圓的面積為: {area}")
```

---

## 🖼️ Streamlit（做漂亮網頁）

Streamlit 是一個可以幫助我們快速做網頁的小工具：

```python
import streamlit as st

st.title("這是標題")          # 網頁大標題
st.write("這是 write 寫的內容")
st.text("這是 text 寫的內容")
```

還可以用 markdown 寫更漂亮的文字：

````python
st.markdown("""
* **粗體文字**
* *斜體文字*
* [連結](https://www.example.com)
* 程式碼：
```python
print("Hello World!")
````

# 標題 1

## 標題 2

### 標題 3

#### 標題 4

""")

```

---

## ✅ 小結
今天我們學了：
- 註解
- print() 輸出
- 變數
- 加減乘除
- 字串
- 型別
- 型別轉換
- input() 輸入
- Streamlit 做網頁

只要多練習，就會越來越熟喔！
🚀 **加油！**
```
