import streamlit as st
import pandas as pd
import numpy as np

st.title("This is the app title")
st.header('This is the app header')
st.markdown("### this is the app markdown")

st.write("Hello world")

## filters and buttons
st.checkbox("yes")
st.button("click")
st.radio("Pick your sport", ["basketball", "football"])
st.selectbox("Pick your sport", ["basketball", "football"])
st.multiselect("Pick your sport", ["basketball", "football"])

## sidebar
st.sidebar.title("this is my sidebar")
st.sidebar.button("click")
st.sidebar.radio("pick your color", ["red", "blue"])

## data viz (2 charts)
df = pd.DataFrame(np.random.randn(10,2), columns=["x", "y"])
st.line_chart(df)
