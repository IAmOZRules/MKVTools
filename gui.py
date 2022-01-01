from func import *
import PySimpleGUI as sg

layout = [
    [sg.Text('MKVTools', justification='center', font=("Helvetica", 25))],
    [sg.Text('IMDB Code', size=(13, 1)), sg.InputText()],
    [sg.Text('Season Start', size=(13, 1)), sg.InputText(size=(15, 1)),
     sg.Text('Season End'), sg.InputText(size=(16, 1))],
    [sg.Text('Episode Directory', size=(13, 1)), sg.InputText()],
    [sg.Text('Subtitle Directory', size=(13, 1)), sg.InputText()],
    [sg.Checkbox('Rename Tags', default=False, size=(31, 1)),
     sg.Button('Rename', size=(8, 1)), sg.Button('Cancel', size=(8, 1))],
]

window = sg.Window('MKVTools', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break

    code = values[0]

    start = int(start) if values[1] != '' else 0
    end = int(end) if values[2] != '' else 0
    episode_dir = values[3]
    subtitle_dir = values[4]
    rename_tag = values[5]

    if event == 'Rename':
        series, seasons, episodes = get_episodes(code, start, end)

        if episode_dir != '':
            rename_episode(episode_dir, episodes)

        if subtitle_dir != '':
            rename_subtitle(subtitle_dir, episodes)

        if rename_tag:
            edit_tag(episode_dir)
        
        sg.popup('Rename Complete', title='MKVTools', keep_on_top=True)
        
window.close()
