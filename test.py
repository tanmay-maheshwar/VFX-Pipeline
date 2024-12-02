import base64
import streamlit as st
import pandas as pd
import os

show_name = 'maha'
def thumbnail_path_generator(shot_name_local):
    thumbnail_path = f'T:/{show_name}/_ASSETS/thumbnails/{shot_name_local}_thumb.png'
    return thumbnail_path






df = pd.read_excel('./Excels/maha.xlsx')
shot_names = df['SHOT NAME']
thumbnail_paths = [thumbnail_path_generator(shot) for shot in shot_names]

df['THUMBNAIL'] = thumbnail_paths

print(df['THUMBNAIL'])