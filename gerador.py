import PySimpleGUI as sg

def init_components():
   sg.ChangeLookAndFeel('Dark Gray 13')
   for i in sg.Text.fonts_installed_list():
      print(i)



init_components()