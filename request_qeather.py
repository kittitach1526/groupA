import requests
import json
from datetime import datetime, timedelta

today = datetime.now() + timedelta(days=0, hours=0)
dt_string = today.strftime("%Y-%m-%d %H:00:00").split()
endPoint = {
    'province': '',
    'amphoe': '',
    'date': dt_string[0],
    'time': dt_string[1]}


class weather:
    temp=0
    hum =0
    #url=f"https://data.tmd.go.th/nwpapi/v1/forecast/area/place?domain=2&province=ปทุมธานี&amphoe=คลองหลวง&fields=tc,rh&starttime={endPoint['date']}T{endPoint['time']}"
    #changeLocation= f"https://data.tmd.go.th/nwpapi/v1/forecast/area/place?domain=2&province={endPoint['province']}&amphoe={endPoint['amphoe']}&fields=tc,rh&starttime={endPoint['date']}T{endPoint['time']}"
    token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImVmYmZjMjUwN2FjZjdiYjBmYTJjM2FiNTlkMTA0NzQ0OTlhNDJiZmZhZjlkYzc2OGY5NDM3M2M4MmUxY2FhZTRjYjYyZjU1Y2VlNzQ2OWY0In0.eyJhdWQiOiIyIiwianRpIjoiZWZiZmMyNTA3YWNmN2JiMGZhMmMzYWI1OWQxMDQ3NDQ5OWE0MmJmZmFmOWRjNzY4Zjk0MzczYzgyZTFjYWFlNGNiNjJmNTVjZWU3NDY5ZjQiLCJpYXQiOjE2NzUyNDk3MzksIm5iZiI6MTY3NTI0OTczOSwiZXhwIjoxNzA2Nzg1NzM5LCJzdWIiOiIyMzk5Iiwic2NvcGVzIjpbXX0.a5MlC5MnGD3gdTOmrfDD457LyEQgOL-G_pKbV-XF2nfDL-TAR7ipkiMd22XMiOvxa5zuQKsvDzD4q4l3CNHgAsztSo4PBn8EdaAMuwlZLlwvta5DwM2hcOWwWzW9O4C6lNKHhWAhiT5eKb6NVApPd57SLJSgLrAmJe6ftvRIOr0TG9Q363yPF9zsoXCLpm0D7ygtONuh2AGwHNs1yB5XpCuGYVRwY9RcKSOD9nJJjUgTIjhFZwg3o7_DaTlByweFZT6FwVr-TOmCBLmtjf2hft7Y3wTGZzQHQJKT_jt9fKLujISxYbrO7OQdcBC5IVapMfcKN6FX-Celdgo9tEyWcCP2dNQ45r07RQBcVrZAhWpLO3XyDrpfpc5nvVVVHiBYWt-E89jwFSUYJJXHqABhw_KouUgQtxfUW_hov_t0p0cICieY2DUBpWhJeWxnFJPk4k4xCmyUH_kYmpYzJV9phJwKl0wj6pd8jP6WlNbr97QzVI5xJwpQAW7EaWZWp-Q6I8su-6na0uxCnYMBrE8PUhxoLp8rWJDxq0X0pGLSmn_t_SDcJ2ev_8yPWW65yXThD4yKP-xsSxLgHeMfgpt9N4XjkLnViofmWXI6flu4mqa0ZYrzbuYvm8OFJhHI7vRtWloF5sl5Qb8h1F5H-79w-706nHjkkUFRiaB75Ff5i4w'
    headers={'accept': 'application/json','authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImVmYmZjMjUwN2FjZjdiYjBmYTJjM2FiNTlkMTA0NzQ0OTlhNDJiZmZhZjlkYzc2OGY5NDM3M2M4MmUxY2FhZTRjYjYyZjU1Y2VlNzQ2OWY0In0.eyJhdWQiOiIyIiwianRpIjoiZWZiZmMyNTA3YWNmN2JiMGZhMmMzYWI1OWQxMDQ3NDQ5OWE0MmJmZmFmOWRjNzY4Zjk0MzczYzgyZTFjYWFlNGNiNjJmNTVjZWU3NDY5ZjQiLCJpYXQiOjE2NzUyNDk3MzksIm5iZiI6MTY3NTI0OTczOSwiZXhwIjoxNzA2Nzg1NzM5LCJzdWIiOiIyMzk5Iiwic2NvcGVzIjpbXX0.a5MlC5MnGD3gdTOmrfDD457LyEQgOL-G_pKbV-XF2nfDL-TAR7ipkiMd22XMiOvxa5zuQKsvDzD4q4l3CNHgAsztSo4PBn8EdaAMuwlZLlwvta5DwM2hcOWwWzW9O4C6lNKHhWAhiT5eKb6NVApPd57SLJSgLrAmJe6ftvRIOr0TG9Q363yPF9zsoXCLpm0D7ygtONuh2AGwHNs1yB5XpCuGYVRwY9RcKSOD9nJJjUgTIjhFZwg3o7_DaTlByweFZT6FwVr-TOmCBLmtjf2hft7Y3wTGZzQHQJKT_jt9fKLujISxYbrO7OQdcBC5IVapMfcKN6FX-Celdgo9tEyWcCP2dNQ45r07RQBcVrZAhWpLO3XyDrpfpc5nvVVVHiBYWt-E89jwFSUYJJXHqABhw_KouUgQtxfUW_hov_t0p0cICieY2DUBpWhJeWxnFJPk4k4xCmyUH_kYmpYzJV9phJwKl0wj6pd8jP6WlNbr97QzVI5xJwpQAW7EaWZWp-Q6I8su-6na0uxCnYMBrE8PUhxoLp8rWJDxq0X0pGLSmn_t_SDcJ2ev_8yPWW65yXThD4yKP-xsSxLgHeMfgpt9N4XjkLnViofmWXI6flu4mqa0ZYrzbuYvm8OFJhHI7vRtWloF5sl5Qb8h1F5H-79w-706nHjkkUFRiaB75Ff5i4w'}
    url=f"https://data.tmd.go.th/nwpapi/v1/forecast/area/place?domain=2&province=ปทุมธานี&amphoe=คลองหลวง&fields=tc,rh&starttime=2023-02-01T23:00:00"
    def __init__(self) -> None:
        pass

    def get_temp():
        r = requests.get(weather.url,headers=weather.headers)
        data= json.loads(r.text)
        # print('this --> json', data)
        data_weather = data['WeatherForecasts']
        data_weather = data_weather[2]
        data_keydata = str(data_weather)
        data_keydata = data_keydata.split(",")
        temp = data_keydata[3].split(" ")
        temp = str(temp[3])
        return temp

print(weather.temp)