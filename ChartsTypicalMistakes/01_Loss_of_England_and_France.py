# график потерь Англии и Франции в войнаХ XVII-XX в.в.
#
import matplotlib.pyplot as plt
import numpy as np

def view_chart():

    # подготовка данных
    century = ['XVII в.', 'XVIII в.', 'XIX в.', 'XX в.']
    england = np.array([226, 314, 273, 807])
    france = np.array([673, 1783, 2522, 1427])
    x = np.arange(len(century))

    # ширина колонки
    width = 0.4

    # создать фигуру
    fg, ax = plt.subplots()

    # нарисовать столбцы
    rects1 = ax.bar(x, france, width, label='Франция')
    rects2 = ax.bar(x + width, england, width, label='Англия')

    # вывести значения на столбцы
    ax.bar_label(rects1, padding=-16, color='w')
    ax.bar_label(rects2, padding=-16)

    # дооформить график
    ax.set_title('Потери Англии и Франции в войнах')
    ax.set_xticks(x + width - (width/2), century)
    ax.set_ylabel('Потери (тыс.чел.)')
    ax.tick_params(bottom=False)
    ax.legend(loc='upper left', ncols=2, frameon=False)

    wm = plt.get_current_fig_manager()
    # развернуть с заголовком
    wm.window.state('zoomed')
    # развернуть без заголовка
    #wm.full_screen_toggle()

    # показать окно
    plt.show()

if __name__ == '__main__':
    view_chart()