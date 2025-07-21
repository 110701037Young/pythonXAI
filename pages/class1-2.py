import streamlit as st

st.title("這是標題")
st.write("這是write寫的內容")
st.text("這是text寫的內容")
st.markdown(
    """
這是用markdown寫的字串
* **粗體文字**
* *斜體文字*
* [連結](https://www.example.com)
* 程式碼:
```python
print("Hello World!")
```
# 這是標題1
## 這是標題2
### 這是標題3
#### 這是標題4
"""
)
