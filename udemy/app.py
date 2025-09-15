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