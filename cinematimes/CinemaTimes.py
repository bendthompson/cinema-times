import streamlit as st
st.set_page_config(layout="wide") #defaults the page to wide layout
import pandas as pd
from cinematimes import imdb
from cinematimes import meguro
from cinematimes import google

st.title("Some Cinema Times🎬")

if not st.session_state.get('multi'):
    subh = st.empty()
    desc = st.empty()
    cols = st.columns([2,1.3])
    with cols[0]:
        col01=st.empty()
        col02=st.empty()
    with cols[1]:
        col11=st.empty()
        col12=st.empty()
        col13=st.empty()
        col14=st.empty()
    st.write('')
    ghli=st.empty()

if st.session_state.get('multi'):
    with st.expander('See Introduction & Instructions'):
        subh = st.empty()
        desc = st.empty()
        cols = st.columns([2,1.3])
        with cols[0]:
            col01=st.empty()
            col02=st.empty()
        with cols[1]:
            col11=st.empty()
            col12=st.empty()
            col13=st.empty()
            col14=st.empty()
        st.write('')
        ghli=st.empty()

subh.subheader("**Welcome!**")
desc.markdown("##### This is a personal project where I used web scraping and API's to source movie showtimes and information for my favourite cinemas")

col01.write('**Instructions**')
col02.markdown("- You can select cinemas from the Cinema List to see what's now showing. \n - You can click the expanders below each movie to see details and a plot summary. \n - Below the movies you can click the expander to see the showtimes for each cinema. \n - If you'd like to add one more cinema to the list, you can search for it next to the list \n - *If there are a lot of movies it can take a while to collect all the information! Please be patient for a few seconds*☺️")

col11.write('**Sources**')
col12.write("Images and details are collected from [imdb-api](https://imdb-api.com/)")
col13.write("Google showtimes info is collected from [serp-api](https://serpapi.com/)")
col14.write("Meguro Cinema info is scraped from [okura-movie](http://www.okura-movie.co.jp/meguro_cinema/now_showing.html)")
ghli.markdown('##### Learn more or connect with me, Ben Thompson, on [Github](https://github.com/bendthompson) and [LinkedIn](https://www.linkedin.com/in/ben-d-thompson/)')

cols = st.columns([1,4,2])
with cols[2]:
    inputcinema = st.text_input('Google search for another cinema here', '')
with cols[0]:
    st.write('')
    st.markdown('## **Cinema List**')
with cols[1]:
    cinemalist = ['Meguro Cinema','Urawa United Cinema', 'Toho Cinema Fujimi']
    if inputcinema != '':
        cinemalist.append(inputcinema)
    cinemas = st.multiselect('', cinemalist, key='multi')


if 'Meguro Cinema' in st.session_state['multi']:
    if 'meguro_info' not in st.session_state:
        with st.spinner('Collecting showtimes and movie information for Meguro Cinema...'):
            soup = meguro.get_soup()
            meg_info = meguro.meguro_info(soup)
            meg_list = meguro.meguro_eng_list(meg_info)
            meg_imdb_search = imdb.search_list(meg_list)
            meg_imdb_info = imdb.info_list(meg_imdb_search)
            meg_df = meguro.meguro_info_df(meg_info)
            st.session_state['meguro_info'] = meg_imdb_info
            st.session_state['meguro_df'] = meg_df


if 'Urawa United Cinema' in st.session_state['multi']:
    if 'urawa_info' not in st.session_state:
        with st.spinner('Collecting showtimes and movie information for Urawa United Cinema...'):
            showtimes = google.search('united cinemas urawa')
            urawa_dfs = google.eng_daily_df_list(showtimes)
            urawa_list = google.eng_movie_list(showtimes)
            urawa_imdb_search = imdb.search_list(urawa_list)
            urawa_imdb_info = imdb.info_list(urawa_imdb_search)
            st.session_state['urawa_info'] = urawa_imdb_info
            st.session_state['urawa_dfs'] = urawa_dfs
            st.session_state['urawa_sts'] = showtimes


if 'Toho Cinema Fujimi' in st.session_state['multi']:
    if 'toho_info' not in st.session_state:
        with st.spinner('Collecting showtimes and movie information for Toho Cinema Fujimi...'):
            showtimes = google.search('toho cinema lalaport fujimi')
            toho_dfs = google.eng_daily_df_list(showtimes)
            toho_list = google.eng_movie_list(showtimes)
            toho_imdb_search = imdb.search_list(toho_list)
            toho_imdb_info = imdb.info_list(toho_imdb_search)
            st.session_state['toho_info'] = toho_imdb_info
            st.session_state['toho_dfs'] = toho_dfs
            st.session_state['toho_sts'] = showtimes

