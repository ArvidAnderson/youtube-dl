import PySimpleGUI as sg
from pytube import YouTube

#ADD THEME


layout = [[sg.Text('Title:'), sg.Text(size=(15, 1), key='-OUTPUT-')],
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

        except:
            window['-OUTPUT-'].update('Not a youtube video', text_color=('red'))
            window.FindElement('Download').Update('Download', disabled=True, button_color=('white', 'red'))
    elif event == 'Download':
        YouTube(link).streams.first().download()

window.close()
