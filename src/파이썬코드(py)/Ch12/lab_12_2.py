import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
path = "C:/Users/jangs/OneDrive/Documents/GitHub/DataSciPy/data/csv/"

weather = pd.read_csv(path + 'weather.csv', encoding='CP949')
monthly = [ None for x in range(12) ]    
monthly_wind = [ 0 for x in range(12) ]  

weather['month'] = pd.DatetimeIndex(weather['일시']).month

for i in range(12) :
    monthly[i] = weather[ weather['month'] == i + 1 ]
    monthly_wind[i] = monthly[i].mean()['평균풍속']       

plt.plot(monthly_wind, 'red')
plt.show()