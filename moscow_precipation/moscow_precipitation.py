import csv
import matplotlib.pyplot as plt
from datetime import datetime


filename = 'moscow_precipitation.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates = []
    quantities = []
    temp_day = []
    temp_night = []
    for row in reader:
        date_time = datetime.strptime(row[0], "%Y-%m-%d")
        quantity = float(row[1])
        day_t = int(row[2])
        night_t = int(row[3])
        
        dates.append(date_time)
        quantities.append(quantity)
        temp_day.append(day_t)
        temp_night.append(night_t)
        
        

# Создание графиков
fig, (ax1, ax2) = plt.subplots(1, 2, dpi=128, figsize=(10, 7))
ax1.bar(dates, quantities)
ax2.plot(dates, temp_day, c='red', label='Днём')
ax2.plot(dates, temp_night, c='blue', label='Ночью')
plt.fill_between(dates, temp_day, temp_night, facecolor='yellow', alpha=0.2)

# Форматирование первого графика
ax1.set_title("Осадки", fontsize=18)
ax1.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax1.set_ylabel("Количество осадков, мм", fontsize=16)
ax1.tick_params(axis='both', which='major', labelsize=16)
fig.suptitle("Погода в Москве: Апрель - Май 2021", fontsize=24)

# Форматирование второго графика
ax2.set_title("Температура", fontsize=18)
ax2.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax2.set_ylabel("Температура, °C", fontsize=16)
ax2.tick_params(axis='both', which='major', labelsize=16)
ax2.legend()

plt.show()
