import streamlit as st
import json
import openai

openai.api_key = st.secrets["OPENAI_API_KEY"]

# 讀取 JSON 題目
with open("question/quiz.json", "r", encoding="utf-8") as f:
    quiz = json.load(f)

# 初始化對話，讓 AI 扮演主持人
messages = [
    {
        "role": "system",
        "content": (
            "你是一位海龜湯遊戲的主持人，"
            "你只需要回答玩家的提問（是/否/無關），或在必要時給提示，"
            "絕對不要主動說出答案。\n"
            "如果玩家的回答已經很接近答案，那就說遊戲結束，並輸出正解\n"
            f"題目：{quiz['title']}\n"
            f"正解：{quiz['answer']}"
        ),
    }
]

print(quiz["title"])

# 玩家第一次提問
messages.append(
    {
        "role": "user",
        "content": "男人以前和女友出海時遇上暴風雨",
    }
)

# 呼叫 API
response = openai.chat.completions.create(model="gpt-4o", messages=messages)

print(response.choices[0].message.content)
