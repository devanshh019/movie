import streamlit as st
import pandas as pd
import numpy as np
import pickle

from matplotlib.pyplot import title

st.title("MOVIE RECOMMENDATION BY DEVANSH")
sim=pickle.load(open('sim.pkl','rb'))
title=pickle.load(open('title.pkl','rb'))
options = st.selectbox(' select your option ',title.values)
def recommendation(name):
    movies=[]
    ind=title[title==name].index[0]
    simmaliraty=sim[ind]
    movie_list=sorted(list(enumerate(simmaliraty)),reverse=True,key=lambda x:x[1])[1:6]
    for i in movie_list:
        movies.append(pd.DataFrame(title).iloc[i[0]].title)
    return movies

if st.button('Recommend'):
    names=recommendation(options)
    for i in names:
        st.write(i)