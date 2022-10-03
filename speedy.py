import speedtest
import PySimpleGUI as sg

sg.theme('DarkTeal9')
layout = [
        [ sg.Text("Speed Tester")],
        [sg.Text("Download",key='Download')],
        [sg.Text("Upload",key='Upload')],
        [sg.Button("START TEST")]
        ]


window = sg.Window("Speedy", layout, margins=(130, 200))
speed= speedtest.Speedtest()

while True:
    event, values = window.read()
    if event == "START TEST":
        down=speed.download()
        up = speed.upload()
        window.Element('Download').update(down)
        window.Element('Upload').update(up)
        
    elif event == sg.WIN_CLOSED:
        break
    

window.close()