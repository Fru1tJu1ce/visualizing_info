import csv
from matplotlib import pyplot as plt
from datetime import datetime


# Чтение максимальных, минимальных температур и даты из файла.
filename = 'formattedqm.csv'
with open(filename) as f:
    reader = csv.reader(f)
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        high = int(row[1])
        low = int(row[3])
        
        highs.append(high)
        lows.append(low)
        dates.append(current_date)
        
# Представление в графическом формате
fig, ax = plt.subplots(dpi=128, figsize=(10, 6))
ax.plot(dates, highs, c='red', label='highs', alpha=0.5)
ax.plot(dates, lows, c='blue', label='lows', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

# Форматирование
ax.set_title("Годовые изменения температуры\nСан Франциско 2021",
    fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Температура (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

# Сохранение фигуры в файле
plt.savefig('sf_temp.png')

plt.show()        


