import PySimpleGUI as sg
import requests

layout = [
    [sg.Text("Digite seu CEP")],
    [sg.Input()],
    [sg.Button("Enviar"),sg.Button("Cancelar")],
    [sg.Output(size=(40,13),key='-OUTPUT-')]
]

window = sg.Window("INFO_CEP",layout)

while True:
    event,value = window.read()

    if event == 'Cancelar' or event == sg.WINDOW_CLOSED:
        break

    elif event == 'Enviar':
        window['-OUTPUT-'].update("")
        try:
            request_info = requests.get(f'https://viacep.com.br/ws/{value[0]}/json/')
            informações = request_info.json()
            for x,y in informações.items():
                print(x.upper()+":",y)
        except:
            window['-OUTPUT-'].update("CEP Inválido")