if inputcinema != '':
    if inputcinema not in st.session_state:
        with st.spinner(f'Collecting showtimes and movie information for {inputcinema}...'):
          showtimes = google.extrasearch(inputcinema)
          st.session_state[inputcinema] = showtimes

if 'Meguro Cinema' in cinemas:
    meg_imdb_info = st.session_state['meguro_info']
    meg_df = st.session_state['meguro_df']

if 'Urawa United Cinema' in cinemas:
    urawa_imdb_info = st.session_state['urawa_info']
    urawa_dfs = st.session_state['urawa_dfs']
    urawa_sts = st.session_state['urawa_sts']

if 'Toho Cinema Fujimi' in cinemas:
    toho_imdb_info = st.session_state['toho_info']
    toho_dfs = st.session_state['toho_dfs']
    toho_sts = st.session_state['toho_sts']



if 'Urawa United Cinema' in cinemas:
    st.header('📽️Urawa United Cinema')


    length=len(urawa_imdb_info) #movies will be displayed in rows of 4
    rows=length//4
    rem=length%4
    cols = st.columns([1,1,1,1])

    if rows >=1:
        for index in range(0,4):
            details=urawa_imdb_info[index]
            with cols[index]:
                mtitle = details['title']
                if len(mtitle) >= 35:
                    mtitle = mtitle[:35]+'...'
                st.write(f'**{mtitle}**')
                st.image(details['image'], width = 220)
                with st.expander("Details"):

                    st.write(f'[{details["year"]}, {details["runtimeMins"]} minutes, {details["contentRating"]}]')
                    st.write('')
                    st.write(f'Director: {details["directors"]}')
                    st.write(f'Starring: {details["stars"]}')
                    st.write(f'Writers: {details["writers"]}')
                    st.write('')
                    st.write(f'IMDb: {details["imDbRating"]} | MetaScore: {details["metacriticRating"]} | LetterBoxd: x')
                    st.write('')
                    st.write(f'{details["genres"]} | {details["companies"]}')
                with st.expander("Plot"):
                    st.write(f'[{details["plot"]}]')

    if rows >=2:
        for index in range(4,8):
            details=urawa_imdb_info[index]
            with cols[index-4]:
                mtitle = details['title']
                if len(mtitle) >= 35:
                    mtitle = mtitle[:35]+'...'
                st.write(f'**{mtitle}**')
                st.image(details['image'], width = 220)
                with st.expander("Details"):

                    st.write(f'[{details["year"]}, {details["runtimeMins"]} minutes, {details["contentRating"]}]')
                    st.write('')
                    st.write(f'Director: {details["directors"]}')
                    st.write(f'Starring: {details["stars"]}')
                    st.write(f'Writers: {details["writers"]}')
                    st.write('')
                    st.write(f'IMDb: {details["imDbRating"]} | MetaScore: {details["metacriticRating"]} | LetterBoxd: x')
                    st.write('')
                    st.write(f'{details["genres"]} | {details["companies"]}')
                with st.expander("Plot"):
                    st.write(f'[{details["plot"]}]')

    if rows >=3:
        for index in range(8,12):
            details=urawa_imdb_info[index]
            with cols[index-8]:
                mtitle = details['title']
                if len(mtitle) >= 35:
                    mtitle = mtitle[:35]+'...'
                st.write(f'**{mtitle}**')
                st.image(details['image'], width = 220)
                with st.expander("Details"):
                    st.write(f'[{details["year"]}, {details["runtimeMins"]} minutes, {details["contentRating"]}]')
                    st.write('')
                    st.write(f'Director: {details["directors"]}')
                    st.write(f'Starring: {details["stars"]}')
                    st.write(f'Writers: {details["writers"]}')
                    st.write('')
                    st.write(f'IMDb: {details["imDbRating"]} | MetaScore: {details["metacriticRating"]} | LetterBoxd: x')
                    st.write('')
                    st.write(f'{details["genres"]} | {details["companies"]}')
                with st.expander("Plot"):
                    st.write(f'[{details["plot"]}]')

    if rem > 0:
        for index, col in zip(range(rows*4,rows*4+rem),[0,1,2,3]):
            details=urawa_imdb_info[index]
            with cols[col]:
                mtitle = details['title']
                if len(mtitle) >= 35:
                    mtitle = mtitle[:35]+'...'
                st.write(f'**{mtitle}**')
                st.image(details['image'], width = 220)
                with st.expander("Details"):

                    st.write(f'[{details["year"]}, {details["runtimeMins"]} minutes, {details["contentRating"]}]')
                    st.write('')
                    st.write(f'Director: {details["directors"]}')
                    st.write(f'Starring: {details["stars"]}')
                    st.write(f'Writers: {details["writers"]}')
                    st.write('')
                    st.write(f'IMDb: {details["imDbRating"]} | MetaScore: {details["metacriticRating"]} | LetterBoxd: x')
                    st.write('')
                    st.write(f'{details["genres"]} | {details["companies"]}')
                with st.expander("Plot"):
                    st.write(f'[{details["plot"]}]')

    showtimes = urawa_sts
    dfdict ={day['day'] +', '+ day['date']:df for day,df in zip(showtimes, urawa_dfs)}

    with st.expander("See times"):
        col=st.columns([1,5])
        with col[0]:
            showday = st.radio('Select a date', options=dfdict.keys(), key='urawaradio')
        with col[1]:
            for i in range(0,len(dfdict)):
                st.write('')
            abc=st.empty()
        st.dataframe(dfdict[showday])
        abc.subheader(f'Looking at : {showday}')


