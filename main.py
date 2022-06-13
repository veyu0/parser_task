import re

import requests
from bs4 import BeautifulSoup

"""
Сайты, на основе которых будет скрипт:
    https://tproger.ru
"""
# Главная ссылка для парсинга
url = 'https://tproger.ru'
# Заголовки, чтобы сайт не принял нас за бота
headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1"
}
# Делает get запрос и записывает ответ в переменную
req = requests.get(url, headers=headers)
src = req.text
# Создаем парсер
soup = BeautifulSoup(src, 'lxml')
# Ищем все статьи через класс
all_articles_hrefs = soup.find_all(class_='article__link')
# Записывает название стать и её ссылку в словарь
all_articles_dict = {}
for item in all_articles_hrefs:
    item_text = item.text
    item_href = item.get('href')

    all_articles_dict[item_text] = item_href
# Парсинг информации внутри статей
for article_name, article_href in all_articles_dict.items():
    # article_name = article_name.rstrip('\n')

    req = requests.get(url=article_href, headers=headers)
    src = req.text

    soup = BeautifulSoup(src, 'lxml')

    article_title = soup.find(class_='single__title').text
    article_text = soup.find(class_='single__content').text
    footer_to_delete = soup.find(class_='footer-meta').text
    article_text = article_text.replace(footer_to_delete, '')

    article_code = soup.find(class_='single__content')
    image_block = article_code.find_all('a', class_='flex lightbox')

    article_img = {}
    for img in image_block:
        image_href = img.get('href')

    # print(f'СТАТЬЯ: {article_title}')
    # print(article_text)
    # print(f'Картинки из статьи {image_href}')
