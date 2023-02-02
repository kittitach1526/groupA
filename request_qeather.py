import requests
import json
from datetime import datetime, timedelta
import PySimpleGUI as sg

province = "ปทุมธานี"
amphore ="คลองหลวง"
    
class weather:
    temp=0
    hum =0
    today = datetime.now() + timedelta(days=0, hours=0)
    dt_string = today.strftime("%Y-%m-%d %H:00:00").split()
    endPoint = {
        'province': province,
        'amphoe': amphore,
        'date': dt_string[0],
        'time': dt_string[1]}
    url=f"https://data.tmd.go.th/nwpapi/v1/forecast/area/place?domain=2&province={endPoint['province']}&amphoe={endPoint['amphoe']}&fields=tc,rh&starttime={endPoint['date']}T{endPoint['time']}"
    #changeLocation= f"https://data.tmd.go.th/nwpapi/v1/forecast/area/place?domain=2&province={weather.endPoint['province']}&amphoe={endPoint['amphoe']}&fields=tc,rh&starttime={endPoint['date']}T{endPoint['time']}"
    token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImVmYmZjMjUwN2FjZjdiYjBmYTJjM2FiNTlkMTA0NzQ0OTlhNDJiZmZhZjlkYzc2OGY5NDM3M2M4MmUxY2FhZTRjYjYyZjU1Y2VlNzQ2OWY0In0.eyJhdWQiOiIyIiwianRpIjoiZWZiZmMyNTA3YWNmN2JiMGZhMmMzYWI1OWQxMDQ3NDQ5OWE0MmJmZmFmOWRjNzY4Zjk0MzczYzgyZTFjYWFlNGNiNjJmNTVjZWU3NDY5ZjQiLCJpYXQiOjE2NzUyNDk3MzksIm5iZiI6MTY3NTI0OTczOSwiZXhwIjoxNzA2Nzg1NzM5LCJzdWIiOiIyMzk5Iiwic2NvcGVzIjpbXX0.a5MlC5MnGD3gdTOmrfDD457LyEQgOL-G_pKbV-XF2nfDL-TAR7ipkiMd22XMiOvxa5zuQKsvDzD4q4l3CNHgAsztSo4PBn8EdaAMuwlZLlwvta5DwM2hcOWwWzW9O4C6lNKHhWAhiT5eKb6NVApPd57SLJSgLrAmJe6ftvRIOr0TG9Q363yPF9zsoXCLpm0D7ygtONuh2AGwHNs1yB5XpCuGYVRwY9RcKSOD9nJJjUgTIjhFZwg3o7_DaTlByweFZT6FwVr-TOmCBLmtjf2hft7Y3wTGZzQHQJKT_jt9fKLujISxYbrO7OQdcBC5IVapMfcKN6FX-Celdgo9tEyWcCP2dNQ45r07RQBcVrZAhWpLO3XyDrpfpc5nvVVVHiBYWt-E89jwFSUYJJXHqABhw_KouUgQtxfUW_hov_t0p0cICieY2DUBpWhJeWxnFJPk4k4xCmyUH_kYmpYzJV9phJwKl0wj6pd8jP6WlNbr97QzVI5xJwpQAW7EaWZWp-Q6I8su-6na0uxCnYMBrE8PUhxoLp8rWJDxq0X0pGLSmn_t_SDcJ2ev_8yPWW65yXThD4yKP-xsSxLgHeMfgpt9N4XjkLnViofmWXI6flu4mqa0ZYrzbuYvm8OFJhHI7vRtWloF5sl5Qb8h1F5H-79w-706nHjkkUFRiaB75Ff5i4w'
    headers={'accept': 'application/json','authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImVmYmZjMjUwN2FjZjdiYjBmYTJjM2FiNTlkMTA0NzQ0OTlhNDJiZmZhZjlkYzc2OGY5NDM3M2M4MmUxY2FhZTRjYjYyZjU1Y2VlNzQ2OWY0In0.eyJhdWQiOiIyIiwianRpIjoiZWZiZmMyNTA3YWNmN2JiMGZhMmMzYWI1OWQxMDQ3NDQ5OWE0MmJmZmFmOWRjNzY4Zjk0MzczYzgyZTFjYWFlNGNiNjJmNTVjZWU3NDY5ZjQiLCJpYXQiOjE2NzUyNDk3MzksIm5iZiI6MTY3NTI0OTczOSwiZXhwIjoxNzA2Nzg1NzM5LCJzdWIiOiIyMzk5Iiwic2NvcGVzIjpbXX0.a5MlC5MnGD3gdTOmrfDD457LyEQgOL-G_pKbV-XF2nfDL-TAR7ipkiMd22XMiOvxa5zuQKsvDzD4q4l3CNHgAsztSo4PBn8EdaAMuwlZLlwvta5DwM2hcOWwWzW9O4C6lNKHhWAhiT5eKb6NVApPd57SLJSgLrAmJe6ftvRIOr0TG9Q363yPF9zsoXCLpm0D7ygtONuh2AGwHNs1yB5XpCuGYVRwY9RcKSOD9nJJjUgTIjhFZwg3o7_DaTlByweFZT6FwVr-TOmCBLmtjf2hft7Y3wTGZzQHQJKT_jt9fKLujISxYbrO7OQdcBC5IVapMfcKN6FX-Celdgo9tEyWcCP2dNQ45r07RQBcVrZAhWpLO3XyDrpfpc5nvVVVHiBYWt-E89jwFSUYJJXHqABhw_KouUgQtxfUW_hov_t0p0cICieY2DUBpWhJeWxnFJPk4k4xCmyUH_kYmpYzJV9phJwKl0wj6pd8jP6WlNbr97QzVI5xJwpQAW7EaWZWp-Q6I8su-6na0uxCnYMBrE8PUhxoLp8rWJDxq0X0pGLSmn_t_SDcJ2ev_8yPWW65yXThD4yKP-xsSxLgHeMfgpt9N4XjkLnViofmWXI6flu4mqa0ZYrzbuYvm8OFJhHI7vRtWloF5sl5Qb8h1F5H-79w-706nHjkkUFRiaB75Ff5i4w'}
    def __init__(self) -> None:
        pass

    def get_temp():
        weather.get_date_time()
        r = requests.get(weather.url,headers=weather.headers)
        data= json.loads(r.text)
        # print('this --> json', data)
        data_weather = data['WeatherForecasts']
        data_weather = data_weather[2]
        data_keydata = str(data_weather)
        data_keydata = data_keydata.split(",")
        temp = data_keydata[3].split(" ")
        weather.temp = str(temp[3])
        return weather.temp

    def get_humidity():
        weather.get_date_time
        r = requests.get(weather.url,headers=weather.headers)
        data= json.loads(r.text)
        # print('this --> json', data)
        data_weather = data['WeatherForecasts']
        data_weather = data_weather[2]
        data_keydata = str(data_weather)
        data_keydata = data_keydata.split(",")
        hum = data_keydata[4].split(" ")
        #print(hum)
        hum = str(hum[2])
        hum= hum.split("}")
        weather.hum = str(hum[0])
        return weather.hum

    def get_date_time():
        weather.today = datetime.now() + timedelta(days=0, hours=0)
        weather.endPoint ={
            'province': '',
            'amphoe': '',
            'date': weather.dt_string[0],
            'time': weather.dt_string[1]}


        

