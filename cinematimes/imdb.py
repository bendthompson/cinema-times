import requests

def moviesearch(query):
    '''
    takes a query and returns {id,resulttype,image,title,description} for the first result from imdb search
    '''
    url = 'https://imdb-api.com/en/API/SearchMovie/k_iw50ohm9/'
    response = requests.get(url+query)
    if response.status_code == 200:
        resultlist = response.json()['results']
        if len(resultlist) != 0:
            firstresult = resultlist[0]
            return firstresult
        else:
            return 'none'
    else:
        return 'none'

def moviedetails(movieid):
    '''
    takes id, calls details api, returns a dict of many details
    '''
    url = 'https://imdb-api.com/en/API/Title/k_iw50ohm9/'
    response = requests.get(url + movieid)
    print(f"Response :{response.status_code}")
    moviedetails = response.json()
    return moviedetails

def resizeimage(imagelink, size='384x528'):
    '''
    takes the image link which is sometimesbig and returns a ink to a resized version
    '''
    url = imagelink.replace('original', '384x528')
    return url

def poster(movieid):
    '''
    from id returns first poster image which is sometimes different to search image
    '''
    url = 'https://imdb-api.com/en/API/Posters/k_iw50ohm9/'
    response = requests.get(url+movieid).json()
    firstposter = response['posters'][0]
    link = firstposter['link']
    return link

def search_list(titlelist):
    '''
    takes a list of titles, searches for them at the imdb api and returns responses
    '''
    resp = [moviesearch(title) for title in titlelist]
    cleanresp = [movie for movie in resp if movie != 'none']
    return cleanresp

def info_list(imdb_search_list):
    '''
    takes a list of imdb ids and returns details about them from imdb api
    '''
    info = [moviedetails(movie['id']) for movie in imdb_search_list]
    for movie in info:
        movie['image']=movie['image'].replace('original', '384x528')
    return info
