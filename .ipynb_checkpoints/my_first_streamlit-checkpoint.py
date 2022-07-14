import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

st.title('Penguins')

penguins = sns.load_dataset('penguins')

option = st.selectbox('Select species:',('Gentoo','Adelie','Chinstrap'))

with st.expander('PENGUINS DATA', expanded=False):
    st.table(penguins[penguins['species'] == option])
    
col1, col2, col3 = st.columns(3)

with col1:
    st.image('Images/Gentoo.png',caption = 'Gentoo')
with col2:
    st.image('Images/Adelie.png',caption = 'Adelie')
with col3:
    st.image('Images/Chinstrap.png',caption = 'Chinstrap')


