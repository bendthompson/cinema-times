import requests
import pandas as pd
import re

def search(query):
    '''
    takes cinema query and returns googles showtimes, a list of dictionaries for each day
    '''
    url = 'https://serpapi.com/search.json'
    params = {"q": query, "hl": "en","gl": "us",
              "api_key": "795f9ca654b1031eb177ec72c1b14382c12a781a6db5e4a739c719fb308e47c8"}

    response = requests.get(url, params=params)
    print(f"Response :{response.status_code}")
    showtimes = response.json()['showtimes']

    return showtimes

def start_end(showtimes):
    '''
    takes showtimes dictionary given by googlesearch and returns tuple of startday and endday
    '''
    startday = showtimes[0]['day'] + ' ' + showtimes[0]['date']
    endday   = showtimes[-1]['day'] + ' ' + showtimes[-1]['date']

    return (startday,endday)


def movies_by_day(showtimes):
    '''
    takes showtimes dict and returns a dictionary- keys are each day, values are lists of movie titles
    '''
    moviesbyday = {day['date'].split()[1] : [movie['name'] for movie in day['movies']] for day in showtimes }
    return moviesbyday

def movie_list(showtimes):
    '''
    goes through showtimes and returns a list of each unique movie
    '''
    movie_set = {movie['name'] for day in showtimes for movie in day['movies']}
    return list(movie_set)

def eng_movie_list(showtimes):
    '''
    goes through showtimes and returns a list of each unique eng movie
    '''
    pattern = r'[\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\uff66-\uff9f]'
    movie_set = {movie['name'] for day in showtimes for movie in day['movies'] if bool(re.search(pattern, movie['name'])) == False}
    return list(movie_set)

def eng_day_to_df(day):
    pattern = r'[\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\uff66-\uff9f]'
    daydict=[{'name':movie['name'],'times':movie['showing']} for movie in day['movies'] if bool(re.search(pattern, movie['name'])) == False]
    for movie in daydict:
        movie['Movie'] = movie.pop('name')
        for typedict in movie['times']:
            movie[typedict['type']] = typedict['time']
        movie.pop('times')
    daydf = pd.DataFrame(daydict)
    return daydf

def day_to_df(day):
    daydict=[{'name':movie['name'],'times':movie['showing']} for movie in day['movies']]
    for movie in daydict:
        movie['Movie'] = movie.pop('name')
        for typedict in movie['times']:
            movie[typedict['type']] = typedict['time'][0]
        movie.pop('times')
    daydf = pd.DataFrame(daydict).fillna('-')
    return daydf

def eng_daily_df_list(showtimes):
    return [eng_day_to_df(day) for day in showtimes]

def daily_df_list(showtimes):
    return [day_to_df(day) for day in showtimes]
