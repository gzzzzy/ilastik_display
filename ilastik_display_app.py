import streamlit as st
import pandas as pd
import numpy as np

st.title('Ilastik display')

uploaded_files = st.file_uploader("上传ilastik结果文件", accept_multiple_files=True)
display_df = pd.DataFrame(columns=['file','count'])
for i,uploaded_file in enumerate(uploaded_files):
    df = pd.read_csv(uploaded_file)
    display_df.loc[i] = [
        uploaded_file.name,
        df['Predicted Class'].value_counts()['Lymphocytes']
    ]

st.dataframe(display_df, use_container_width=True,height=None)
