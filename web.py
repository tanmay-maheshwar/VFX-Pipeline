import streamlit as st
import pandas as pd

st.title("SHOTLIGHT")

df = pd.DataFrame([1,2,3,4,5,6,7,8,9,10]
             ,columns=["Shot_Number","Task"])
st.dataframe(df)