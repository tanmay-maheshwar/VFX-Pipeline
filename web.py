import streamlit as st
import pandas as pd
from modules import filter_parser as fp
import os


def show_name(show_excel_path_local):
    show_excel = show_excel_path_local.split('/')[-1]
    show_abbv = show_excel.split('.')[0]
    return show_abbv


def user_info():
    user_name = os.getlogin()
    user_name = user_name.replace('.',' ').title()
    return user_name


def filter_options(filepath='./appReq/status_filters.json'):
    with open(filepath,'r') as json_file:
        return json_file


def original_df(filepath='./Excels/maha.xlsx'):
    df_local= pd.read_excel(filepath,index_col='Sno.')
    df_local.fillna('',inplace=True)
    return df_local


def status_filter(filter_data_local):
    if filter_data_local == 'WIP':
        df_local = original_df()
        wip_df_local = df_local[df_local['STATUS'].str.contains('WIP')]
        return wip_df_local

    elif filter_data_local == 'APPROVED':
        df_local = original_df()
        app_df_local = df_local[df_local['STATUS'].str.contains('Approved')]
        return app_df_local

    elif filter_data_local == 'KICKBACK':
        df_local = original_df()
        kickback_df_local = df_local[df_local['STATUS'].str.contains('Kickback')]
        return kickback_df_local

    else:
        df_local = original_df()
        return df_local


def user_filter(user_filter_data_local):
    if user_filter_data_local == 'MY SHOTS':
        df_local = original_df()
        user_filter_df = df_local[df_local['ARTIST'].str.contains(user_info())]
        return user_filter_df
    else:
        df_local = original_df()
        return df_local


def dataframe_writer(edited_dataframe_local):
    edited_dataframe_local.to_excel(show_excel_path, sheet_name='Sheet1')




show_excel_path = './Excels/maha.xlsx'

st.set_page_config(layout='wide')

st.title("SHOTLIGHT")
st.divider()

top_left, top_right = st.columns([1, 1], gap="large")

df = original_df()
with top_left:
    selection= st.pills("Shot Status Filter :",fp.filter_options('./appReq/status_filters.json'),selection_mode='single',key='status_filter')
    if st.session_state['status_filter']:
       df = status_filter(st.session_state['status_filter'])
    print(st.session_state['status_filter'])

with top_right:
    selection01= st.pills("User Filter :",fp.filter_options('./appReq/user_filters.json'),selection_mode='single',key='user_filter')
    if st.session_state['user_filter']:
       df = user_filter(st.session_state['user_filter'])
    print(st.session_state['user_filter'])




#--------------------------------------------------------------MAIN_DATA_TABLE---------------------------------------------------------------------------------------




edited_df=st.data_editor(df,key='my_data',
                         column_config={'Sno.':st.column_config.Column(disabled=True),
                                        'SHOT NAME':st.column_config.Column(disabled=True),
                                        'TASK':st.column_config.Column(width='large',disabled=True),
                                        'STATUS':st.column_config.Column(),
                                        'THUMBNAIL':st.column_config.ImageColumn(),
                                        'DEPARTMENT':st.column_config.Column(disabled=True),
                                        'ARTIST':st.column_config.Column(disabled=True),
                                        'VERSION':st.column_config.Column(disabled=True),
                                        'START DATE':st.column_config.Column(disabled=True),
                                        'ETA':st.column_config.Column(disabled=True),
                                        'NOTES':st.column_config.Column(disabled=True,width='large')
                                        },

                           hide_index=True,
                           height=500,
                           num_rows='fixed'
                         )


#------------------------------------------------------------------SHOW_LABEL--------------------------------------------------------------------------------------

if not edited_df.equals(df):
    dataframe_writer(edited_df)




st.write(f'<header><b>Show-</b></header>\n{show_name(show_excel_path).capitalize()}',
         unsafe_allow_html=True)







