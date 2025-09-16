import streamlit as st
import pandas as pd

st.write("Hello World")

st.write("Hello :blue[World]")

st.title("Hello World")

st.title("Hello World :sunglasses:")

st.write(
    pd.DataFrame(
        {
            "first column":[1,2,3,4],
            "second column":[10,20,30,40],
        }
    )
)

st.link_button("Click here","https://paypayfleamarket.yahoo.co.jp")

st.header("Hello World",divider="rainbow")

code = """print("Hello)"""
st.code(code,language="python")


agree = st.checkbox("I agree")
if agree:
    st.write("Okay!")

options = st.multiselect(
    "好きな色はなんですか？",
    ["赤","緑","青","黄"]
)

st.write("あなたが選んだ色は:",options)

radio = st.radio(
    "好きな色はなんですか？",
    ["赤","緑","青","黄"]
)

st.write("あなたが選んだ色は:",radio)

df = pd.DataFrame(
    [
        {"colors":"赤","rating":4},
        {"colors":"緑","rating":5},
        {"colors":"青","rating":3},
    ]
)

edited_df = st.data_editor(df)
st.write(edited_df.loc[edited_df["rating"].idxmax()]["colors"])
df = pd.DataFrame(
    [
        {"colors":"赤","rating":4,"mark": True},
        {"colors":"緑","rating":5,"mark": True},
        {"colors":"青","rating":3,"mark": True},
    ]
)

edited_df = st.data_editor(df)
edited_df = edited_df[edited_df["mark"] == True]
st.write(edited_df.loc[edited_df["rating"].idxmax()]["colors"])

age = st.slider("あなたは何歳ですか？",0,130,40)
st.write("わたしは",age,"歳です")

import datetime
date = st.date_input("あなたが生まれたのはいつですか？",datetime.date(2000,1,1))
st.write("わたしは",date,"生まれです")

text = st.text_input("入力してください","XXXXXXXX")
st.write(text)

col1,col2 = st.columns(2)
with col1:
    st.title("Column1")
    st.write("これはカラムの1です")
with col2:
    st.title("Column2")
    st.write("これはカラムの2です")

tab1,tab2 = st.tabs(["tab1","tab2"])
with tab1:
    st.title("Tab1")
    st.write("これはタブの1です")
with tab2:
    st.title("Tab2")
    st.write("これはタブの2です")

with st.expander("もっと詳しく見る"):
    st.write("XXXXXXXXXXXXXXXXXXXXX")

with st.sidebar:
    st.title("XXXXXXXXXXXXXXXXXXXXX")
    st.write("XXXXXXXXXXXXXXXXXXXXX")

agree = st.checkbox("同意しますか？")
if agree == True:
    st.toast("Thank You",icon = "👍")

birthday = st.checkbox("今日はあなたの誕生日ですか？")
if birthday == True:
    st.toast("おめでとう！",icon = "👍")
    st.balloons()

st.page_link("app.py",label="Home",icon="☺️")
st.page_link("pages/page1.py",label="page1")
st.page_link("pages/page2.py",label="page2")
st.page_link("https://qiita.com/papasim824/items/1804bc1bd8d4c195d8a8",label="other")