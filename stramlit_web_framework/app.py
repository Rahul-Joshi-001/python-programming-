import streamlit as st
import pandas as pd
import numpy as np

##Title of the application 
st.title("hello Streamlit")

##display simple text
st.write("this is a simple text")

##creating a dataframe
df = pd.DataFrame({
    'first':[1,2,3,4],
    'second': [10,20,30,40]
})

##display the data frame 
st.write("here is the dataframe ")
st.write(df)

##create a line chart
chart_data = pd.DataFrame({
    'x':[1,2,3,4,10],
    'y': [10,20,30,15,50]
}
)
st.line_chart(chart_data)