if 'Toho Cinema Fujimi' in cinemas:
    st.header('📽️Toho Cinema Fujimi')


    length=len(toho_imdb_info) #movies will be displayed in rows of 4
    rows=length//4
    rem=length%4
    cols = st.columns([1,1,1,1])
    if rows >=1:
        for index in range(0,4):
            details=toho_imdb_info[index]
            with cols[index]:
                mtitle = details['title']
                if len(mtitle) >= 35:
                    mtitle = mtitle[:35]+'...'
                st.write(f'**{mtitle}**')
                st.image(details['image'], width = 220)
                with st.expander("Details"):

                    st.write(f'[{details["year"]}, {details["runtimeMins"]} minutes, {details["contentRating"]}]')
                    st.write('')
                    st.write(f'Director: {details["directors"]}')
                    st.write(f'Starring: {details["stars"]}')
                    st.write(f'Writers: {details["writers"]}')
                    st.write('')
                    st.write(f'IMDb: {details["imDbRating"]} | MetaScore: {details["metacriticRating"]} | LetterBoxd: x')
                    st.write('')
                    st.write(f'{details["genres"]} | {details["companies"]}')
                with st.expander("Plot"):
                    st.write(f'[{details["plot"]}]')

    if rows >=2:
        for index in range(4,8):
            details=toho_imdb_info[index]
            with cols[index-4]:
                mtitle = details['title']
                if len(mtitle) >= 35:
                    mtitle = mtitle[:35]+'...'
                st.write(f'**{mtitle}**')
                st.image(details['image'], width = 220)
                with st.expander("Details"):

                    st.write(f'[{details["year"]}, {details["runtimeMins"]} minutes, {details["contentRating"]}]')
                    st.write('')
                    st.write(f'Director: {details["directors"]}')
                    st.write(f'Starring: {details["stars"]}')
                    st.write(f'Writers: {details["writers"]}')
                    st.write('')
                    st.write(f'IMDb: {details["imDbRating"]} | MetaScore: {details["metacriticRating"]} | LetterBoxd: x')
                    st.write('')
                    st.write(f'{details["genres"]} | {details["companies"]}')
                with st.expander("Plot"):
                    st.write(f'[{details["plot"]}]')

    if rows >=3:
        for index in range(8,12):
            details=toho_imdb_info[index]
            with cols[index-8]:
                mtitle = details['title']
                if len(mtitle) >= 35:
                    mtitle = mtitle[:35]+'...'
                st.write(f'**{mtitle}**')
                st.image(details['image'], width = 220)
                with st.expander("Details"):
                    st.write(f'[{details["year"]}, {details["runtimeMins"]} minutes, {details["contentRating"]}]')
                    st.write('')
                    st.write(f'Director: {details["directors"]}')
                    st.write(f'Starring: {details["stars"]}')
                    st.write(f'Writers: {details["writers"]}')
                    st.write('')
                    st.write(f'IMDb: {details["imDbRating"]} | MetaScore: {details["metacriticRating"]} | LetterBoxd: x')
                    st.write('')
                    st.write(f'{details["genres"]} | {details["companies"]}')
                with st.expander("Plot"):
                    st.write(f'[{details["plot"]}]')

    if rem > 0:
        for index, col in zip(range(rows*4,rows*4+rem),[0,1,2,3]):
            details=toho_imdb_info[index]
            with cols[col]:
                mtitle = details['title']
                if len(mtitle) >= 35:
                    mtitle = mtitle[:35]+'...'
                st.write(f'**{mtitle}**')
                st.image(details['image'], width = 220)
                with st.expander("Details"):

                    st.write(f'[{details["year"]}, {details["runtimeMins"]} minutes, {details["contentRating"]}]')
                    st.write('')
                    st.write(f'Director: {details["directors"]}')
                    st.write(f'Starring: {details["stars"]}')
                    st.write(f'Writers: {details["writers"]}')
                    st.write('')
                    st.write(f'IMDb: {details["imDbRating"]} | MetaScore: {details["metacriticRating"]} | LetterBoxd: x')
                    st.write('')
                    st.write(f'{details["genres"]} | {details["companies"]}')
                with st.expander("Plot"):
                    st.write(f'[{details["plot"]}]')

    showtimes = toho_sts
    dfdict ={day['day'] +', '+ day['date']:df for day,df in zip(showtimes, toho_dfs)}

    with st.expander("See times"):
        col=st.columns([1,5])
        with col[0]:
            showday = st.radio('Select a date', options=dfdict.keys(), key='tohoradio')
        with col[1]:
            for i in range(0,len(dfdict)):
                st.write('')
            abc=st.empty()
        st.dataframe(dfdict[showday])
        abc.subheader(f'Looking at : {showday}')


