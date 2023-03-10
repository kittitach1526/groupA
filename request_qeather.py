import requests
import json
from datetime import datetime, timedelta
import PySimpleGUI as sg

province = "ปทุมธานี"
amphore = "คลองหลวง"
dataChange = {
    'prov': None,
    'temp': None,
    'Humidity': None,
    'amphoe': None,
}


class weather:
    temp = 0
    hum = 0
    today = datetime.now() + timedelta(days=0, hours=0)
    dt_string = today.strftime("%Y-%m-%d %H:00:00").split()
    endPoint = {
        'province': province,
        'amphoe': amphore,
        'date': dt_string[0],
        'time': dt_string[1]}
    url = f"https://data.tmd.go.th/nwpapi/v1/forecast/area/place?domain=2&province={endPoint['province']}&amphoe={endPoint['amphoe']}&fields=tc,rh&starttime={endPoint['date']}T{endPoint['time']}"
    token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImVmYmZjMjUwN2FjZjdiYjBmYTJjM2FiNTlkMTA0NzQ0OTlhNDJiZmZhZjlkYzc2OGY5NDM3M2M4MmUxY2FhZTRjYjYyZjU1Y2VlNzQ2OWY0In0.eyJhdWQiOiIyIiwianRpIjoiZWZiZmMyNTA3YWNmN2JiMGZhMmMzYWI1OWQxMDQ3NDQ5OWE0MmJmZmFmOWRjNzY4Zjk0MzczYzgyZTFjYWFlNGNiNjJmNTVjZWU3NDY5ZjQiLCJpYXQiOjE2NzUyNDk3MzksIm5iZiI6MTY3NTI0OTczOSwiZXhwIjoxNzA2Nzg1NzM5LCJzdWIiOiIyMzk5Iiwic2NvcGVzIjpbXX0.a5MlC5MnGD3gdTOmrfDD457LyEQgOL-G_pKbV-XF2nfDL-TAR7ipkiMd22XMiOvxa5zuQKsvDzD4q4l3CNHgAsztSo4PBn8EdaAMuwlZLlwvta5DwM2hcOWwWzW9O4C6lNKHhWAhiT5eKb6NVApPd57SLJSgLrAmJe6ftvRIOr0TG9Q363yPF9zsoXCLpm0D7ygtONuh2AGwHNs1yB5XpCuGYVRwY9RcKSOD9nJJjUgTIjhFZwg3o7_DaTlByweFZT6FwVr-TOmCBLmtjf2hft7Y3wTGZzQHQJKT_jt9fKLujISxYbrO7OQdcBC5IVapMfcKN6FX-Celdgo9tEyWcCP2dNQ45r07RQBcVrZAhWpLO3XyDrpfpc5nvVVVHiBYWt-E89jwFSUYJJXHqABhw_KouUgQtxfUW_hov_t0p0cICieY2DUBpWhJeWxnFJPk4k4xCmyUH_kYmpYzJV9phJwKl0wj6pd8jP6WlNbr97QzVI5xJwpQAW7EaWZWp-Q6I8su-6na0uxCnYMBrE8PUhxoLp8rWJDxq0X0pGLSmn_t_SDcJ2ev_8yPWW65yXThD4yKP-xsSxLgHeMfgpt9N4XjkLnViofmWXI6flu4mqa0ZYrzbuYvm8OFJhHI7vRtWloF5sl5Qb8h1F5H-79w-706nHjkkUFRiaB75Ff5i4w'
    headers = {'accept': 'application/json', 'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImVmYmZjMjUwN2FjZjdiYjBmYTJjM2FiNTlkMTA0NzQ0OTlhNDJiZmZhZjlkYzc2OGY5NDM3M2M4MmUxY2FhZTRjYjYyZjU1Y2VlNzQ2OWY0In0.eyJhdWQiOiIyIiwianRpIjoiZWZiZmMyNTA3YWNmN2JiMGZhMmMzYWI1OWQxMDQ3NDQ5OWE0MmJmZmFmOWRjNzY4Zjk0MzczYzgyZTFjYWFlNGNiNjJmNTVjZWU3NDY5ZjQiLCJpYXQiOjE2NzUyNDk3MzksIm5iZiI6MTY3NTI0OTczOSwiZXhwIjoxNzA2Nzg1NzM5LCJzdWIiOiIyMzk5Iiwic2NvcGVzIjpbXX0.a5MlC5MnGD3gdTOmrfDD457LyEQgOL-G_pKbV-XF2nfDL-TAR7ipkiMd22XMiOvxa5zuQKsvDzD4q4l3CNHgAsztSo4PBn8EdaAMuwlZLlwvta5DwM2hcOWwWzW9O4C6lNKHhWAhiT5eKb6NVApPd57SLJSgLrAmJe6ftvRIOr0TG9Q363yPF9zsoXCLpm0D7ygtONuh2AGwHNs1yB5XpCuGYVRwY9RcKSOD9nJJjUgTIjhFZwg3o7_DaTlByweFZT6FwVr-TOmCBLmtjf2hft7Y3wTGZzQHQJKT_jt9fKLujISxYbrO7OQdcBC5IVapMfcKN6FX-Celdgo9tEyWcCP2dNQ45r07RQBcVrZAhWpLO3XyDrpfpc5nvVVVHiBYWt-E89jwFSUYJJXHqABhw_KouUgQtxfUW_hov_t0p0cICieY2DUBpWhJeWxnFJPk4k4xCmyUH_kYmpYzJV9phJwKl0wj6pd8jP6WlNbr97QzVI5xJwpQAW7EaWZWp-Q6I8su-6na0uxCnYMBrE8PUhxoLp8rWJDxq0X0pGLSmn_t_SDcJ2ev_8yPWW65yXThD4yKP-xsSxLgHeMfgpt9N4XjkLnViofmWXI6flu4mqa0ZYrzbuYvm8OFJhHI7vRtWloF5sl5Qb8h1F5H-79w-706nHjkkUFRiaB75Ff5i4w'}

    def __init__(self) -> None:
        pass

    def get_temp(self):
        weather.get_date_time()
        r = requests.get(weather.url, headers=weather.headers)
        data = json.loads(r.text)
        print('----->',data)
        data_weather = data['WeatherForecasts']
        data_weather = data_weather[2]
        data_keydata = str(data_weather)
        data_keydata = data_keydata.split(",")
        temp = data_keydata[3].split(" ")
        weather.temp = str(temp[3])
        return weather.temp

    def get_humidity(self):
        weather.get_date_time
        r = requests.get(weather.url, headers=weather.headers)
        data = json.loads(r.text)
        data_weather = data['WeatherForecasts']
        data_weather = data_weather[2]
        data_keydata = str(data_weather)
        data_keydata = data_keydata.split(",")
        hum = data_keydata[4].split(" ")
        hum = str(hum[2])
        hum = hum.split("}")
        weather.hum = str(hum[0])
        return weather.hum

    def get_date_time():
        weather.today = datetime.now() + timedelta(days=0, hours=0)
        weather.endPoint = {
            'province': '',
            'amphoe': '',
            'date': weather.dt_string[0],
            'time': weather.dt_string[1]}

    def change_city(window):
        xpos, ypos = window.current_location()
        new_city = sg.popup_get_text(
            'กรอกชื่อจังหวัด และอำเภอ', keep_on_top=True, location=(xpos+405, ypos))
        if new_city == None:
            return
        dataChange = str(new_city).split(' ')
        if len(dataChange) > 2 or len(dataChange) < 2:
            sg.popup(("ข้อมูลที่ระบุไม่ถูกต้อง"), keep_on_top=True)
            return
        if new_city is not None and len(dataChange) == 2:
            weather.endPoint['province'] = dataChange[0]
            weather.endPoint['amphoe'] = dataChange[1]
            weather.changeEnpoint(
                weather.endPoint['province'], weather.endPoint['amphoe'])

    def changeEnpoint(e1, e2):
        global dataChange
        try:
            changeLocation = f"https://data.tmd.go.th/nwpapi/v1/forecast/area/place?domain=2&province={e1}&amphoe={e2}&fields=tc,rh&starttime={weather.endPoint['date']}T{weather.endPoint['time']}"
            weather.get_date_time()
            r = requests.get(changeLocation, headers=weather.headers)
            data = json.loads(r.text)
            # print('this change', data)
            data_weather = data['WeatherForecasts']
            data_weather = data_weather[2]
            data_keydata = str(data_weather)
            data_keydata = data_keydata.split(",")
            temp = data_keydata[3].split(" ")
            weather.temp = str(temp[3])
            hum = data_keydata[4].split(" ")
            hum = str(hum[2])
            hum = hum.split("}")
            weather.hum = str(hum[0])
            dataChange['temp'] = weather.temp
            dataChange['prov'] = e1
            dataChange['amphoe'] = e2
            dataChange['Humidity'] = weather.hum
            # print('this is test', changeLocation)
            return changeLocation
        except (ConnectionError, IndexError):
            sg.popup(("ไม่พบพื้นที่ที่ระบุ"), keep_on_top=True)
            return
