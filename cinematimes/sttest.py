import streamlit as st
import pandas as pd
import numpy as np
from cinematimes import google
st.title('testing df display')
button2=st.button('hg')
if button2:
    with st.expander('hi'):
        subh = st.empty()#st.subheader("**Welcome!** This was a personal project practicing data sourcing with API's and HTML scraping")
        cols = st.columns([2,1.3])
        with cols[0]:
            col01=st.empty()#st.write('**Instructions**')
            col02=st.empty()#st.markdown("- You can select cinemas from the Cinema List to see what's now showing. \n - You can click the expanders below each movie to see details and a plot summary. \n - Below the movies you can click the expander to see the showtimes for each cinema. \n - If you'd like to add one more cinema to the list, you can search for it next to the list \n - *If there are a lot of movies it can take a while to collect all the information! Please be patient for a few seconds*☺️")
        with cols[1]:
            col11=st.empty()#st.write('**Sources**')
            col12=st.empty()#st.write("Images and details are collected from [imdb-api](https://imdb-api.com/)")
            col13=st.empty()#st.write("Google showtimes info is collected from [serp-api](https://serpapi.com/)")
            col14=st.empty()#st.write("Meguro Cinema info is scraped from [okura-movie](http://www.okura-movie.co.jp/meguro_cinema/now_showing.html)")
if not button2:
    subh = st.empty()#st.subheader("**Welcome!** This was a personal project practicing data sourcing with API's and HTML scraping")
    cols = st.columns([2,1.3])
    with cols[0]:
        col01=st.empty()#st.write('**Instructions**')
        col02=st.empty()#st.markdown("- You can select cinemas from the Cinema List to see what's now showing. \n - You can click the expanders below each movie to see details and a plot summary. \n - Below the movies you can click the expander to see the showtimes for each cinema. \n - If you'd like to add one more cinema to the list, you can search for it next to the list \n - *If there are a lot of movies it can take a while to collect all the information! Please be patient for a few seconds*☺️")
    with cols[1]:
        col11=st.empty()
        col12=st.empty()
        col13=st.empty()
        col14=st.empty()


intro = st.empty()
button = st.button('intro')

subh.subheader("**Welcome!** This was a personal project practicing data sourcing with API's and HTML scraping")
col01.write('**Instructions**')
col02.markdown("- You can select cinemas from the Cinema List to see what's now showing. \n - You can click the expanders below each movie to see details and a plot summary. \n - Below the movies you can click the expander to see the showtimes for each cinema. \n - If you'd like to add one more cinema to the list, you can search for it next to the list \n - *If there are a lot of movies it can take a while to collect all the information! Please be patient for a few seconds*☺️")

col11.write('**Sources**')
col12.write("Images and details are collected from [imdb-api](https://imdb-api.com/)")
col13.write("Google showtimes info is collected from [serp-api](https://serpapi.com/)")
col14.write("Meguro Cinema info is scraped from [okura-movie](http://www.okura-movie.co.jp/meguro_cinema/now_showing.html)")


cols = st.columns([1,4,2])
with cols[2]:
    inputcinema = st.text_input('To add one other cinema to the list, type a Google search here', '')
with cols[0]:
    st.write('')
    st.markdown('## **Cinema List**')
with cols[1]:
    cinemalist = ['Meguro Cinema','Urawa United Cinema', 'Toho Cinema Fujimi']
    if inputcinema != '':
        cinemalist.append(inputcinema)
    cinemas = st.multiselect('', cinemalist, key='multi')




if inputcinema != '':
    if inputcinema not in st.session_state:
        with st.spinner(f'Collecting showtimes and movie information for {inputcinema}...'):
          showtimes = google.extrasearch(inputcinema)
          st.session_state[inputcinema] = showtimes

if inputcinema in cinemas:
    st.header(f'📽️{inputcinema}')
    showtimes = st.session_state[inputcinema]
    if type(showtimes) != str:
        dfdict ={day['day'] +', '+ day['date']:df for day,df in zip(showtimes, google.eng_daily_df_list(showtimes))}
        with st.expander("See times"):
            col=st.columns([1,5])
            with col[0]:
                showday = st.radio('Select a date', options=dfdict.keys())
            with col[1]:
                for i in range(0,len(dfdict)):
                    st.write('')
                abc=st.empty()
            st.dataframe(dfdict[showday])
            abc.subheader(f'Looking at : {showday}')
    else:
        st.write(showtimes)
        st.write('Maybe try a more specific search?')
