import streamlit as st
import pandas as pd
import numpy as np

st.title("Streamlit Text input:")


age = st.slider("select your age:",0,100,25)
st.write("your age is : ",age)

name = st.text_input("Enter Your name : ")
if name:
    st.write(f"Hello, {name}")

options=["python","java","c++","javascript"]
choice = st.selectbox("chosse your fav sub : ",options)
st.write(f"you chossed : {choice}")

data={
    "Name":["john","jane","jake","Jill"],
    "age":[28,24,35,40],
    "City":["New Yourk","los angles","chicago","Houston"]
}

df= pd.DataFrame(data)
st.write(df)

df.to_csv("sampledata.csv")
uploaded_file = st.file_uploader("choose a csv file",type='csv')
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)