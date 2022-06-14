import requests
from bs4 import BeautifulSoup

"""
Сайты, на основе которых будет скрипт:
    https://tproger.ru
"""
print('Этот скрипт работает на основе сайта https://tproger.ru')
print('Скрипт может парсить актуальные статьи с главной страницы, а также статьи по определенным тегам, например Python')
print('Чтобы парсить страницы по тегам это нужно указать в ссылке, например https://tproger.ru/tag/python/')

# Параметры для парсинга
url = str(input('Введите ссылку на сайт: '))
#TODO написать скрипт корректирующий длинну строки
N = int(input('Введите длину строки: '))
save_pics = str(input('Сохранить картинки в виде ссылок? y/n: '))
#TODO дописать скрипт по сохранению в файл
save_file = str(input('Сохранить информацию в файл? y/n: '))
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
    #article_name = article_name.rstrip('\n')
    # Берем за основу новую ссылку
    req = requests.get(url=article_href, headers=headers)
    src = req.text
    # Создаем новый объект супа
    soup = BeautifulSoup(src, 'lxml')
    # Собираем заголовок статьи, текст и удаляем футтер
    article_title = soup.find(class_='single__title').text
    article_text = soup.find(class_='single__content').text
    footer_to_delete = soup.find(class_='footer-meta').text
    article_text = article_text.replace(footer_to_delete, '')
    # Ищем ссылки на картинки
    article_code = soup.find(class_='single__content')
    image_block = article_code.find_all('a', class_='flex lightbox')
    # Помещаем ссылки на картинки в список
    image_href_list = []
    for img in image_block:
        image_href = img.get('href')
        image_href_list.append(image_href)
    # Выводим статьи и картинки
    print(f'СТАТЬЯ: {article_title}')
    print(f'ТЕКСТ СТАТЬИ: {article_text}')
    if save_pics == 'y':
        for image in image_href_list:
            print(f'Картинка: {image}')

    with open('result.txt', 'w', encoding='utf-8') as file:
        file.write(f'{article_title}\n{article_text}')
