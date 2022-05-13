import streamlit as st
st.set_page_config(layout="wide")
import numpy as np
import pandas as pd


st.title("Some Cinema Times🎬")

cinemas = st.multiselect('Cinemas', ['Meguro','Urawa'])


st.header('📽️Meguro Cinema')

length=6
rows=length//4
rem=length%4

imgs=[
    'https://imdb-api.com/images/384x528/MV5BZWMyYzFjYTYtNTRjYi00OGExLWE2YzgtOGRmYjAxZTU3NzBiXkEyXkFqcGdeQXVyMzQ0MzA0NTM@._V1_Ratio0.7273_AL_.jpg',
      'https://imdb-api.com/images/384x528/MV5BMWEwNjhkYzYtNjgzYy00YTY2LThjYWYtYzViMGJkZTI4Y2MyXkEyXkFqcGdeQXVyNTM0OTY1OQ@@._V1_Ratio0.7273_AL_.jpg',
      'https://imdb-api.com/images/384x528/MV5BZWMyYzFjYTYtNTRjYi00OGExLWE2YzgtOGRmYjAxZTU3NzBiXkEyXkFqcGdeQXVyMzQ0MzA0NTM@._V1_Ratio0.7273_AL_.jpg',
      'https://imdb-api.com/images/384x528/MV5BMWEwNjhkYzYtNjgzYy00YTY2LThjYWYtYzViMGJkZTI4Y2MyXkEyXkFqcGdeQXVyNTM0OTY1OQ@@._V1_Ratio0.7273_AL_.jpg',
      'https://imdb-api.com/images/384x528/MV5BZWMyYzFjYTYtNTRjYi00OGExLWE2YzgtOGRmYjAxZTU3NzBiXkEyXkFqcGdeQXVyMzQ0MzA0NTM@._V1_Ratio0.7273_AL_.jpg',
      'https://imdb-api.com/images/384x528/MV5BMWEwNjhkYzYtNjgzYy00YTY2LThjYWYtYzViMGJkZTI4Y2MyXkEyXkFqcGdeQXVyNTM0OTY1OQ@@._V1_Ratio0.7273_AL_.jpg']
