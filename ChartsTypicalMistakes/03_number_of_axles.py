# рассмотрение разных видов диаграмм для одного набора данных
import matplotlib.pyplot as plt
import numpy as np

# данные
years = np.array([2019, 2020, 2021, 2022])
total_sales = np.array([1_100_000, 1_200_000, 1_500_000, 1_300_000])
# последовательность цветов их палитры Blues
colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(total_sales)))


def view_charts():
    # создать фигуры для четырех графиков
    fg, ax = plt.subplots(2, 2)
    fg.suptitle('Объемы продаж модели по годам', fontsize=20, fontweight='bold')
    # отсутпы графиков
    fg.tight_layout(h_pad=2, w_pad=.1)

    # точечная диаграмма ###############################################################################
    ax[0, 0].scatter(years, total_sales, c=total_sales / 1_000_000, s=total_sales / 1000, alpha=0.5)
    ax[0, 0].set_xlabel('Годы', fontsize=10, color='tab:grey')
    ax[0, 0].set_ylabel('Вырчука (млн ед)', fontsize=10, color='tab:grey')
    ax[0, 0].set_title('Точечная диаграмма: нет понимания процесса')

    # линейная диаграмма ################################################################################
    ax[0, 1].plot(years, total_sales, 'o-')
    ax[0, 1].set_title('Линейный график: прослеживается тенденция')

    # круговая диаграмма ################################################################################
    ax[1, 0].pie(total_sales,
                 labels=years,
                 labeldistance=.5,
                 colors=colors,
                 rotatelabels=True,
                 wedgeprops={'linewidth': 1, 'edgecolor': 'white'})
    ax[1, 0].set_title('Круговая диаграмма: целые части чего?')

    # столбчатая диаграмма ##############################################################################
    width = .8
    x = np.arange(len(years))
    rects = ax[1, 1].bar(x, total_sales / 1_000_000, width, label='Франция')
    ax[1, 1].bar_label(rects, padding=-16, color='w')
    ax[1, 1].set_ylabel('Вырчука (млн ед)', fontsize=10, color='tab:grey')
    ax[1, 1].set_xticks(x, years)
    ax[1, 1].tick_params(bottom=False)
    ax[1, 1].set_title('Столбчатая диаграмма: сравнение данных по периодам')

    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    plt.show()


if __name__ == '__main__':
    view_charts()
