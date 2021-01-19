import PySimpleGUI as sg
from PIL import Image
import requests
from io import BytesIO
from pytube import YouTube

#Fix later
image_element = sg.Image(filename='test.PNG')

layout = [[sg.Text('Title:'), sg.Text(size=(15, 1), key='-OUTPUT-')],
          [image_element],
          [sg.Input(key='-IN-')],
          [sg.Button('Load'), sg.Button('Download', disabled=True, button_color=('white', 'red')), sg.Button('Exit')]]

window = sg.Window('Arvid', layout)

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
            window['-OUTPUT-'].update(yt.title, text_color=('black'))
            window.FindElement('Download').Update('Download', disabled=False, button_color=('white', 'green'))
            print(YouTube(link).thumbnail_url)

            #IMG FIX LATER
            url_thumbnail = YouTube(link).thumbnail_url
            response = requests.get(url_thumbnail, stream=True)
            img = Image.open(response.raw)
            img = img.save("thumbnail_temporary.png")
            image_element.update('thumbnail_temporary.png')
        except:
            window['-OUTPUT-'].update('Not a youtube video', text_color=('red'))
            window.FindElement('Download').Update('Download', disabled=True, button_color=('white', 'red'))
    elif event == 'Download':
        YouTube(link).streams.first().download()
        YouTube(link).thumbnail_url
window.close()
