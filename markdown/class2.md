以下是幫你整理的《**今天 Python 上課筆記**》，用 **簡單、國小同學也能懂** 的方式說明，讓你複習起來更輕鬆！

---

## 🐍 Python 是什麼？

Python 是一種讓電腦聽得懂的語言，就像人跟人用中文或英文聊天，我們用 Python 跟電腦說話。

---

## ✅ 比較運算子：比一比誰大誰小

我們可以用一些符號來比較兩個數字：

| 指令 |        說明        |     範例結果     |
| :--: | :----------------: | :--------------: |
| `==` |    是不是一樣？    | `1 == 2` → False |
| `!=` |   是不是不一樣？   | `1 != 2` → True  |
| `>=` | 是不是大於或等於？ | `1 >= 2` → False |
| `<=` | 是不是小於或等於？ | `1 <= 2` → True  |
| `>`  |    是不是大於？    | `1 > 2` → False  |
| `<`  |    是不是小於？    |  `1 < 2` → True  |

---

## 🔀 邏輯運算子：讓電腦想一想

| 指令  |      用途      |           範例           |
| :---: | :------------: | :----------------------: |
| `not` |    反過來想    |    `not True` → False    |
| `and` |   同時都要對   | `True and False` → False |
| `or`  | 至少一個對就好 |  `False or True` → True  |

---

## 🔒 密碼驗證：教電腦判斷對不對

```python
password = input("請輸入密碼: ")
if password == "1234":
    print("密碼正確")
else:
    print("密碼錯誤")
```

還可以加更多人：

```python
if password == "1234":
    print("歡迎Ray")
elif password == "5678":
    print("歡迎Mike")
elif password == "abcd":
    print("歡迎Alice")
else:
    print("密碼錯誤")
```

---

## 📅 判斷閏年

如果輸入的年份可以被 4 整除，而且不能被 100 整除，或是能被 400 整除，就是閏年：

```python
year = int(input("請輸入年份: "))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(year, "是閏年")
else:
    print(year, "不是閏年")
```

---

## 🖱 Streamlit：互動小工具

Streamlit 是一個可以做漂亮互動網頁的工具。

例如：

- `st.number_input()`：讓大家輸入數字
- `st.write()`：顯示文字
- `st.button()`：按鈕
- `st.balloons()` / `st.snow()`：放氣球或下雪，好玩！

範例：

```python
import streamlit as st
number = st.number_input("請輸入一個數字", step=1, min_value=0, max_value=100, value=60)
st.write(f"你輸入的數字是: {number}")
```

---

## 🏫 分數判斷：幾分是什麼等第？

```python
score = st.number_input("請輸入分數", step=1, min_value=0, max_value=100, value=60)
if score >= 90:
    st.write("你的等第是A")
elif score >= 80:
    st.write("你的等第是B")
elif score >= 70:
    st.write("你的等第是C")
elif score >= 60:
    st.write("你的等第是D")
else:
    st.write("你的等第是F")
```

---

## 🔢 for 迴圈：重複做事情

讓電腦幫忙從 0 數到 9：

```python
for i in range(10):
    print(i)
```

還可以設定從 2 到 5：

```python
for i in range(2, 6):
    print(i)
```

或每次跳 2：

```python
for i in range(2, 10, 2):
    print(i)
```

---

## ⛩️ 金字塔：用數字或星星做出來

輸入一個數字，做數字金字塔：

```
1
22
333
```

輸入層數，做箭頭金字塔：

```
  *
 ***
*****
  *
  *
```

---

## 🍎 串列 List：裝很多東西的箱子

```python
L3 = ["蘋果", "香蕉", "橘子"]
L4 = [1, 2, 3, 4, 5]
L5 = [1, "蘋果", True, 3.14]
L6 = [1, 2, 3, ["蘋果", "香蕉"]]
```

取出裡面的東西：

```python
print(L6[1])        # → 2
print(L6[3][0])     # → "蘋果"
```

切一段出來：

```python
L = [1, 2, 3, "a", "b", "c"]
print(L[1:4:2])     # → [2, "a"]
print(L[::2])       # → [1, 3, "b"]
```

---

✨ **以上就是今天學到的重點**！
下次再複習，就可以更熟練～
如果想要，我也可以幫你畫成更好看的筆記圖喔！ 🌟
