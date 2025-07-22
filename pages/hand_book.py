import streamlit as st

with st.expander("Class 1 課堂筆記"):
    st.write(
        """

    ## 🐍 Python 是什麼？

    Python 是一種電腦程式語言，就像人類說中文、英文，電腦也要用程式語言溝通。

    ---

    ## ✏️ 註解

    * `#` 開頭的是 **單行註解**，是寫給人看的，電腦不會執行。
    * 用 `\"""` 包起來的則是 **多行註解**，可以寫很多行的說明。

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

    * 字串可以用 `+` 連接起來，也可以用 `*` 重複：

    ```python
    s1 = "Hello"
    s2 = "World"
    print(s1 + s2)          # HelloWorld
    print(s1 + " " + s2)    # Hello World
    print(s2 * 3)           # WorldWorldWorld
    ```

    * f-string：把變數放進文字裡：

    ```python
    name = "Python"
    age = 31
    new_str = f"我是{name}, 今年{age}歲"
    print(new_str)  # 我是Python, 今年31歲
    ```

    * `len()` 可以看字串長度：

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

    * 把 True / False 變成數字：

    ```python
    print(int(True))     # 1
    print(int(False))    # 0
    ```

    * 把數字變成字串：

    ```python
    print(str(1000))     # "1000"
    ```

    * 把數字變成小數：

    ```python
    print(float(123))    # 123.0
    ```

    * 布林值的特別規則：

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
    st.markdown(\"""
    * **粗體文字**
    * *斜體文字*
    * [連結](https://www.example.com)
    * 程式碼：
    ```python
    print("Hello World!")
    ````

    # 標題1

    ## 標題2

    ### 標題3

    #### 標題4

    \""")

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


    """
    )

with st.expander("Class 2 課堂筆記"):
    st.write(
        """
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

"""
    )
