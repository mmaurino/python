import json
import PySimpleGUI as sg
from datetime import datetime
from os.path import isfile
def siexiste():
    with open('jugadores.json', 'r') as archivo:
        data = json.load(archivo)
    data.update({values[0]:{'juego ':event,'fecha ':fecha}})
    with open('jugadores.json', 'w') as archivo:
        json.dump(data, archivo) 
sg.theme('DarkAmber')
layout = [[sg.Text('INGRESE NOMBRE ')],[sg.Input()],[sg.Text('SELECCIONE EL JUEGO A JUGAR ')],[sg.Button('AHORCADO'), sg.Button('TATETI')]]      
window = sg.Window('Juegos', layout)    
event, values = window.read()    
window.close()
now = datetime.now()
fecha= now.strftime('Dia :%d, Mes: %m, Anio: %Y, Hora: %H, Minutos: %M, Segundos: %S')
if(isfile("jugadores.json")):
    siexiste()
else:
    archivo = open("jugadores.json", "a")
    datos={values[0]:{'juego':event,'fecha':fecha}}
    json.dump(datos, archivo) 
    archivo.close()
if event=='AHORCADO':
    import ahorcado
elif event=='TATETI':
    import tateti
    
