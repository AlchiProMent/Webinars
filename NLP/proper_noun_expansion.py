# расширение базового словаря за счёт добавления сленговых имён собственных
# https://spacy.io/api/
import spacy
from os import path
from spacy.vocab import Vocab
from spacy.tokens import Doc
from pandas import DataFrame

DOC_NAME = 'doc.sdc'

txt = '''Однажды в студёную зимнюю пору Питер и Ольга захотели поехать в путешествие. 
Долго они выбирали куда поехать и решили побывать в Санкт-Петербурге. 
По пути они встретили Лену и Таню, которые хотели ехать в Ёбург, но решили присоединиться к Питеру и Ольге. 
В Питере друзья поселились в гостинице "Москва" с видом из окна на Неву. Но Лене больше нравился Владивосток.
И на следующий день она улетела ближайшим рейсом к Тихому океану.  
'''

change_doc = False
if path.isfile(DOC_NAME):
    # загрузить с диска
    doc = Doc(Vocab()).from_disk(DOC_NAME)

else:
    nlp = spacy.load('ru_core_news_md')
    doc = nlp(txt)
    change_doc = True

# ndarr = doc.to_array(['LEMMA', 'POS', 'DEP'])
# print(ndarr)
# print()

print('Предложения:')
for sent in doc.sents:
    print(sent)
print()

print('[ Токены ]')
print(f'     |{"Токены":<16}| {"Леммы":<15}| {"Тип":<10}| {"Head":<15}| {"Dep":<10}')
print('-' * 73)

more_marks = {}
for token in doc:
    if not token.pos_ in ['PUNCT', 'SPACE']:
        print(f'{"START" if token.is_sent_start else " END " if token.is_sent_end else "     "}'
              f'| {token.text:<15}'
              f'| {token.lemma_:<15}'
              f'| {token.pos_:<10}'
              f'| {token.head.text:<15}'
              f'| {token.dep_:<10}')

        # остальные значения поместить в дополнительный словарь
        more_marks[token.text] = {'lemma': token.lemma_, 'children': list(token.children),
                                  'lefts': list(token.lefts),
                                  'rights': list(token.rights),
                                  'ancestors': list(token.ancestors)}


print('\n[ Имена собственные ]')
print(f'{"Имена":<22}| {"Признаки":<12}| {"1л.ед.ч.им.":<12}')
print('-' * 46)
names = {}
# по именованным сущностям (Entity)
for ent in doc.ents:
    print(f'{ent.text:<22}| {ent.label_:<12}| {ent.lemma_:<12}')
    # подсчитывать количество только для людей (PERSON)
    if ent.label_ == 'PER':
        if ent.lemma_ in names:
            names[ent.lemma_] += 1
        else:
            names[ent.lemma_] = 1

print()
df = DataFrame({'Всего': names})
df.sort_values(by='Всего', inplace=True, ascending=False)
print(df)


print('\n\nЗависимости и связи токенов:')
# вывести дополнительные атрибуты
for key, dicts in more_marks.items():
    print('-'*50)
    # токен (символами в верхнем регистре)
    print(f'{key} ({dicts["lemma"]}):')

    if len(dicts['children']) > 0:
        print(f'\tПотомки: \t{dicts["children"]}')

    if len(dicts['lefts']) > 0:
        print(f'\tЛевые: \t{dicts["lefts"]}')

    if len(dicts['rights']) > 0:
        print(f'\tПравые: \t{dicts["rights"]}')

    if len(dicts['ancestors']) > 0:
        print(f'\tСвязанные: \t{dicts["ancestors"]}')

# сохранить на диск
if change_doc:
    doc.to_disk(DOC_NAME)
