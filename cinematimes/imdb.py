import requests

def moviesearch(query):
    '''
    takes a query and returns {id,resulttype,image,title,description} for the first result from imdb search
    '''
    url = 'https://imdb-api.com/en/API/SearchMovie/k_iw50ohm9/'
    response = requests.get(url+query).json()
    firstresult = response['results'][0]
    return firstresult

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
