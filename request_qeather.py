import requests
import json
from datetime import datetime, timedelta

#===========================Token=====================================
tokenFam = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImQwZDVmNDhiNDgzZjI1MWE1YjM5Mzk0YmNmOWQ2ZmEwMGEyN2QwYzM2Y2RkYWE0YTMxMTNmOTllZmZlNTRiYzBiYTkzZjQ5NWU5OTM0NjlkIn0.eyJhdWQiOiIyIiwianRpIjoiZDBkNWY0OGI0ODNmMjUxYTViMzkzOTRiY2Y5ZDZmYTAwYTI3ZDBjMzZjZGRhYTRhMzExM2Y5OWVmZmU1NGJjMGJhOTNmNDk1ZTk5MzQ2OWQiLCJpYXQiOjE2NzUzMDQ5MzksIm5iZiI6MTY3NTMwNDkzOSwiZXhwIjoxNzA2ODQwOTM5LCJzdWIiOiIyNDAwIiwic2NvcGVzIjpbXX0.OehTWreoqkyKggq1_vzsmYAwQZO-gq2fZrCQ6ZzL6CVClAPrdjq7TH4Xyp1pnDG6V0wSNva8H_SntSCcTAgSufCHFRgj4Zh8bG3a33ooClh2iYoEl9z4BPLXvZgmVKCI6oKmjIOyKQL1NT6H1b3BpI6YsAy7WwxdO8QSNftRXJHIvOsehkEiiLplpg3zYg2_ZhY-_0o9d372ZPxqYoDlprsfFkvz_tLzSkBab-tYUDj7sBE0Wuor9fnEWO3cF3Qc5WYO5faA-5BBbQsk63gH2ANAsKuPOC5RM1o-LceW6CpZTMfL6YtTurbqOTK5RLHqfXbKXL3YqdW3_jq5JxgHWCHle3DAAaYWW2p1GXd2rWqmjgrTugcjHZrPFJ7ku1z4FZj6wQBbhG2hBAC-TSx6LrfrJdVhkj3U0axvsS2vPjnGxQ_Qp1gaQsPxe6MeM5Va9Lv-FRre9CZy20Ebm6ehfao2HI0-y2IN8Q5t5vjA2YH3cq35QLnqVw7Jc4Fs0c_e6wQCHWkX5Sa3IPwoe-fND68PyB58qHXjC5JAhmmcOkv5k2PcfX3lbHCYEUcI0BLCjky-qLoNDM3nPbqmoSlaH6S7t_BWRvKxO0wNUUEzI6UdgX7sFnG-0BVcokcGQxT__3pCYWReo7ZmZaiY7UQZJegt-eG1bhHx-n7l1AAKHsI'
tokenBest = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImVmYmZjMjUwN2FjZjdiYjBmYTJjM2FiNTlkMTA0NzQ0OTlhNDJiZmZhZjlkYzc2OGY5NDM3M2M4MmUxY2FhZTRjYjYyZjU1Y2VlNzQ2OWY0In0.eyJhdWQiOiIyIiwianRpIjoiZWZiZmMyNTA3YWNmN2JiMGZhMmMzYWI1OWQxMDQ3NDQ5OWE0MmJmZmFmOWRjNzY4Zjk0MzczYzgyZTFjYWFlNGNiNjJmNTVjZWU3NDY5ZjQiLCJpYXQiOjE2NzUyNDk3MzksIm5iZiI6MTY3NTI0OTczOSwiZXhwIjoxNzA2Nzg1NzM5LCJzdWIiOiIyMzk5Iiwic2NvcGVzIjpbXX0.a5MlC5MnGD3gdTOmrfDD457LyEQgOL-G_pKbV-XF2nfDL-TAR7ipkiMd22XMiOvxa5zuQKsvDzD4q4l3CNHgAsztSo4PBn8EdaAMuwlZLlwvta5DwM2hcOWwWzW9O4C6lNKHhWAhiT5eKb6NVApPd57SLJSgLrAmJe6ftvRIOr0TG9Q363yPF9zsoXCLpm0D7ygtONuh2AGwHNs1yB5XpCuGYVRwY9RcKSOD9nJJjUgTIjhFZwg3o7_DaTlByweFZT6FwVr-TOmCBLmtjf2hft7Y3wTGZzQHQJKT_jt9fKLujISxYbrO7OQdcBC5IVapMfcKN6FX-Celdgo9tEyWcCP2dNQ45r07RQBcVrZAhWpLO3XyDrpfpc5nvVVVHiBYWt-E89jwFSUYJJXHqABhw_KouUgQtxfUW_hov_t0p0cICieY2DUBpWhJeWxnFJPk4k4xCmyUH_kYmpYzJV9phJwKl0wj6pd8jP6WlNbr97QzVI5xJwpQAW7EaWZWp-Q6I8su-6na0uxCnYMBrE8PUhxoLp8rWJDxq0X0pGLSmn_t_SDcJ2ev_8yPWW65yXThD4yKP-xsSxLgHeMfgpt9N4XjkLnViofmWXI6flu4mqa0ZYrzbuYvm8OFJhHI7vRtWloF5sl5Qb8h1F5H-79w-706nHjkkUFRiaB75Ff5i4w'
#================================================================

