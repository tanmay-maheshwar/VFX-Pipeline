import streamlit as st
import pandas as pd
from modules import filter_parser as fp


def show_name(show_excel_path_local):
    show_excel = show_excel_path_local.split('/')[-1]
    show_abbv = show_excel.split('.')[0]
    return show_abbv

def filter_options(filepath='./appReq/filters.json'):
    with open(filepath,'r') as json_file:
        return json_file

def original_df(filepath='./Excels/maha.xlsx'):
    df_local= pd.read_excel(filepath)
    return df_local


def current_df(filter_data_local):

    if filter_data_local == 'WIP':
        df = original_df()
        wip_df_local = df[df['STATUS'].str.contains('WIP')]
        return wip_df_local

    elif filter_data_local == 'APPROVED':
        df = original_df()
        app_df_local = df[df['STATUS'].str.contains('Approved')]
        return app_df_local

    elif filter_data_local == 'KICKBACK':
        df = original_df()
        kickback_df_local = df[df['STATUS'].str.contains('Kickback')]
        return kickback_df_local

    else:
        df = original_df()
        return df




    



st.set_page_config(layout='wide')

show_excel_path = './Excels/maha.xlsx'

st.title("SHOTLIGHT")
st.divider()
selection= st.pills("Filters:",fp.filter_options(),selection_mode='single',key='filter_selection')






df = current_df(st.session_state['filter_selection'])
#--------------------------------------------------------------MAIN_DATA_TABLE---------------------------------------------------------------------------------------




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
               height=700,


              )


#------------------------------------------------------------------SHOW_LABEL--------------------------------------------------------------------------------------


st.write(f'<header><b>Show-</b></header>\n{show_name(show_excel_path).capitalize()}',
         unsafe_allow_html=True)

data = st.session_state['my_data']['edited_rows']
data_list = list(data)



# try:
#     print(type(data))
#     print(data)
# except IndexError:
#     pass


