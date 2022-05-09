import requests

def google_search(query):
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
    movie_set = {movie['name'] for movie in day['movies'] for day in showtimes}
    return list(movie_set)
