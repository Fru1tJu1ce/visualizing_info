import csv
import pygal.maps.world
from pygal.style import Style

from instruments import get_country_code as gcc


filename = 'forest_area.csv'
forest_dict = {}
forest_dict_1, forest_dict_2 = {}, {}
forest_dict_3, forest_dict_4 = {}, {}
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for row in reader:
        code = gcc(row[0])
        if code:
            try:
                value = int(float(row[-4]))
                forest_dict[code] = value
            except ValueError:
                print('Missing data for ' + str(row[0]))
        else:
            print("Данная страна не распознана: " + row[0])

for key, value in forest_dict.items():
    if value > 3000000:
        forest_dict_1[key] = value
    elif value > 300000:
        forest_dict_2[key] = value
    elif value > 50000:
        forest_dict_3[key] = value
    else:
        forest_dict_4[key] = value
    
# Настройка стиля.
wm_style = Style(
    background='#ffffff',  # Фоновый цвет вне графика
    plot_background='#ffffff',  # Цвета в табличке при наведении на страну
    foreground='#000000',  # Цвет текста из легенды для графика
    foreground_strong='#000000',  # Цвет текста названия графика
    foreground_subtle='#000000',  # Цвет обводки стран
    opacity='.6',  # Прозрачность меток в легенде
    opacity_hover='.4',  # Прозрачность меток при наведении курсора
    transition='400ms ease-in',  # Время анимации при наведении на страну
    colors=('#0e9600', '#d8db00', '#cc0000', '#0075e3'))

# Представление информации в графическом виде.
wm = pygal.maps.world.World(style=wm_style)
wm.title = ('Площадь лесной территории различных стран (кв. км.)' +
            '\n 2018 год')
wm.add('>3m', forest_dict_1)
wm.add('300k-3m', forest_dict_2)
wm.add('50k-300k', forest_dict_3)
wm.add('<50k', forest_dict_4)
wm.render_to_file('forest_area.svg')