#data = weather.get_temp()
#print(data)
#data = weather.get_humidity()
#print(data)
#--------------------------------------------------------------------------------------------------------------------------------------------------------
class gui(weather):
    sg.ChangeLookAndFeel('lightblue')
    BG_COLOR = "#FFC13F" #sg.theme_text_color()
    TXT_COLOR = "#000000" #sg.theme_background_color()
    ALPHA = 0.8
    timeout_minutes = 5 * (60 * 1000)
    
    APP_DATA = {
        'City': 'ปทุมธานี',
        'Country': 'TH',
        'Postal': None,
        'Description': 'clear skys',
        'Temp': 101.0,
        'Feels Like': 72.0,
        'Wind': 0.0,
        'Humidity': 0,
        'Precip 1hr': 0.0,
        'Pressure': 0,
        'Updated': 'Not yet updated',
        'Icon': None,
        'Units': 'Imperial'
    }
    def metric_row(metric):
        lbl = sg.Text(metric, font=('Arial', 10), pad=(15, 0), size=(9, 1))
        num = sg.Text(gui.APP_DATA[metric], font=('Arial', 10, 'bold'), pad=(0, 0), size=(9, 1), key=metric)
        return [lbl, num]

    def metric_row(metric):
        lbl = sg.Text(metric, font=('Arial', 10), pad=(15, 0), size=(9, 1))
        num = sg.Text(gui.APP_DATA[metric], font=('Arial', 10, 'bold'), pad=(0, 0), size=(9, 1), key=metric)
        return [lbl, num]

    def create_window():
        col1 = sg.Column(
            [[sg.Text(gui.APP_DATA['City'], font=('Arial Rounded MT Bold', 18), pad=((10, 0), (50, 0)), size=(18, 1), background_color=gui.BG_COLOR, text_color=gui.TXT_COLOR, key='City')],
            [sg.Text(gui.APP_DATA['Description'], font=('Arial', 12), pad=(10, 0), background_color=gui.BG_COLOR, text_color=gui.TXT_COLOR, key='Description')]],
                background_color=gui.BG_COLOR, key='COL1')
        col2 = sg.Column(
            [[sg.Text('×', font=('Arial Black', 16), pad=(0, 0), justification='right', background_color=gui.BG_COLOR, text_color=gui.TXT_COLOR, enable_events=True, key='-QUIT-')],
            [sg.Image(data=gui.APP_DATA['Icon'], pad=((5, 10), (0, 0)), size=(100, 100), background_color=gui.BG_COLOR, key='Icon')]],
                element_justification='center', background_color=gui.BG_COLOR, key='COL2')
        col3 = sg.Column(
            [[sg.Text(gui.APP_DATA['Updated'], font=('Arial', 8), background_color=gui.BG_COLOR, text_color=gui.TXT_COLOR, key='Updated')]],
                pad=(10, 5), element_justification='left', background_color=gui.BG_COLOR, key='COL3')
        col4 = sg.Column(
            [[sg.Text('click to change city', font=('Arial', 8, 'italic'), background_color=gui.BG_COLOR, text_color=gui.TXT_COLOR, enable_events=True, key='-CHANGE-')]],
                pad=(10, 5), element_justification='right', background_color=gui.BG_COLOR, key='COL4')
        top_col = sg.Column([[col1, col2]], pad=(0, 0), background_color=gui.BG_COLOR, key='TopCOL')
        bot_col = sg.Column([[col3, col4]], pad=(0, 0), background_color=gui.BG_COLOR, key='BotCOL')
        lf_col = sg.Column(
            [[sg.Text(gui.APP_DATA['Temp'], font=('Haettenschweiler', 90), pad=((10, 0), (0, 0)), justification='center', key='Temp')]],
                pad=(10, 0), element_justification='center', key='LfCOL')
        rt_col = sg.Column(
            [gui.metric_row('Temp'),gui.metric_row('Humidity')],#gui.metric_row('Feels Like'), gui.metric_row('Wind'), , gui.metric_row('Precip 1hr'), gui.metric_row('Pressure')
                pad=((15, 0), (25, 5)), key='RtCOL')
        layout = [[top_col], [lf_col, rt_col], [bot_col]]
        window = sg.Window(layout=layout, title='Weather Widget', size=(400, 315), margins=(0, 0), finalize=True, 
            element_justification='center', keep_on_top=True, no_titlebar=True, grab_anywhere=True, alpha_channel=gui.ALPHA)
        for col in ['COL1', 'COL2', 'TopCOL', 'BotCOL', '-QUIT-']:
            window[col].expand(expand_y=True, expand_x=True)
        for col in ['COL3', 'COL4', 'LfCOL', 'RtCOL']:
            window[col].expand(expand_x=True)
        return window

    def show_display():
        window = gui.create_window()
        while True:
            event, _ = window.read(timeout=gui.timeout_minutes)
            if event in (None, '-QUIT-'):
                break
    #if event == '-CHANGE-':
    #   change_city(window)
    # Update per refresh rate
    #request_weather_data(create_endpoint(2))
    #update_metrics(window)
        window.close()
#--------------------------------------------------------------------------------------------------------------------------------------------------------

gui.APP_DATA['Temp'] = weather.get_temp()
gui.show_display()


