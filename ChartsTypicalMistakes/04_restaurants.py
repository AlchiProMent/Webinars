# график о ресторанах, открывшихся в 2020 году
import matplotlib.pyplot as plt
import numpy as np

# данные
r_types = ['Русская', 'Здоровое питание', 'Европейская', 'Грузинская', 'Морепродукты', 'Гриль и мясо',
           'Итальянская', 'Азиатская', 'Авторская', 'Остальное (бар, караоке, кофейни)']
r_proc = [1., 1., 2.5, 3.5, 7., 8., 11., 13., 25., 28.]
colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(r_types)))

def view_charts():
    # создать фигуры для четырех графиков
    fg, ax = plt.subplots(1, 2)
    fg.suptitle('Доля ресторанов, открывшихся в 2020 году по типу кухни', fontsize=20, fontweight='bold')
    # отсутпы графиков
    fg.tight_layout(w_pad=3)

    # круговая диаграмма ################################################################################
    ax[0].pie(r_proc,
              labels=r_types,
              autopct='%.2f%%',
              colors=colors,
              rotatelabels=True,
              wedgeprops={'linewidth': 1, 'edgecolor': 'white'})

    # горизонтальная гистограмма
    y = np.arange(len(r_types))
    ax[1].barh(y, r_proc, color=colors, height=.98)
    ax[1].set_yticks(y, labels=r_types)
    ax[1].invert_yaxis()
    ax[1].tick_params(left=False)
    ax[1].set_xlabel('Доля в обзем объеме (%)', fontsize=10, color='tab:grey')

    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    plt.show()


if __name__ == '__main__':
    view_charts()
