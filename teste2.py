import PySimpleGUI as sg

inp = sg.popup_get_text("aloha", title="bible")
print("You entered: ", inp)
print(inp)