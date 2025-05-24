from dotenv import load_dotenv
load_dotenv()

import os
import streamlit as st
from openai import OpenAI

# 専門家の種類とシステムメッセージ
experts = {
    "健康アドバイザー": "あなたは健康に関するアドバイザーです。安全なアドバイスを提供してください。",
    "金融コンサルタント": "あなたは金融の専門家です。投資や家計管理について分かりやすくアドバイスしてください。",
    "キャリアカウンセラー": "あなたはキャリアカウンセラーです。仕事や転職、キャリアアップについて親身にアドバイスしてください。",
    "ITエンジニア": "あなたはITエンジニアです。プログラミングやIT技術について分かりやすく説明してください。"
}

st.title("専門家AIチャット")

st.markdown("""
このWebアプリは、4種類の専門家AI（健康アドバイザー、金融コンサルタント、キャリアカウンセラー、ITエンジニア）に質問できるチャットサービスです。  
1. 相談したい専門家をラジオボタンで選択してください。  
2. 下のテキストエリアに相談内容を入力し、「AIに相談」ボタンを押してください。  
AIが選択した専門家として回答します。
""")

# 専門家の種類を選択
selected_expert = st.radio("相談したい専門家を選んでください", list(experts.keys()))

user_input = st.text_area("相談内容を入力してください", "")

def get_expert_answer(input_text: str, expert_key: str) -> str:
    """入力テキストと専門家種別を受け取り、LLMからの回答を返す"""
    client = OpenAI()
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": experts[expert_key]},
            {"role": "user", "content": input_text}
        ],
        temperature=0.5
    )
    return completion.choices[0].message.content

if st.button("AIに相談"):
    if user_input.strip() == "":
        st.warning("相談内容を入力してください。")
    else:
        answer = get_expert_answer(user_input, selected_expert)
        st.markdown("#### 回答")
        st.write(answer)