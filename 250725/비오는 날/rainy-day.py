n = int(input())

class Forecast:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

ans = Forecast("9999-99-99", "", "")

for _ in range(n):
    date, day, weather = tuple(input().split())
    
    forecast = Forecast(date, day, weather)
    
    if weather == "Rain":
        if ans.date >= forecast.date:
            ans = forecast

print(f'{ans.date} {ans.day} {ans.weather}')
