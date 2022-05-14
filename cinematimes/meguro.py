import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import imdb

def get_soup():
    '''
    html request to meguro cinema website to get soup
    '''
    url = 'http://www.okura-movie.co.jp/meguro_cinema/now_showing.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

def date_extract(soup):
    '''
    extracts date text from relevant html soup
    '''
    datespans = soup.find_all(class_='date')
    dates = [date.text.replace('.','/') for date in datespans]
    return dates

def movie_extract(soup):
    '''
    extracts movie text from relevant html soup
    '''
    engpattern = r'[\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\uff66-\uff9f]' #unicode for chinese/jp chars
    jppattern = r"タイトル☆-->(.*)<!--☆ここまで"

    engtitle = soup.find('span', class_='text_small').text.replace('\n','')
    engtitle = re.sub(engpattern,'', engtitle)

    jptitle = re.findall(jppattern, str(soup))[0].replace('\u3000', ' ')

    movie_dict = {'engtitle':engtitle, 'jptitle':jptitle}
    return(movie_dict)

def meguro_info(soup):
    '''
    from the soup, gets divs for date and movie info sequentially. then extracts just date and movies and returns ordered list of the info
    '''
    dateormovie = soup.find_all(id=['jyouei_kikan','sakuhin_detail']) #j_k is date info, s_d is movie detail

    meguro_info = [
    date_extract(dateormovie) if dateormovie.attrs['id'] == 'jyouei_kikan'
    else movie_extract(dateormovie)
    for dateormovie in dateormovie]

    return meguro_info

def meguro_eng_list(meg_info):
    '''
    return a list of only the english names
    '''
    return [title for movie in meg_info if type(movie) == dict for title in [movie['engtitle']] if title != '']

def meguro_imdb_search(meg_list):
    ''''
    takes a list of titles and returns titles and ids from moviesearch api
    '''
    resp = [imdb.moviesearch(title) for title in meg_list]
    cleanresp = [movie for movie in resp if movie != 'none']
    return cleanresp

def meguro_imdb_info(meg_imdb_search):
    '''
    takes the responses from the meguro_imdb_info returns all the details from details api
    '''
    info = [imdb.moviedetails(movie['id']) for movie in meg_imdb_search]
    for movie in info:
        movie['image']=movie['image'].replace('original', '384x528')
    return info

def meguro_info_df(meguro_info):
    ''''
    takes the meguro_info data from meguro_info function
    '''
    infodict={}

    m_info = meguro_info.copy()

    for item in m_info:
        if type(item) == list:
            key=item[0]+' - '+item[1]
            infodict[key] = []
        if type(item) == dict:
            value = item['engtitle']
            if value == '':
                value = 'japanese movie'
                infodict[key].insert(-1,value)
            else:
                infodict[key].insert(0,value)

    maxlength = max([len(movies) for movies in infodict.values()]) #padding to make lists same length for df
    for key in infodict.keys():
        while len(infodict[key]) < maxlength:
            infodict[key].append('-')

    return pd.DataFrame(infodict)

if __name__ == '__main__':

    soup = get_soup()
    print(meguro_info(soup))