# --------------------------------------------------------------------------------------------------------------------------------------------------------


class gui(weather):

    sg.ChangeLookAndFeel('lightblue')
    BG_COLOR = "#FFC13F"  # sg.theme_text_color()
    TXT_COLOR = "#000000"  # sg.theme_background_color()
    ALPHA = 0.8
    timeout_minutes = 5 * (60 * 1000)
    todayGui = datetime.now() + timedelta(days=0, hours=0)
    dt_stringGui = todayGui.strftime("%Y-%m-%d %H:%M:%S").split()
    APP_DATA = {
        'City': weather.endPoint['province'] + '  อ.' + weather.endPoint['amphoe'],
        'Country': 'TH',
        'Postal': None,
        'Description': 'clear skys',
        'อุณหภูมิ': 101.0,
        'Feels Like': 72.0,
        'Wind': 0.0,
        'ความชื้น': 0,
        'Precip 1hr': 0.0,
        'Pressure': 0,
        'Updated': f'วันที่ {dt_stringGui[0]} ณ เวลา {dt_stringGui[1]}',
        'Icon': None,
        'Units': 'Imperial'
    }

    def __init__(self) -> None:
        super().__init__()

    def metric_row(metric):
        lbl = sg.Text(metric, font=('Arial', 10), pad=(15, 0), size=(9, 1))
        num = sg.Text(gui.APP_DATA[metric], font=(
            'Arial', 10, 'bold'), pad=(0, 0), size=(9, 1), key=metric)
        return [lbl, num]

    def create_window():
        col1 = sg.Column(
            [[sg.Text(gui.APP_DATA['City'], font=('Arial Rounded MT Bold', 20), pad=((22, 100), (25, 0)), size=(
                18, 1), background_color=gui.BG_COLOR, text_color=gui.TXT_COLOR, key='City')]],
            background_color=gui.BG_COLOR, key='COL1')
        col2 = sg.Column(
            [[sg.Text('×', font=('Arial Black', 16), pad=((1, 1), (1, 1)), justification='center', background_color=gui.BG_COLOR, text_color=gui.TXT_COLOR, enable_events=True, key='-QUIT-')]],
            element_justification='center', background_color=gui.BG_COLOR, key='COL2')
        # col2 = sg.Column(
        #     [[sg.Text('×', font=('Arial Black', 16), pad=(0, 0), justification='right', background_color=gui.BG_COLOR, text_color=gui.TXT_COLOR, enable_events=True, key='-QUIT-')],
        #      [sg.Image(data=gui.APP_DATA['Icon'], pad=((5, 10), (0, 0)), size=(100, 100), background_color=gui.BG_COLOR, key='Icon')]],
        #     element_justification='center', background_color=gui.BG_COLOR, key='COL2')
        col3 = sg.Column(
            [[sg.Text(gui.APP_DATA['Updated'], font=(
                'Arial', 10), background_color=gui.BG_COLOR, text_color=gui.TXT_COLOR, key='Updated')]],
            pad=(10, 5), element_justification='left', background_color=gui.BG_COLOR, key='COL3')
        col4 = sg.Column(
            [[sg.Text('คลิกเพื่อเปลี่ยนพื้นที่', font=('Arial', 10), background_color=gui.BG_COLOR,  # 'italic'
                      text_color=gui.TXT_COLOR, enable_events=True, key='-CHANGE-')]],
            pad=(10, 5), element_justification='right', background_color=gui.BG_COLOR, key='COL4')
        top_col = sg.Column([[col1, col2]], pad=(
            0, 0), background_color=gui.BG_COLOR, key='TopCOL')
        bot_col = sg.Column([[col3, col4]], pad=(
            0, 0), background_color=gui.BG_COLOR, key='BotCOL')
        lf_col = sg.Column(
            [[sg.Text(gui.APP_DATA['อุณหภูมิ'] + ' °C', font=('Haettenschweiler', 80), pad=(
                (10, 0), (0, 0)), justification='center', key='Temp')]],
            pad=(10, 0), element_justification='center', key='LfCOL')
        rt_col = sg.Column(
            # gui.metric_row('Feels Like'), gui.metric_row('Wind'), , gui.metric_row('Precip 1hr'), gui.metric_row('Pressure')
            [gui.metric_row('อุณหภูมิ'), gui.metric_row('ความชื้น')],
            pad=((15, 0), (25, 5)), key='RtCOL')
        layout = [[top_col], [lf_col, rt_col], [bot_col]]
        window = sg.Window(layout=layout, title='Weather Widget', size=(480, 315), margins=(0, 0), finalize=True,
                           element_justification='center', keep_on_top=True, no_titlebar=True, grab_anywhere=True, alpha_channel=gui.ALPHA)
        for col in ['COL1', 'COL2', 'TopCOL', 'BotCOL', '-QUIT-']:
            window[col].expand(expand_y=True, expand_x=True)
        for col in ['COL3', 'COL4', 'LfCOL', 'RtCOL']:
            window[col].expand(expand_x=True)
        return window

    def show_display(self):
        gui.APP_DATA['อุณหภูมิ'] = self.get_temp()
        gui.APP_DATA['ความชื้น'] = self.get_humidity()
        window = gui.create_window()
        while True:
            try:
                event, _ = window.read(timeout=gui.timeout_minutes)
                if event in (None, '-QUIT-'):
                    break
                if event == '-CHANGE-':
                    weather.change_city(window)
                    gui.APP_DATA['อุณหภูมิ'] = dataChange['temp']
                    gui.APP_DATA['City'] = dataChange['prov'] + ' อ.' + dataChange['amphoe']
                    gui.APP_DATA['ความชื้น'] = dataChange['Humidity']
                    window.close()
                    window = gui.create_window()
            except (KeyError, ValueError, TypeError, ):
                pass


# --------------------------------------------------------------------------------------------------------------------------------------------------------
a = gui()
m = weather()

a.show_display()

# co1 [sg.Text(gui.APP_DATA['Description'], font=('Arial', 12), pad=(10, 0), background_color=gui.BG_COLOR, text_color=gui.TXT_COLOR, key='Description')]