if 'Meguro Cinema' in cinemas:

    st.header('📽️Meguro Cinema')

    length=len(meg_imdb_info) #movies will be displayed in rows of 4
    rows=length//4
    rem=length%4
    cols = st.columns([1,1,1,1])

    if rows >=1:
        for index in range(0,4):
            details=meg_imdb_info[index]
            with cols[index]:
                mtitle = details['title']
                if len(mtitle) >= 35:
                    mtitle = mtitle[:35]+'...'
                st.write(f'**{mtitle}**')
                st.image(details['image'], width = 220)
                with st.expander("Details"):

                    st.write(f'[{details["year"]}, {details["runtimeMins"]} minutes, {details["contentRating"]}]')
                    st.write('')
                    st.write(f'Director: {details["directors"]}')
                    st.write(f'Starring: {details["stars"]}')
                    st.write(f'Writers: {details["writers"]}')
                    st.write('')
                    st.write(f'IMDb: {details["imDbRating"]} | MetaScore: {details["metacriticRating"]} | LetterBoxd: x')
                    st.write('')
                    st.write(f'{details["genres"]} | {details["companies"]}')
                with st.expander("Plot"):
                    st.write(f'[{details["plot"]}]')

    if rows >=2:
        for index in range(4,8):
            details=meg_imdb_info[index]
            with cols[index-4]:
                mtitle = details['title']
                if len(mtitle) >= 35:
                    mtitle = mtitle[:35]+'...'
                st.write(f'**{mtitle}**')
                st.image(details['image'], width = 220)
                with st.expander("Details"):

                    st.write(f'[{details["year"]}, {details["runtimeMins"]} minutes, {details["contentRating"]}]')
                    st.write('')
                    st.write(f'Director: {details["directors"]}')
                    st.write(f'Starring: {details["stars"]}')
                    st.write(f'Writers: {details["writers"]}')
                    st.write('')
                    st.write(f'IMDb: {details["imDbRating"]} | MetaScore: {details["metacriticRating"]} | LetterBoxd: x')
                    st.write('')
                    st.write(f'{details["genres"]} | {details["companies"]}')
                with st.expander("Plot"):
                    st.write(f'[{details["plot"]}]')

    if rows >=3:
        for index in range(8,12):
            details=meg_imdb_info[index]
            with cols[index-8]:
                mtitle = details['title']
                if len(mtitle) >= 35:
                    mtitle = mtitle[:35]+'...'
                st.write(f'**{mtitle}**')
                st.image(details['image'], width = 220)
                with st.expander("Details"):
                    st.write(f'[{details["year"]}, {details["runtimeMins"]} minutes, {details["contentRating"]}]')
                    st.write('')
                    st.write(f'Director: {details["directors"]}')
                    st.write(f'Starring: {details["stars"]}')
                    st.write(f'Writers: {details["writers"]}')
                    st.write('')
                    st.write(f'IMDb: {details["imDbRating"]} | MetaScore: {details["metacriticRating"]} | LetterBoxd: x')
                    st.write('')
                    st.write(f'{details["genres"]} | {details["companies"]}')
                with st.expander("Plot"):
                    st.write(f'[{details["plot"]}]')

    if rem > 0:
        for index, col in zip(range(rows*4,rows*4+rem),[0,1,2,3]):
            details=meg_imdb_info[index]
            with cols[col]:
                mtitle = details['title']
                if len(mtitle) >= 35:
                    mtitle = mtitle[:35]+'...'
                st.write(f'**{mtitle}**')
                st.image(details['image'], width = 220)
                with st.expander("Details"):

                    st.write(f'[{details["year"]}, {details["runtimeMins"]} minutes, {details["contentRating"]}]')
                    st.write('')
                    st.write(f'Director: {details["directors"]}')
                    st.write(f'Starring: {details["stars"]}')
                    st.write(f'Writers: {details["writers"]}')
                    st.write('')
                    st.write(f'IMDb: {details["imDbRating"]} | MetaScore: {details["metacriticRating"]} | LetterBoxd: x')
                    st.write('')
                    st.write(f'{details["genres"]} | {details["companies"]}')
                with st.expander("Plot"):
                    st.write(f'[{details["plot"]}]')
    with st.expander("See times"):
        st.table(meg_df)

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
