import requests
from bs4 import BeautifulSoup

"""
Сайты, на основе которых будет скрипт:
    https://tproger.ru
    https://habr.com
    https://xakep.ru
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
    article_name = article_name.rstrip('\n')

    req = requests.get(url=article_href, headers=headers)
    src = req.text
