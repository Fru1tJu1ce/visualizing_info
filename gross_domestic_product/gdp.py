import json
import pygal.maps.world

from instruments import get_country_code as gcc


# Загрузка данных в переменную.
filename = 'gdp_json.json'
with open(filename) as f_obj:
    data = json.load(f_obj)

# Словари для сортировки информации по значению ВВП
formatted_1, formatted_2, formatted_3, = {}, {}, {}

# Построение словарей из исходных данных.
for gdp_dict in data:
    if gdp_dict['Year'] == 2016:
        country_name = gdp_dict['Country Name']
        value = round(int(float(gdp_dict['Value'])) / 1000000)
        # Получение правильно отформатированного кода страны.
        code = gcc(country_name)
        
        if code:
            # Форматирование данных по значению ВВП.
            if value > 10000000:
                formatted_1[code] = value
            elif value > 1000000:
                formatted_2[code] = value
            else:
                formatted_3[code] = value
                
        # Вывод нераспознанных стран.
        else:
            print('Данная страна не распознана: ' + country_name)

# Представление данных в графическом виде.
wm = pygal.maps.world.World()
wm.title = 'ВВП стран в млн$ США'
wm.add('>10t', formatted_1)
wm.add('1t - 10t', formatted_2)
wm.add('<1t', formatted_3)
wm.render_to_file('gdp.svg')
