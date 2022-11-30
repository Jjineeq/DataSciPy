import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

path = "C:/Users/jangs/OneDrive/Documents/GitHub/DataSciPy/data/csv/"

weather = pd.read_csv(path + 'weather.csv', encoding='CP949')

weather['month'] = pd.DatetimeIndex(weather['일시']).month
means = weather.groupby('month').mean()
means['평균풍속'].plot(kind = 'bar')

plt.show()