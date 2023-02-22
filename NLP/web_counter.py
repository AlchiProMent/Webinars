# подсчёт количества имён на веб ресурсах
from bs4 import BeautifulSoup
from urllib.request import urlopen
import spacy
from pandas import DataFrame
from os import path
from spacy.vocab import Vocab
from spacy.tokens import Doc
import plotly.express as px

LENTA_RU = 'https://lenta.ru/'
INTERFAX = 'https://www.interfax.ru/'

DOC_FILE_NAME = 'ru_web_23_02_21.dfw'
GRAPH_FILE = 'graph.html'

TOTAL_COL = 'Всего'
ORG_COL = 'Организации'
LOC_COL = 'Локации'

def get_text_from_url(file_url):
    # получить текст страницы сплошным потоком (без разбивки на элементы)
    try:
        html = urlopen(file_url)
        dom = BeautifulSoup(html, 'html.parser')
    except:
        return ''
    else:
        return dom.text

def calc_names(doc):
    # собрать все имена, локации и организации в тексте и справочнике частот
    names = {}
    locals = {}
    orgs = {}

    # пройтись по именованным сущностям (Entity)
    for ent in doc.ents:
        # для каждой группы сформировать собственный словарь частот
        match ent.label_:
            case 'PER':
                if ent.lemma_ in names:
                    names[ent.lemma_] += 1
                else:
                    names[ent.lemma_] = 1
            case 'LOC':
                if ent.lemma_ in names:
                    locals[ent.lemma_] += 1
                else:
                    locals[ent.lemma_] = 1
            case 'ORG':
                if ent.lemma_ in names:
                    orgs[ent.lemma_] += 1
                else:
                    orgs[ent.lemma_] = 1

    # создать три массива
    df_names = DataFrame({TOTAL_COL: names})
    df_locals = DataFrame({LOC_COL: locals})
    df_orgs = DataFrame({ORG_COL: orgs})
    # отсортировать по значению
    df_names.sort_values(by=TOTAL_COL, inplace=True, ascending=False)
    df_locals.sort_values(by=LOC_COL, inplace=True, ascending=False)
    df_orgs.sort_values(by=ORG_COL, inplace=True, ascending=False)
    return [df_names, df_locals, df_orgs]

def show_bar(df, col_name, html_name=GRAPH_FILE):
    # создать график
    fig = px.bar(df, x=df.index, y=col_name, color=df.index)
    fig.write_html(html_name)

if __name__ == '__main__':
    print('Загрузка из сети началась...')
    text = get_text_from_url(LENTA_RU)
    print('Данные загружены')

    change_doc = False
    if path.isfile(DOC_FILE_NAME):
        # загрузить с диска
        print('Чтение ранее сохранённых данных')
        doc = Doc(Vocab()).from_disk(DOC_FILE_NAME)
    else:
        print('Создание новой модели...')
        nlp = spacy.load('ru_core_news_md')
        doc = nlp(text)
        print('Модель создана')
        change_doc = True

    # подсчитать количество встреченных имён
    dfs = calc_names(doc)
    # вывести результат
    for df in dfs:
        print()
        print(df)

    # вывести график частот
    show_bar(dfs[0], TOTAL_COL, 'names.html')

    # сохранить на диск
    if change_doc:
        doc.to_disk(DOC_FILE_NAME)
