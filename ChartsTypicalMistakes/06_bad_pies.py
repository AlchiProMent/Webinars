# неудкачное использование круговых диаграмм
import matplotlib.pyplot as plt
import numpy as np

# данные
titles = np.array(['Вся продукция', 'Основная'])
products = np.array([[12., 1.2],
                     [21., 1.8],
                     [10., 0.9],
                     [15., 2.],
                     [20., 2.9],
                     [25., 3.4]])


def view_charts():
    # создать фигуры для четырех графиков
    fg, ax = plt.subplots(2, 3)
    fg.suptitle('Динамика изменения структуры основной продукции в общем объеме производства за период 2017-2022 г.г.',
                fontsize=18, fontweight='bold')

    title_font_dict={'fontsize': 14,'fontweight': 'bold','color': 'tab:blue'}

    ax[0, 0].pie(products[0], labels=titles, autopct='%.2f%%', explode=[0, 0.2], counterclock=False)
    ax[0, 0].set_title('2017', fontdict=title_font_dict)

    ax[0, 1].pie(products[1], labels=titles, autopct='%.2f%%', explode=[0, 0.2], counterclock=False)
    ax[0, 1].set_title('2018', fontdict=title_font_dict)

    ax[0, 2].pie(products[2], labels=titles, autopct='%.2f%%', explode=[0, 0.2], counterclock=False)
    ax[0, 2].set_title('2018', fontdict=title_font_dict)

    ax[1, 0].pie(products[3], labels=titles, autopct='%.2f%%', explode=[0, 0.2], counterclock=False)
    ax[1, 0].set_title('2017', fontdict=title_font_dict)

    ax[1, 1].pie(products[4], labels=titles, autopct='%.2f%%', explode=[0, 0.2], counterclock=False)
    ax[1, 1].set_title('2018', fontdict=title_font_dict)

    ax[1, 2].pie(products[5], labels=titles, autopct='%.2f%%', explode=[0, 0.2], counterclock=False)
    ax[1, 2].set_title('2018', fontdict=title_font_dict)

    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    plt.show()


if __name__ == '__main__':
    view_charts()
