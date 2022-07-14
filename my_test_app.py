import streamlit as st
import pandas as pd
import seaborn as sns

st.title('Penguins')

penguins = sns.load_dataset('penguins')

option = st.selectbox('What penguin do you want?',('Gentoo','Adelie','Chinstrap'))

with st.expander("PENGUINS"):
    st.table(penguins[penguins.species == option])

col1, col2, col3 = st.columns(3)    

with col1:
    st.image('Images/Adelie.png',caption = 'Adelie')
with col2:
    st.image('Images/Chinstrap.png',caption = 'Chinstrap')
with col3:
    st.image('Images/Gentoo.png',caption = 'Gentoo')
# new_text = st.text_input('Movie title')    
# text1 = st.text('This is some text.')
# text1.body = new_text
# st.write('', text1.body)




    

