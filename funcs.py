import requests
from bs4 import BeautifulSoup
import csv
from page import Page

HOST = 'https://habr.com'
URL = 'https://habr.com/ru/all/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/102.0.5005.115 Safari/537.36 OPR/88.0.4412.53', 'accept': '*/*'}
FILE = 'habr.csv'


def get_html(url1, params=None):
    request = requests.get(url1, headers=HEADERS, params=params)
    return request


def get_pages_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find_all('a', class_='tm-pagination__page')
    if pagination:
        return int(pagination[-1].get_text())
    else:
        return 1


def save_file(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['ASS'])
        for item in items:
            writer.writerow([item['title'], item['time'], item['number_of_votes'], item['comments'], item['bookmarks'],
                             item['habr_title_href'], item['URL author']])


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('article', class_='tm-articles-list__item')
    temp_obj = Page()
    habr = []

    for item in items:
        habr_title_href = item.find('a', class_='tm-article-snippet__title-link').get('http://href')
        if habr_title_href:
            habr_title_href = requests.get('href')
            print(habr_title_href.text)
        else:
            habr_title_href = '...'


        author_URL = HOST + item.find('a', class_='tm-user-info__username').get('href')
        temp = get_html(author_URL).text


        title = item.find('a', class_='tm-article-snippet__title-link').get_text()
        time =  item.find('span', class_='tm-article-snippet__datetime-published').get_text()
        number_of_votes = item.find('div', class_='tm-votes-meter').find_next('span').get_text().replace('<span class="tm-votes-meter__value tm-votes-meter__value tm-votes-meter__value_appearance-article tm-votes-meter__value_rating">', '')
        comments = item.find('span', class_='tm-article-comments-counter-link__value').get_text(strip=True).replace('\n', '')
        bookmarks = item.find('span', class_='bookmarks-button__counter').get_text(strip=True).replace('<span class="bookmarks-button__counter" title="Êîëè÷åñòâî ïîëüçîâàòåëåé, äîáàâèâøèõ ïóáëèêàöèþ â çàêëàäêè">','')
        authors_name = item.find('span', class_='tm-user-info__user').get_text(strip=True)
        habr_title_href = HOST + item.find('a', class_='tm-article-snippet__title-link').get('href')
        URL_author = HOST + item.find('a', class_='tm-user-info__username').get('href')
        author_rating = temp.find('span', class_='tm-user-info__username').get_text(strip=True).replace('\n', '')
        author_karma = temp.find('span', class_='tm-user-info__username').get_text(strip=True).replace('\n', '')

        habr.append(temp_obj.init_obj(title, time, number_of_votes, comments, bookmarks, authors_name, habr_title_href, URL_author, author_rating, author_karma))

    return habr


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        habr = []
        pages_count = get_pages_count(html.text)
        print(pages_count)
        for page in range(1, pages_count + 1):
            print(f'Page num {page} of {pages_count}...')
            html = get_html(URL, params={'page': page})
            habr.extend(get_content(html.text))
            print(habr)
            save_file(habr, FILE)
            # habr = get_content(html.text)
        print(habr)
    else:
        print('Error')
