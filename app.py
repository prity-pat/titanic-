import seaborn as sns
import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt 

st.title('titanic datasets analysis_stramlit')

df = sns.load_dataset('titanic')

st.sidebar.header('User Input Parameters')
c = st.sidebar.selectbox('Select the class', df['class'].unique())
g = st.sidebar.selectbox('select the class', df['sex'].unique())

plot_type = st.radio('select the plot',('bar', 'line','hist', 'box','kde'))

if plot_type == 'bar':
    st.write('bar plot')
    fig, ax = plt.subplots()
    df.groupby(['class','sex'])['survived'].mean().unstack().plot(kind = 'bar', ax = ax)
    st.pyplot(fig)

elif plot_type == 'line':
    st.write('bar plot')
    fig, ax = plt.subplots()
    df.groupby(['class','sex'])['survived'].mean().unstack().plot(kind = 'line', ax = ax)
    st.pyplot(fig)


elif plot_type == 'hist':
    st.write('hist plot')
    fig, ax = plt.subplots()
    df.groupby(['class','sex'])['survived'].mean().unstack().plot(kind = 'hist', ax = ax)
    st.pyplot(fig)   

elif plot_type == 'box':
    st.write('box plot')
    fig, ax = plt.subplots()
    df.groupby(['class','sex'])['survived'].mean().unstack().plot(kind = 'box', ax = ax)
    st.pyplot(fig)  

elif plot_type == 'kde':
    st.write('kde plot')
    fig, ax = plt.subplots()
    df.groupby(['class','sex'])['survived'].mean().unstack().plot(kind = 'kde', ax = ax)
    st.pyplot(fig)            