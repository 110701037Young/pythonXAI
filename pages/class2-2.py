import streamlit as st

number = st.number_input("請輸入一個數字", step=1, min_value=0, max_value=100, value=60)

st.write(f"你輸入的數字是: {number}")

st.write("## 練習")
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

st.button("點我", key="button1")

if st.button("點我", key="button2"):
    st.balloons()

if st.button("點我", key="button3"):
    st.snow()
