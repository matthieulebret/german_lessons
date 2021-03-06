import streamlit as st
import pandas as pd
import numpy as np
import requests
from st_aggrid import AgGrid

import altair as alt

st.set_page_config('German classes',layout='wide')

st.title('German language app')

@st.cache(suppress_st_warning=True,ttl=60)
def getdata():
    articles = pd.read_excel('german_vocab.xlsx',1,index_col = 0,header=0)
    pronouns = pd.read_excel('german_vocab.xlsx',2,index_col=0,header=0)
    words = pd.read_excel('german_vocab.xlsx',0)
    return articles,pronouns,words

articles,pronouns,words=getdata()

with st.expander('Articles and pronouns'):
    col1,col2 = st.columns([1.2,2])
    with col1:
        st.subheader('Articles')
        articles
    with col2:
        st.subheader('Pronouns')
        pronouns

st.subheader('Vocabulary')


highlight = alt.selection(type='interval',bind='scales',encodings=['x','y'])
fig = alt.Chart(words).mark_bar().encode(alt.X('Lesson number:N'),alt.Y('count()'),color='Phrase / Word:N').add_selection(highlight)
st.altair_chart(fig,use_container_width=True)


phrword = st.selectbox('Select words / phrases',['All','Words','Phrases'],0)

if phrword == 'Words':
    words = words[words['Phrase / Word']=='word']
elif phrword == 'Phrases':
    words = words[words['Phrase / Word']=='phrase']

AgGrid(words)
