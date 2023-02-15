import pandas as pd
from pandas import DataFrame
import numpy as np

CSV_NAME = 'lotto7x49.csv'

def calc_intervals(dframe, elem_num):
    df = dframe.copy()
    df[df != elem_num] = 0
    elem_df = df['A'] + df['B'] + df['C'] + df['D'] + df['E'] + df['F']
    not_nul_elem = elem_df[elem_df != 0]
    count = []
    ind = not_nul_elem.index
    for i, ind_curr in enumerate(ind):
        if i < len(ind)-1:
            count.append(ind[i] - ind[i+1])
    return count


def go_calc_stat(file_name):
    print('Начало анализа данных...')
    try:
        df = pd.read_csv(file_name, index_col=0)
    except:
        print('Ошибка')
    else:
        stat = []
        print('Начало расчета')
        for num in range(1, 50):
            totals = calc_intervals(df, num)
            # создать массив
            tot_arr = np.array(totals)
            # добавить статистику для очередного элемента
            stat.append((num, tot_arr.min(), tot_arr.max(), tot_arr.mean(), tot_arr.std(), tot_arr.var()))

        # вывести таблицу статистик
        for st in stat:
            print(st)




if __name__ == '__main__':
    go_calc_stat(CSV_NAME)