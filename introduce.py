import streamlit as st
from PIL import Image
import pandas as pd
import altair as alt

st.set_page_config(page_title="自己紹介", page_icon="👨")

st.header("自己紹介をします!")
st.image("Image.jpg",width=100, caption="限界社会人")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### 👤 パーソナル
    - 名前:柏木理希
    - 出身地:福島県
    - 生年月日:1998年10月19日                

    ### 💼 職業  
    データサイエンティスト（JAST株式会社）
    """)

with col2:
    st.markdown("""
    ### 🏃 趣味  
    - ランニング（週4回）  
    - スポーツ観戦  
    - サウナでリフレッシュ
    
    ### 💰 経歴  
    - 金融機関で2年間法人営業  
    - 金融機関で1年間データサイエンティスト
    """)

st.markdown("---")

option = st.selectbox("どの話題に興味ある？", ["仕事", "ランニング", "サウナ"])

if option == "ランニング":
    st.write("月間100km走ってます🏃‍♂️")
elif option == "仕事":
    st.write("AI・機械学習のプロジェクトに関わっています！")
elif option == "サウナ":
    st.write("個人的No.1は岐阜の大垣サウナ🧖‍♂️")

st.markdown("---")
st.header("🏃おすすめランニングメニュー")
with st.expander("メニューを見る"):
    st.markdown(
    """
       -☑ 10キロjog(キロ:4分30秒) \n
       -☑ 200メートル 10本 \n
       -☑ 5キロペース走(4分45秒ペースから1キロ毎に10秒タイムを短縮)
    """)

st.markdown("---")
st.subheader("これからのチャレンジ")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ### 学びたい内容
    - 機械学習
    - 生成AI
    - SIerの全体像
        """)

with col2:
    st.markdown("""
   ### 今年の目標
   - pythonスキルの向上
   - フルマラソン参加
   - 貯金
""")
    
with col3:
    st.markdown("""
   ### 将来的にやりたい
  - データを使ったスポーツ分析
  - 沖縄への移住
""")


st.markdown("---")
st.subheader("ひとこと")
st.info("日々精進。走ることも、学ぶことも。")
st.success("人生もランも、コツコツ積み重ねが大事💪🔥")

st.markdown("---")
st.subheader("最後に")
name = st.text_input("あなたの名前は？")
if name:
    st.write(f"{name}さん、最後まで見てくれてありがとうございます！✨")

st.markdown("----")
st.caption("© 20250410 Riki Kashiwagi")