import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

st.title = ("irisデータを用いた予測アプリ")

iris = load_iris()
x = pd.DataFrame(iris.data,columns=iris.feature_names)
y = pd.Series(iris.target, name = "species")

st.write(iris)
st.write(x)
st.write(ｙ)

