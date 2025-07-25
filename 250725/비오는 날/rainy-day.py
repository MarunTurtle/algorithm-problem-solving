n = int(input())

class Forecast:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

forecasts = []

for _ in range(n):
    date, day, weather = tuple(input().split())
    forecast = Forecast(date, day, weather)
    forecasts.append(forecast)

forecasts.sort(key=lambda x:x.date)

for i in range(n):
    if forecasts[i].weather == "Rain":
        print(f'{forecasts[i].date} {forecasts[i].day} {forecasts[i].weather}')
        break
