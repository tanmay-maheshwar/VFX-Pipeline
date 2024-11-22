import streamlit as st
import pandas as pd


st.set_page_config(layout='wide')
st.title("SHOTLIGHT")

df = pd.read_excel('./Excels/data.xlsx','Sheet1',index_col =None)

st.data_editor(df,
             column_config={'#':st.column_config.Column(width='small',disabled=True),
                            'SHOT_NUMBER':st.column_config.Column(disabled=True),
                            'TASK':st.column_config.Column(disabled=True),
                            'STATUS':st.column_config.Column(disabled=True),
                            'THUMBNAIL':st.column_config.ImageColumn(),
                            'DEPARTMENT':st.column_config.Column(disabled=True),
                            'ARTIST':st.column_config.Column(disabled=True),
                            'START DATE':st.column_config.Column(disabled=True),
                            'ETA':st.column_config.Column(disabled=True),
                            'NOTES':st.column_config.Column(disabled=True,width='large')
                            },

               hide_index=True,

              )



