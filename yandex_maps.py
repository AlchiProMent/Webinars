'''
Поиск на карте yandex.maps организаций в окрестности указанного адреса
вебинар от 25 января 2023 г.

Строка для ввода адреса:
<input class="input__control _bold">

Название организации:
<div class="class="search-business-snippet-view__title">
'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

YANDEX_MAP = 'https://maps.yandex.ru/'

def wait(drv, timeout=5, by=By.TAG_NAME, var='DIV'):
    # режим ожидания
    try:
        # ждать timeout секунд, пока не обнаружится указанный элемент
        WebDriverWait(drv, timeout=timeout).until(ec.visibility_of_element_located((by, var)))
    except:
        return False
    else:
        return True


def view_inside_orgs(drv, value):
    # вывести список организаций
    print('Объекты рядом:')
    print('-------------')
    # получить все элементы указанного класса
    orgs = drv.find_elements(by=By.CLASS_NAME, value=value)
    for org in orgs:
        # вывести текстовый атрибут
        print(org.text)
    print()


def yandex_maps(search_str):
    # загрузка карты и выполнение поиска

    options = Options()
    options.page_load_strategy = 'normal'
    # установить режим максимизации окна браузера
    options.add_argument('--start-maximized')
    # создать драйвер
    driver = webdriver.Chrome(options=options)
    # загрузить в драйвер страницу
    driver.get(YANDEX_MAP)

    # ждать появления элемента
    if wait(driver, 5, By.CLASS_NAME, 'input__control'):
        addr_box = driver.find_element(by=By.CLASS_NAME, value='input__control')
        # ввести адрес в строку
        addr_box.send_keys(search_str)
        # эмулировать нажатие ENTER
        addr_box.send_keys(Keys.RETURN)

        # дождаться загрузки элемента
        if wait(driver, 10, By.CLASS_NAME, 'search-business-snippet-view__title'):
            # вывести список названий
            view_inside_orgs(driver, 'search-business-snippet-view__title')
        else:
            print(f'По адресу "{search_str}" ничего не найдено')
    else:
        print('Отсутствует строка ввода!')

    driver.close()
    print()

if __name__ == '__main__':
    while (search_str := input('Введите адрес: ')):
        if search_str:
            # выполнить запрос
            yandex_maps(search_str)
