import streamlit as st

st.title("BMI計算アプリ")

st.sidebar.header("ユーザー情報の入力")

name = st.sidebar.text_input("名前を入力", value="柏木理希")
gender = st.sidebar.selectbox("性別選択", ["男", "女", "その他"])
age = st.sidebar.number_input("年齢", min_value=0, max_value=120, value=25, step=1)

st.sidebar.write("身長(cm)体重(kg)を入力してください")
height = st.sidebar.slider("身長(cm)", 100, 200, 170)
weight = st.sidebar.slider("体重(kg)", 30, 150, 60)

st.write("下記のボタンを押してBMIを計算しましょう")

col1,col2 = st.columns(2)

with col1:
    caculate_button =st.button("BMIを計算")

with col2:
    show_detail = st.checkbox("BMI分類ガイドを表示")

    bmi = None

if caculate_button:
    bmi = 0
    if height > 0:
        bmi = round(weight / ((height / 100)**2),2)
        st.success(f"{name}さんのBMIは{bmi}です")

if show_detail:
    st.markdown("### BMI分類ガイド(WHO基準)")
    st.markdown(
        """
        -  **18.5未満**: 低体重
        -  **18.5~24.9**: 普通体重
        -  **25.0~29.9**: 過体重
        -  **30.0以上**: 肥満
        """
    )

if bmi is not None:
    if bmi < 18.5:
        st.info("現在、やや痩せ気味のようです。")
    elif 18.5 <= bmi < 25:
        st.info("標準的な範囲です。健康的な体重を維持しましょう。")
    elif 25 <= bmi < 30:
        st.warning("やや体重が多めです。生活習慣を見直すと良いかもしれません。")
    else:
        st.error("肥満の可能性があります。適切なダイエットや医療相談を検討しましょう。")
