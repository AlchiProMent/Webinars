'''
Вебинар от 24 января 2023 г.

Осуществить парсинг сайта ИНТЕРФАКС (блок САМОЕ ЧИТАЕМОЕ)
https://www.interfax.ru/

Получить: название статьи, URL, дату публикации, рубрику, сумму слов в тексте статьи
Создать: ASCII-файл, в котором каждая строка будет содержать информацию о статье в виде
разбтых символом | (вертикальная черта):
* заголовок
* дата в формате YY-MM-DD,HH:mm
* название рубрики
* количество слов в статье
* URL статьи

Аналих HTML-кода страниц сайта Интерфакса:
САМО ЧИТАЕМОЕ: <div class="rcMR">
ссылка на статью: <a class="rcMR_nlink">

СТАТЬЯ (загруженная страница)
Заголовок: <h1>
Дата: <a CLASS="time">
Рубрика: <aside class="textML"><a>
Текст статьи (абзацы): <p>
'''

from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

START_URL = 'https://www.interfax.ru'


def code_month(month_name):
    # преобразование названия месяца в код (по первым буквам)
    if 'янв' in month_name:
        return '01'
    elif 'фев' in month_name:
        return '02'
    elif 'мар' in month_name:
        return '03'
    elif 'апр' in month_name:
        return '04'
    elif 'май' in month_name:
        return '05'
    elif 'июн' in month_name:
        return '06'
    elif 'июл' in month_name:
        return '07'
    elif 'авг' in month_name:
        return '08'
    elif 'сен' in month_name:
        return '09'
    elif 'окт' in month_name:
        return '10'
    elif 'ноя' in month_name:
        return '11'
    elif 'дек' in month_name:
        return '12'
    else:
        return 'XX'

def save_to_file(filen_name, lst: list, on_screen=True):
    # сохранить массив строк lst в файл filen_name
    with open(filen_name, 'w') as f:
        for s in lst:
            f.write(s + '\n')
            # выводить на экран при необходимости
            if on_screen:
                print(s)

def parse_interfax(url):
    # парсинг сайта
    html = str(urlopen(url).read(), 'Windows 1251')
    dom = BeautifulSoup(html, 'html.parser')
    # получить все ссылки на статьи в блоке "Самое читаемое"
    most_read_links = dom.find_all('a', class_='rcMR_nlink')

    # пустой список для накапливания строк для последующего сохранения в файл
    records = []
    for link in most_read_links:
        # URL текущей статьи
        curr_url = f'{url}{link.get("href")}'
        # избавиться от параметра utm_source
        url_lst = curr_url.split('?')
        # HTML-документ статьи
        art_html = str(urlopen(url_lst[0]).read(), 'Windows 1251')
        # DOM статьи
        article = BeautifulSoup(art_html, 'html.parser')

        # заголовок
        title = article.h1.text
        # рубрика
        rubrika = article.find(class_='textML').find('a').text

        # строка даты (убрать начальные и хвостовые пробелы при помощи strip)
        date_str = article.find('a', class_='time').text.strip()
        # разбить строку с датай вида 'HH:MM, DD xxxxxxxx YYYY' на пять групп
        m = re.search(r'(\d{2})[:](\d{2}), (\d{1,2}) (\S+) (\d{4})', date_str)
        # переформатировать дату в формат 'YY-MM-DD,HH:mm'
        fdate = f'{m.group(5)}-{code_month(m.group(4))}-{m.group(3)},{m.group(1)}:{m.group(2)}'

        # все абзацы текста статьи
        all_p = article.find_all('p')
        txt = ''
        # собрать все абзацы в единый текстовый блок
        for p in all_p:
            txt += p.text

        # разбить текстовый блок на отдельные слова
        words = re.findall(r'\S+', txt)

        # сгруппировать все полученные значения в единую строку и добавить в список
        records.append(f'{title}|{fdate}|{rubrika}|{len(words)}|{url_lst[0]}')

    # сохранить масссив строк в файл
    save_to_file('interfax.txt', records)


if __name__ == '__main__':
    print(f'Начался парсинг сайта "{START_URL}"...')
    parse_interfax(START_URL)
    input('Для завершения работы нажмите ENTER...')
