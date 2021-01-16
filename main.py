import PySimpleGUI as sg
from pytube import YouTube

#  https://www.youtube.com/watch?v=74ZSIJk2pcg

sg.theme('reddit')

layout = [[sg.Text('Title:'), sg.Text(size=(15,1), key='-OUTPUT-')],
          [sg.Input(key='-IN-')],
          [sg.Button('Load'), sg.Button('Exit')]]

window = sg.Window('Arvid', layout)

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Load':
        # Update the "output" text element to be the value of "input" element
        link = values['-IN-']
        yt = YouTube(link)
        window['-OUTPUT-'].update(yt.title)
window.close()




