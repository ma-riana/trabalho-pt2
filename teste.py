import PySimpleGUI as sg

sg.theme('BluePurple')

layout = [[sg.InputCombo(('OI', 'Oi dnv'), size=(20, 2), key='cb_opcoes')],
          [sg.Button('Show'), sg.Button('Exit')]]

window = sg.Window('Pattern 2B', layout)
event, values = window.read()

print(event, values)


window.close()