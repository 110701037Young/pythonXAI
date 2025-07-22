import streamlit as st

st.write("## 數字金字塔")
num1 = st.number_input("請輸入一個數字(1-9)", step=1, min_value=1, max_value=9)
st.write("數字金字塔:")
for i in range(1, num1 + 1):
    st.write(str(i) * i)

st.write("## 箭頭金字塔")
num2 = st.number_input("請輸入箭頭的層數", step=1, min_value=1)
arrow = ""
for i in range(1, num2 + 1):
    arrow = arrow + (" " * (num2 - i) + "*" * (i * 2 - 1) + "\n")
for i in range(num2):
    arrow = arrow + (" " * (num2 - 1) + "*" + "\n")
st.write(
    f"""
```
箭頭金字塔:
{arrow}         
```
"""
)
