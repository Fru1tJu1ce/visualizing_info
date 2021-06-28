import pygal

from random_walk import RandomWalk

 
# Построение случайного блуждания и нанесение точек на диаграмму.
rw = RandomWalk(10000)
rw.fill_walk()
points = []

print("Calculating...")
for value in range(rw.num_points):
    points.append((rw.x_values[value], rw.y_values[value]))
    
xy_chart = pygal.XY(stroke=False, show_y_labels=False, 
                    show_x_labels=False, dots_size=1)
xy_chart.title = ("Случайные блуждания из " + str(rw.num_points) +
                  " точек.")
 
xy_chart.add('Случайные блуждания', points)
xy_chart.add('Начальная точка', [points[0]])
xy_chart.add('Конечная точка', [points[-1]])
xy_chart.render_to_file('rw_visual.svg')

print("Done!")

