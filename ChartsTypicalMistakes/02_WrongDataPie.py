# Ошибочные данные в пеодписях к диаграмме
import matplotlib.pyplot as plt
import numpy as np

# подготовить данные
data = [69, 15, 45, 29, 44]
fruit = ['Слива: 45%', 'Дыня: 8%', 'Яблоко: 20%', 'Арбуз: 15%', 'Смородина: 22%']
# создать фигуру и axes
fg, ax = plt.subplots()

# ax.pie(data, labels=fruit, autopct='%.2f%%', explode=[0, 0, 0, 0.2, 0])
ax.pie(data,
       labels=fruit,
       labeldistance=.5,
       rotatelabels=True,
       explode=[0, 0, 0, 0.2, 0],
       wedgeprops={'linewidth': 1, 'edgecolor': 'white'},
       counterclock=False)

ax.set_title('Структура плодов, представленных в продаже',
             fontdict=dict({'fontsize': 18,
                            'fontweight': 'bold',
                            'color': 'tab:blue'}))

wm = plt.get_current_fig_manager()
wm.window.state('zoomed')
plt.show()

