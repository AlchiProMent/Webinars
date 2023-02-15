# сравнение количественного показателя по нескольким видам
import matplotlib.pyplot as plt
from pandas import DataFrame
import numpy as np

df = DataFrame({'Январь': [8, 2, 4],
                'Февраль': [12, 3, 10],
                'Март': [10, 9, 14],
                'Апрель': [15, 7, 12]},
               index=['Грузовики', 'Автокраны', 'Бульдозеры'])

y = np.arange(len(df.columns))

def view_charts():
    # создать фигуры для четырех графиков
    fg, ax = plt.subplots(1, 2)
    fg.suptitle('Объёмы продаж по видам продукции по периодам', fontsize=20, fontweight='bold')
    # отсутпы графиков
    fg.tight_layout(w_pad=3)

    ax[0].plot(df.T, 'o-')
    ax[0].legend(labels=df.index)
    ax[0].grid(axis='x', color='#dddddd', linestyle='dashed')

    width = 0.25
    x = np.arange(len(df.columns))
    rects0 = ax[1].bar(x, df.iloc[0], width, label=df.index[0])
    rects1 = ax[1].bar(x + width, df.iloc[1], width, label=df.index[1])
    rects2 = ax[1].bar(x + width*2, df.iloc[2], width, label=df.index[2])
    ax[1].set_ylabel('Объем выпуска (шт)', fontsize=10, color='tab:grey')
    ax[1].legend(labels=df.index)
    ax[1].grid(axis='y', color='#dddddd', linestyle='dashed')

    # установить подписи по X
    ax[1].set_xticks(x + (width*1.5), df.columns)
    # убрать фаски
    ax[1].tick_params(bottom=False)

    ax[1].bar_label(rects0, padding=-16)
    ax[1].bar_label(rects1, padding=-16)
    ax[1].bar_label(rects2, padding=-16)


    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    plt.show()


if __name__ == '__main__':
    view_charts()