today = datetime.now() + timedelta(days=0, hours=0)
dt_string = today.strftime("%Y-%m-%d %H:00:00").split()
endPoint = {
    'province': '',
    'amphoe': '',
    'date': dt_string[0],
    'time': dt_string[1]
}
# print('today', dt_string)
url=f"https://data.tmd.go.th/nwpapi/v1/forecast/area/place?domain=2&province=ปทุมธานี&amphoe=คลองหลวง&fields=tc,rh&starttime={endPoint['date']}T{endPoint['time']}"
changeLocation= f"https://data.tmd.go.th/nwpapi/v1/forecast/area/place?domain=2&province={endPoint['province']}&amphoe={endPoint['amphoe']}&fields=tc,rh&starttime={endPoint['date']}T{endPoint['time']}"
token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImVmYmZjMjUwN2FjZjdiYjBmYTJjM2FiNTlkMTA0NzQ0OTlhNDJiZmZhZjlkYzc2OGY5NDM3M2M4MmUxY2FhZTRjYjYyZjU1Y2VlNzQ2OWY0In0.eyJhdWQiOiIyIiwianRpIjoiZWZiZmMyNTA3YWNmN2JiMGZhMmMzYWI1OWQxMDQ3NDQ5OWE0MmJmZmFmOWRjNzY4Zjk0MzczYzgyZTFjYWFlNGNiNjJmNTVjZWU3NDY5ZjQiLCJpYXQiOjE2NzUyNDk3MzksIm5iZiI6MTY3NTI0OTczOSwiZXhwIjoxNzA2Nzg1NzM5LCJzdWIiOiIyMzk5Iiwic2NvcGVzIjpbXX0.a5MlC5MnGD3gdTOmrfDD457LyEQgOL-G_pKbV-XF2nfDL-TAR7ipkiMd22XMiOvxa5zuQKsvDzD4q4l3CNHgAsztSo4PBn8EdaAMuwlZLlwvta5DwM2hcOWwWzW9O4C6lNKHhWAhiT5eKb6NVApPd57SLJSgLrAmJe6ftvRIOr0TG9Q363yPF9zsoXCLpm0D7ygtONuh2AGwHNs1yB5XpCuGYVRwY9RcKSOD9nJJjUgTIjhFZwg3o7_DaTlByweFZT6FwVr-TOmCBLmtjf2hft7Y3wTGZzQHQJKT_jt9fKLujISxYbrO7OQdcBC5IVapMfcKN6FX-Celdgo9tEyWcCP2dNQ45r07RQBcVrZAhWpLO3XyDrpfpc5nvVVVHiBYWt-E89jwFSUYJJXHqABhw_KouUgQtxfUW_hov_t0p0cICieY2DUBpWhJeWxnFJPk4k4xCmyUH_kYmpYzJV9phJwKl0wj6pd8jP6WlNbr97QzVI5xJwpQAW7EaWZWp-Q6I8su-6na0uxCnYMBrE8PUhxoLp8rWJDxq0X0pGLSmn_t_SDcJ2ev_8yPWW65yXThD4yKP-xsSxLgHeMfgpt9N4XjkLnViofmWXI6flu4mqa0ZYrzbuYvm8OFJhHI7vRtWloF5sl5Qb8h1F5H-79w-706nHjkkUFRiaB75Ff5i4w'
headers={'accept': 'application/json','authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImVmYmZjMjUwN2FjZjdiYjBmYTJjM2FiNTlkMTA0NzQ0OTlhNDJiZmZhZjlkYzc2OGY5NDM3M2M4MmUxY2FhZTRjYjYyZjU1Y2VlNzQ2OWY0In0.eyJhdWQiOiIyIiwianRpIjoiZWZiZmMyNTA3YWNmN2JiMGZhMmMzYWI1OWQxMDQ3NDQ5OWE0MmJmZmFmOWRjNzY4Zjk0MzczYzgyZTFjYWFlNGNiNjJmNTVjZWU3NDY5ZjQiLCJpYXQiOjE2NzUyNDk3MzksIm5iZiI6MTY3NTI0OTczOSwiZXhwIjoxNzA2Nzg1NzM5LCJzdWIiOiIyMzk5Iiwic2NvcGVzIjpbXX0.a5MlC5MnGD3gdTOmrfDD457LyEQgOL-G_pKbV-XF2nfDL-TAR7ipkiMd22XMiOvxa5zuQKsvDzD4q4l3CNHgAsztSo4PBn8EdaAMuwlZLlwvta5DwM2hcOWwWzW9O4C6lNKHhWAhiT5eKb6NVApPd57SLJSgLrAmJe6ftvRIOr0TG9Q363yPF9zsoXCLpm0D7ygtONuh2AGwHNs1yB5XpCuGYVRwY9RcKSOD9nJJjUgTIjhFZwg3o7_DaTlByweFZT6FwVr-TOmCBLmtjf2hft7Y3wTGZzQHQJKT_jt9fKLujISxYbrO7OQdcBC5IVapMfcKN6FX-Celdgo9tEyWcCP2dNQ45r07RQBcVrZAhWpLO3XyDrpfpc5nvVVVHiBYWt-E89jwFSUYJJXHqABhw_KouUgQtxfUW_hov_t0p0cICieY2DUBpWhJeWxnFJPk4k4xCmyUH_kYmpYzJV9phJwKl0wj6pd8jP6WlNbr97QzVI5xJwpQAW7EaWZWp-Q6I8su-6na0uxCnYMBrE8PUhxoLp8rWJDxq0X0pGLSmn_t_SDcJ2ev_8yPWW65yXThD4yKP-xsSxLgHeMfgpt9N4XjkLnViofmWXI6flu4mqa0ZYrzbuYvm8OFJhHI7vRtWloF5sl5Qb8h1F5H-79w-706nHjkkUFRiaB75Ff5i4w'}
#headers2={'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImVmYmZjMjUwN2FjZjdiYjBmYTJjM2FiNTlkMTA0NzQ0OTlhNDJiZmZhZjlkYzc2OGY5NDM3M2M4MmUxY2FhZTRjYjYyZjU1Y2VlNzQ2OWY0In0.eyJhdWQiOiIyIiwianRpIjoiZWZiZmMyNTA3YWNmN2JiMGZhMmMzYWI1OWQxMDQ3NDQ5OWE0MmJmZmFmOWRjNzY4Zjk0MzczYzgyZTFjYWFlNGNiNjJmNTVjZWU3NDY5ZjQiLCJpYXQiOjE2NzUyNDk3MzksIm5iZiI6MTY3NTI0OTczOSwiZXhwIjoxNzA2Nzg1NzM5LCJzdWIiOiIyMzk5Iiwic2NvcGVzIjpbXX0.a5MlC5MnGD3gdTOmrfDD457LyEQgOL-G_pKbV-XF2nfDL-TAR7ipkiMd22XMiOvxa5zuQKsvDzD4q4l3CNHgAsztSo4PBn8EdaAMuwlZLlwvta5DwM2hcOWwWzW9O4C6lNKHhWAhiT5eKb6NVApPd57SLJSgLrAmJe6ftvRIOr0TG9Q363yPF9zsoXCLpm0D7ygtONuh2AGwHNs1yB5XpCuGYVRwY9RcKSOD9nJJjUgTIjhFZwg3o7_DaTlByweFZT6FwVr-TOmCBLmtjf2hft7Y3wTGZzQHQJKT_jt9fKLujISxYbrO7OQdcBC5IVapMfcKN6FX-Celdgo9tEyWcCP2dNQ45r07RQBcVrZAhWpLO3XyDrpfpc5nvVVVHiBYWt-E89jwFSUYJJXHqABhw_KouUgQtxfUW_hov_t0p0cICieY2DUBpWhJeWxnFJPk4k4xCmyUH_kYmpYzJV9phJwKl0wj6pd8jP6WlNbr97QzVI5xJwpQAW7EaWZWp-Q6I8su-6na0uxCnYMBrE8PUhxoLp8rWJDxq0X0pGLSmn_t_SDcJ2ev_8yPWW65yXThD4yKP-xsSxLgHeMfgpt9N4XjkLnViofmWXI6flu4mqa0ZYrzbuYvm8OFJhHI7vRtWloF5sl5Qb8h1F5H-79w-706nHjkkUFRiaB75Ff5i4w'}
r = requests.get(url,headers=headers)
data= json.loads(r.text)
# print('this --> json', data)
data_weather = data['WeatherForecasts']
data_weather = data_weather[2]
data_keydata = str(data_weather)
data_keydata = data_keydata.split(",")
temp = data_keydata[3].split(" ")
temp = str(temp[3])
# print(data_keydata[3]+" /////"+data_keydata[4])
# print(data_keydata[3])
# print(temp)


class weather :

    def __init__(self,link_url,token):
        self.link_url = link_url
        self.token = token
    


