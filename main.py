import PySimpleGUI as sg
from PIL import Image
import requests #For thumbnail url img
from pytube import YouTube

sg.LOOK_AND_FEEL_TABLE['YOUTUBE_THEME_ARVID'] = {'BACKGROUND': '#282828',
                                        'TEXT': '#FFFFFF',
                                        'INPUT': '#686868',
                                        'TEXT_INPUT': '#282828',
                                        'SCROLL': '#c7e78b',
                                        'BUTTON': ('white', '#686868'),
                                        'PROGRESS': ('#01826B', '#D0D0D0'),
                                        'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                        }

sg.theme('YOUTUBE_THEME_ARVID')

#Fix later
image_element = sg.Image(filename='logo.png')

layout = [[sg.Text('No YouTube video selected', text_color=('red')), sg.Text(size=(45, 1), key='-OUTPUT-')],
          [image_element],
          [sg.Input(key='-IN-')],
          [sg.Button('Load'), sg.Button('Download', disabled=True, button_color=('white', 'red')), sg.Button('Exit')]]

window = sg.Window('Arvid', layout, size=(350, 300))


while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Load':
        # Update the "output" text element to be the value of "input" element
        try:
            link = values['-IN-']
            yt = YouTube(link)
            window['-OUTPUT-'].update(yt.title, text_color=('#FFFFFF'))
            window.FindElement('Download').Update('Download', disabled=False, button_color=('white', 'green'))
            print(YouTube(link).thumbnail_url)
            #IMG
            url_thumbnail = YouTube(link).thumbnail_url
            response = requests.get(url_thumbnail, stream=True)
            img = Image.open(response.raw)
            img = img.save("thumbnail_temporary.png")
            image_element.update('thumbnail_temporary.png')
        except:
            window['-OUTPUT-'].update('Not a youtube video', text_color=('red'))
            window.FindElement('Download').Update('Download', disabled=True, button_color=('white', 'red'))
            image_element.update('logo.png')
    elif event == 'Download':
        YouTube(link).streams.first().download()
        YouTube(link).thumbnail_url
window.close()
