import requests

import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


url = ("https://api.github.com/search/repositories?q=language:c"
       "&sort=stars")

r = requests.get(url)
print("Status code: ",r.status_code)

response_dict = r.json()
repo_dicts = response_dict['items']
names, plot_dicts = [], []

for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    if repo_dict['description'] == None:
        repo_dict['description'] = 'Description is missing!'
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],
        'xlink': repo_dict['html_url'],
        }
    plot_dicts.append(plot_dict)

# Построение визуализации
my_style = LS('#333366', basestyle=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14 # Дополнительные метки (имена на Ох)
my_config.major_label_font_size = 18 # Метки по Оу, кратные 5000
my_config.truncate_label = 15 # Сокращение имён проектов до 15 символов.
my_config.show_y_guides = False # Скрытие горизонтальных линий
my_config.width = 1000
chart = pygal.Bar(my_config ,style=my_style)

chart.title = 'Most-Starred C Projects on GitHub'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('c_repos.svg')
