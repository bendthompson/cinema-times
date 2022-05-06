import requests
from bs4 import BeautifulSoup

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
    engtitle = soup.find('span', class_='text_small').text
    jptitle = re.findall(pattern, str(soup))[0].replace('\u3000', ' ')
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
