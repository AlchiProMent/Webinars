#################################################################################
# Учебная программа
# Парсинг страницы архива тиражей
# лотереи "Спортлото 7 из 49"
# Автор: Дмитрий Румянцев
# 2023 г.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from pandas import DataFrame
import re
import time

STOLOTO_ARCHIVE_URL = 'https://www.stoloto.ru/7x49/archive'
RUN_URL = 'https://www.stoloto.ru/7x49/archive/{}'
CSV_NAME = 'lotto7x49.csv'

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

def wait(drv, by=By.TAG_NAME, tout=5, val='div'):
    # подождать указанное время до появления объекта
    try:
        WebDriverWait(drv, timeout=tout).until(ec.visibility_of_element_located((by, val)))
    except:
        return False
    else:
        return True


def save2csv(csv_name, lst):
    # сохранить в CSV-файл

    print(f'Получено {len(lst)} результатов тиражей.')

    # списки для индекса DataFrames...
    indexes = []
    # ...и колонок
    col_0 = []
    col_1 = []
    col_2 = []
    col_3 = []
    col_4 = []
    col_5 = []
    col_6 = []

    # сформировать семь списков на основе исходных справочников
    print('Преобразование массива в форму для DataFrame...')
    for dct in lst:
        for key, el in dct.items():
            # добавить значение в массив индексов
            indexes.append(key)
            # разбросать значения по спискам
            col_0.append(el[0])
            col_1.append(el[1])
            col_2.append(el[2])
            col_3.append(el[3])
            col_4.append(el[4])
            col_5.append(el[5])
            col_6.append(el[6])

    # сформировать DataFrame
    df = DataFrame({'A': col_0, 'B': col_1, 'C': col_2, 'D': col_3, 'E': col_4, 'F': col_5, 'G': col_6},
                   index=indexes)

    try:
        # сохранить в файл (файл будет перезаписан)
        df.to_csv(csv_name)
    except:
        print(f'Ошибка при попытке сохранения файла "{csv_name}"')
    else:
        print(f'Данные успешно сохранены в файле "{csv_name}"')


def clicked_on_button(drv, button, total):
    # цикл по числу заказанных кликов по кнопке
    for i in range(total):
        # прокрутить страиницу вниз
        drv.execute_script("window.scrollTo(0,document.body.clientHeight);")
        # ожидать
        time.sleep(5)
        try:
            button.click()
        except:
            print(f'Не получается кликнуть: {i}')
        else:
            print(f'{i}-й click...')
            time.sleep(5)


def go_parsing(arch_url, total_clicked=1):
    # начать парсинг

    # список для результатов тиражей
    all_runs = []

    # создать объект для настройки опций
    options = Options()
    # установить стратегию загрузки
    options.page_load_strategy = 'normal'
    # opts.headless = True

    # создать драйвер
    print('Старт браузера Chrome...')
    driver = webdriver.Chrome(options=options)

    print('Загрузка страницы...')
    # загрузить страницу
    driver.get(arch_url)

    if wait(driver, By.XPATH, tout=5, val='//div[@class="more"]/span[@class="pseudo"]'):

        if total_clicked > 0:
            print('Начало кликанья по кнопке...')
            # получить кнопку "Показать ещё"
            press_box = driver.find_element(by=By.XPATH, value='//div[@class="more"]/span[@class="pseudo"]')
            # несколько кликов по кнопке
            clicked_on_button(driver, press_box, total_clicked)

        print('Начало парсинга страницы...')
        # собрать результаты всех загруженных тиражей (не делается проверка на действительное наличие элементов)
        div_class_mains = driver.find_elements(by=By.CSS_SELECTOR, value='div.main')
        for div_class_main in div_class_mains:
            # блок с номером тиража
            num_run = div_class_main.find_element(by=By.CLASS_NAME, value='draw').text
            # все результаты тиражей
            numbers_txt = div_class_main.find_element(by=By.CSS_SELECTOR, value='span.zone').text
            # получить результаты тиражей
            numbers = re.findall(r'\d{2}', numbers_txt)
            # добавить очередной тираж в виде справочника #Тиража: [значения]
            all_runs.append({num_run: numbers})
        print('Парсинг закончен. Массив значений сформирован.')

    driver.close()
    return all_runs


if __name__ == '__main__':
    runs_dict = go_parsing(STOLOTO_ARCHIVE_URL, 5)
    # сохранить в CSV
    save2csv(CSV_NAME, runs_dict)
    print('Программа закончила работу.')
