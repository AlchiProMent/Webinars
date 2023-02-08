######################################################
# анализ результатов тиражей
#
#
import pandas as pd
import numpy as np

CSV_NAME = 'lotto7x49.csv'

def go_analyse(scv_file_name):
    print('Начало анализа данных...')
    df = pd.read_csv(scv_file_name, index_col=0)
    print(f'Получен массив размерностью {df.shape}')
    print(df.info())
    print()

    # преобразовать в ndarray
    data = np.array(df.values)

    print('\nСумма по столбцам:')
    cols_sum = data.sum(axis=0)
    for ind, m in enumerate(cols_sum):
        print(f'{chr(ind+65):>2}: {m}')

    print('\nСреднее по столбцам:')
    cols_mean = data.mean(axis=0)
    for ind, m in enumerate(cols_mean):
        print(f'{chr(ind+65):>2}: {m}')

    print('\nСтандартное отклонение:')
    cols_std = data.std(axis=0)
    for ind, m in enumerate(cols_std):
        print(f'{chr(ind+65):>2}: {m}')

    print('\nДисперсия:')
    cols_var = data.var(axis=0)
    for ind, m in enumerate(cols_var):
        print(f'{chr(ind+65):>2}: {m}')

    print('\nМинимум:')
    cols_min = data.min(axis=0)
    for ind, m in enumerate(cols_min):
        print(f'{chr(ind+65):>2}: {m}')

    print('\nМаксимум:')
    cols_max = data.max(axis=0)
    for ind, m in enumerate(cols_max):
        print(f'{chr(ind+65):>2}: {m}')

    print('\nСводная статистика:')
    print(df.describe(include='all'))

    print('\nВсего появлений каждого номера:')
    total_in_a = df['A'].value_counts()
    total_in_b = df['B'].value_counts()
    total_in_c = df['C'].value_counts()
    total_in_d = df['D'].value_counts()
    total_in_e = df['E'].value_counts()
    total_in_f = df['F'].value_counts()
    total_in_g = df['G'].value_counts()

    # собрать статистики вместе
    total_nums = total_in_a + total_in_b + total_in_c + total_in_d + total_in_e + total_in_f + total_in_g
    # отсортировать по убыванию
    sorted_total_nums = total_nums.sort_values(ascending=False)
    print(sorted_total_nums)

if __name__ == '__main__':
    go_analyse(CSV_NAME)