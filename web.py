import streamlit as st
import pandas as pd


st.set_page_config(layout='wide')
st.title("SHOTLIGHT")

df = pd.read_excel('./Excels/data_01.xlsx','Sheet1',index_col =None)
print(df['ARTIST'][0])

st.data_editor(df,key='my_data',
             column_config={'Sno.':st.column_config.Column(width='small',disabled=True),
                            'SHOT NAME':st.column_config.Column(disabled=True),
                            'TASK':st.column_config.Column(width='large',disabled=True),
                            'STATUS':st.column_config.Column(disabled=True),
                            'THUMBNAIL':st.column_config.ImageColumn(),
                            'DEPARTMENT':st.column_config.Column(disabled=True),
                            'ARTIST':st.column_config.Column(),
                            'VERSION':st.column_config.Column(disabled=True),
                            'START DATE':st.column_config.Column(disabled=True),
                            'ETA':st.column_config.Column(disabled=True),
                            'NOTES':st.column_config.Column(disabled=True,width='large')
                            },

               hide_index=True,
               height=700

              )


data = st.session_state['my_data']['edited_rows']
data_list = list(data)

try:
    print(data_list)
except IndexError:
    pass
