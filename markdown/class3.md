以下是一篇**用簡單、適合國小同學也能懂的筆記**，幫助你回想今天學到的 Python 和 Streamlit 課程內容：

---

## 🍎 Python 基本操作回顧

### ✅ 看看清單裡有幾個東西：`len()`

```python
print(len([]))  # 空的清單，長度是0
print(len(["蘋果"]))  # 有一個東西，長度是1
print(len(["a", "b"]))  # 有兩個東西
print(len([1, 2, 3]))  # 有三個東西
```

---

### ✅ 用 `for` 迴圈看清單裡的東西

```python
l = [1, 2, 3]

# 用索引看
for i in range(len(l)):
    print(l[i])

# 直接看裡面的值
for element in l:
    print(element)
```

---

### ✅ 改變清單裡的東西

```python
l[0] = "A"
l[2] = "c"
print(l)  # 結果：['A', 2, 'c']
```

---

### ✅ 清單的複製和修改

```python
a = [10, 20, 30]
b = a  # 兩個變數指向同一個清單
b[1] = 200
print(a)  # a也被改了

c = [40, 50, 60]
d = c[:]  # 複製一份新的
d[1] = 500
print(c)  # c不會被改到
```

---

### ✅ 常用清單方法

```python
# append() 加一個東西到最後
l1 = [1, 2, 3]
l1.append(4)
print(l1)

# remove() 移除第一個出現的東西
l2 = ["a", "b", "c", "b", "a"]
l2.remove("b")
print(l2)

# pop() 移除最後一個或指定位置的東西
l3 = [1, 2, 3]
l3.pop()
print(l3)

l4 = [1, 2, 3]
l4.pop(1)  # 移除索引1的東西
print(l4)

# sort() 排序
l5 = [3, 1, 5, 3.3, 4, 2]
l5.sort()
print(l5)
```

---

## 🖼️ Streamlit 介紹

Streamlit 是幫助我們做**網頁**的小工具。

### ✅ 欄位

```python
col1, col2 = st.columns(2)
col1.button("按鈕1")
col2.button("按鈕2")
```

---

### ✅ 輸入文字

```python
text = st.text_input("請輸入文字")
st.write("你輸入的文字是:", text)
```

---

### ✅ session state (幫助我們記住變數)

```python
if "var1" not in st.session_state:
    st.session_state.var1 = 1

if st.button("add 1 to var1"):
    st.session_state.var1 += 1
    st.rerun()
```

---

## 🍔 做一個簡單的點餐機

- 輸入餐點
- 加到購物籃
- 可以刪掉

```python
food = col1.text_input("請輸入餐點")
if col2.button("加入"):
    st.session_state.order.append(food)
    st.rerun()
```

---

## 🔁 while 迴圈 & break

```python
i = 0
while i < 5:
    print(i)
    i += 1

# 如果想提早停止
i = 0
while i < 5:
    if i == 3:
        break
    print(i)
    i += 1
```

---

## 🎲 random 模組

- `random.randrange(1, 4)`：會得到 1、2 或 3
- `random.randint(10, 20)`：得到 10 到 20 的隨機整數

---

## 🎮 猜數字遊戲

電腦想好一個 1\~100 的數字，我們去猜：

```python
while True:
    guess = int(input("請輸入一個數字: "))
    if guess < target:
        print("再大一點")
    elif guess > target:
        print("再小一點")
    else:
        print("猜中了")
        break
```

---

## 🎁 一番賞小遊戲

- 有 100 張獎券，只有 1 張是中獎
- 一直抽，直到抽到中獎

```python
table = [0]*100
target = random.randint(1, 100)
table[target - 1] = 1

while True:
    pick = random.randint(1, 100)
    if table[pick - 1] == 1:
        print("恭喜你抽中了一番賞")
        break
    else:
        print("沒有中獎，繼續抽")
    table[pick - 1] = 2  # 標記已抽過
```

---

## ✏️ **小總結**

今天我們學會了：
✅ 清單的使用方法
✅ for & while 迴圈
✅ random 隨機數
✅ Streamlit 做網頁和記住資料

希望你看完可以複習，也能試著自己寫寫看！
如果想要，我也可以幫你畫圖或做流程圖來幫助理解喔～ 🌟
