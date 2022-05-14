import streamlit as st
st.set_page_config(layout="wide")
import numpy as np
import pandas as pd
import imdb
import google
import meguro
st.session_state

if 'meguro_info' not in st.session_state:
    soup = meguro.get_soup()
    meg_info = meguro.meguro_info(soup)
    meg_list = meguro.meguro_eng_list(meg_info)
    meg_imdb_search = meguro.meguro_imdb_search(meg_list)
    meg_imdb_info = meguro.meguro_imdb_info(meg_imdb_search)
    meg_df = meguro.meguro_info_df(meg_info)
    st.session_state['meguro_info'] = meg_imdb_info
    st.session_state['meguro_df'] = meg_df

meg_imdb_info = st.session_state['meguro_info']
meg_df = st.session_state['meguro_df']

st.title("Some Cinema Times🎬")

cols = st.columns([1,6])

with cols[0]:
    st.write('')
    st.markdown('## **Cinemas**')
with cols[1]:
    cinemas = st.multiselect('', ['Meguro','Urawa'])


st.header('📽️Meguro Cinema')

length=len(meg_imdb_info)
rows=length//4
rem=length%4


cols = st.columns(np.full(4,1))
if 'Meguro' in cinemas:
    if rows >=1:
        for index in range(0,4):
            details=meg_imdb_info[index]
            with cols[index]:
                mtitle = details['title']
                if len(mtitle) >= 35:
                    mtitle = mtitle[:35]+'...'
                st.write(mtitle)
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
                st.write(mtitle)
                st.image(details['image'], width = 220)
                with st.expander("Details"):
                    details=moviedetails[index]
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
                st.write(mtitle)
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
                st.write(mtitle)
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
    df = pd.DataFrame(
        np.random.randn(10, 5),
        columns=('col %d' % i for i in range(5)))

    with st.expander("See times"):
        st.table(meg_df)

st.header('📽️Urawa United Cinema')

# imgs =
# titles =
# moviedetails =


if 'Urawa' in cinemas:
    st.text('urawa movies')
