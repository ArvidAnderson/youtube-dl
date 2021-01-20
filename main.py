import image_downloader
import PySimpleGUI as sg
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
img_res = 366, 188

layout = [[sg.Text('No YouTube video selected',  text_color=('red')), sg.Text(size=(45, 1), key='-OUTPUT-')],
          [image_element],
          [sg.Input(key='-IN-')],
          [sg.Button('Load'), sg.Button('Download', disabled=True, button_color=('white', 'red')), sg.Button('Exit')]]

window = sg.Window('Arvid', layout, resizable=False, size=(350, 300))


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
            url_thumbnail = YouTube(link).thumbnail_url
            image_element.update(image_downloader.dl_thumbnail_url(url_thumbnail, img_res))
        except:
            window['-OUTPUT-'].update('Not a youtube video', text_color=('red'))
            window.FindElement('Download').Update('Download', disabled=True, button_color=('white', 'red'))
            image_element.update('logo.png')
    elif event == 'Download':
        YouTube(link).streams.first().download()
        YouTube(link).thumbnail_url
window.close()
