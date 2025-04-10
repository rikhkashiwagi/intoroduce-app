import streamlit as st
col1, col2= st.columns(2)
col1.write("左")
col2.write("右")

user_input = st.text_input("名前を入力してください")
st.write(f"こんにちは、{user_input}さん")

age = st.number_input("年齢を入力",min_value=0, max_value=120, value=20, step=1)
st.write(f"あなたの年齢は{age}ですね")

agree = st.checkbox("同意します")
if agree:
    st.write("同意ありがと")

c = st.selectbox("好きな色を選んでください",["赤", "青", "緑"])
st.write(f"あなたの選んだ色は{c}です")

fruit = st.radio("フルーツを選択",["リンゴ","バナナ","みかん"])
st.write(f"選択されたのは{fruit}です")

value = st.slider("値を選択してください", 0, 100, 50)
st.write(f"現在の値: {value}")

if st.button("クリックしてメッセージを表示"):
    st.write("ボタンが押されました！")