import streamlit as st

st.title("這是標題")
st.write("這是內容")
st.text("這是純文字")
st.markdown(
    """
可以處理markdown語法\n
例如:\n
* **粗體**\n
* *斜體*
* [連結](https://www.example.com)
* 代碼塊:
```python
print("hello world")
```
"""
)
