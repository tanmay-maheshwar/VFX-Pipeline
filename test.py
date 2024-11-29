import streamlit as st
import pandas as pd
import os


def user_info():
    user_name = os.getlogin()
    user_name = user_name.replace('.',' ').title()
    print(user_name)
    return user_name


df = pd.read_excel('./Excels/maha.xlsx')
print(df['ARTIST'].str.contains(user_info()))