titles = [
'Spider-Man: No Way Home',
'UnchartedUnchartedUnchartedUncharted',
'Spider-Man: Into the Spider-Verse',
'El Planeta',
'The Blues Brothers',
'Summer of Soul (...Or, When the Revolution Could Not Be Televised)',
'Belushi']
moviedetails = [
    {'title': 'Spider-Man: No Way Home',
 'year': '2021',
 'runtimeMins': '148',
 'runtimeStr': '2h 28min',
 'plot': "Peter Parker's secret identity is revealed to the entire world. Desperate for help, Peter turns to Doctor Strange to make the world forget that he is Spider-Man. The spell goes horribly wrong and shatters the multiverse, bringing in monstrous villains that could destroy the world.",
 'directors': 'Jon Watts',
 'writers': 'Chris McKenna, Erik Sommers, Stan Lee',
 'stars': 'Tom Holland, Zendaya, Benedict Cumberbatch',
 'genres': 'Action, Adventure, Fantasy',
 'companies': 'Columbia Pictures, Pascal Pictures, Marvel Studios',
 'contentRating': 'PG-13',
 'imDbRating': '8.4',
 'metacriticRating': '71'},{'title': 'Spider-Man: No Way Home',
 'year': '2021',
 'runtimeMins': '149',
 'runtimeStr': '2h 28min',
 'plot': "Peter Parker's secret identity is revealed to the entire world. Desperate for help, Peter turns to Doctor Strange to make the world forget that he is Spider-Man. The spell goes horribly wrong and shatters the multiverse, bringing in monstrous villains that could destroy the world.",
 'directors': 'Jon Watts',
 'writers': 'Chris McKenna, Erik Sommers, Stan Lee',
 'stars': 'Tom Holland, Zendaya, Benedict Cumberbatch',
 'genres': 'Action, Adventure, Fantasy',
 'companies': 'Columbia Pictures, Pascal Pictures, Marvel Studios',
 'contentRating': 'PG-13',
 'imDbRating': '8.4',
 'metacriticRating': '71'},{'title': 'Spider-Man: No Way Home',
 'year': '2021',
 'runtimeMins': '150',
 'runtimeStr': '2h 28min',
 'plot': "Peter Parker's secret identity is revealed to the entire world. Desperate for help, Peter turns to Doctor Strange to make the world forget that he is Spider-Man. The spell goes horribly wrong and shatters the multiverse, bringing in monstrous villains that could destroy the world.",
 'directors': 'Jon Watts',
 'writers': 'Chris McKenna, Erik Sommers, Stan Lee',
 'stars': 'Tom Holland, Zendaya, Benedict Cumberbatch',
 'genres': 'Action, Adventure, Fantasy',
 'companies': 'Columbia Pictures, Pascal Pictures, Marvel Studios',
 'contentRating': 'PG-13',
 'imDbRating': '8.4',
 'metacriticRating': '71'},{'title': 'Spider-Man: No Way Home',
 'year': '2021',
 'runtimeMins': '151',
 'runtimeStr': '2h 28min',
 'plot': "Peter Parker's secret identity is revealed to the entire world. Desperate for help, Peter turns to Doctor Strange to make the world forget that he is Spider-Man. The spell goes horribly wrong and shatters the multiverse, bringing in monstrous villains that could destroy the world.",
 'directors': 'Jon Watts',
 'writers': 'Chris McKenna, Erik Sommers, Stan Lee',
 'stars': 'Tom Holland, Zendaya, Benedict Cumberbatch',
 'genres': 'Action, Adventure, Fantasy',
 'companies': 'Columbia Pictures, Pascal Pictures, Marvel Studios',
 'contentRating': 'PG-13',
 'imDbRating': '8.4',
 'metacriticRating': '71'},{'title': 'Spider-Man: No Way Home',
 'year': '2021',
 'runtimeMins': '152',
 'runtimeStr': '2h 28min',
 'plot': "Peter Parker's secret identity is revealed to the entire world. Desperate for help, Peter turns to Doctor Strange to make the world forget that he is Spider-Man. The spell goes horribly wrong and shatters the multiverse, bringing in monstrous villains that could destroy the world.",
 'directors': 'Jon Watts',
 'writers': 'Chris McKenna, Erik Sommers, Stan Lee',
 'stars': 'Tom Holland, Zendaya, Benedict Cumberbatch',
 'genres': 'Action, Adventure, Fantasy',
 'companies': 'Columbia Pictures, Pascal Pictures, Marvel Studios',
 'contentRating': 'PG-13',
 'imDbRating': '8.4',
 'metacriticRating': '71'},{'title': 'Spider-Man: No Way Home',
 'year': '2021',
 'runtimeMins': '153',
 'runtimeStr': '2h 28min',
 'plot': "Peter Parker's secret identity is revealed to the entire world. Desperate for help, Peter turns to Doctor Strange to make the world forget that he is Spider-Man. The spell goes horribly wrong and shatters the multiverse, bringing in monstrous villains that could destroy the world.",
 'directors': 'Jon Watts',
 'writers': 'Chris McKenna, Erik Sommers, Stan Lee',
 'stars': 'Tom Holland, Zendaya, Benedict Cumberbatch',
 'genres': 'Action, Adventure, Fantasy',
 'companies': 'Columbia Pictures, Pascal Pictures, Marvel Studios',
 'contentRating': 'PG-13',
 'imDbRating': '8.4',
 'metacriticRating': '71'}]

cols = st.columns(np.full(4,1))
if 'Meguro' in cinemas:
    if rows >=1:
        for index in range(0,4):
            with cols[index]:
                mtitle = titles[index]
                if len(mtitle) >= 35:
                    mtitle = mtitle[:35]+'...'
                st.write(mtitle)
                st.image(imgs[index], width = 220)
                with st.expander("See details"):
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

    if rows >=2:
        for index in range(4,8):
            with cols[index-4]:
                mtitle = titles[index]
                if len(mtitle) >= 35:
                    mtitle = mtitle[:35]+'...'
                st.write(mtitle)
                st.image(imgs[index], width = 220)
                with st.expander("See details"):
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

    if rows >=3:
        for index in range(8,12):
            with cols[index-8]:
                mtitle = titles[index]
                if len(mtitle) >= 35:
                    mtitle = mtitle[:35]+'...'
                st.write(mtitle)
                st.image(imgs[index], width = 220)
                with st.expander("See details"):
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

    if rem > 0:
        for index, col in zip(range(rows*4,rows*4+rem),[0,1,2,3]):
            with cols[col]:
                mtitle = titles[index]
                if len(mtitle) >= 35:
                    mtitle = mtitle[:35]+'...'
                st.write(mtitle)
                st.image(imgs[index], width = 220)
                with st.expander("See details"):
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

    df = pd.DataFrame(
        np.random.randn(10, 5),
        columns=('col %d' % i for i in range(5)))

    with st.expander("See times"):
        st.table(df)

st.header('📽️Urawa Cinema')
if 'Urawa' in cinemas:
    st.text('urawa movies')
