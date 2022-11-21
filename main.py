import requests, os
from pprint import pprint
import msvcrt as m
def enter():
    print("Presione ENTER para continuar...")
    m.getch()
clear = lambda: os.system('cls')
clear()
a="metric"
i="sp"
API_Clave = '11b788f86dfaa5c8ad9bf936146ca76d'
ciudad = input("Digite la ciudad: ")
datos_clima =requests.get(
        "http://api.openweathermap.org/data/2.5/weather?appid="+API_Clave+"&q="+ciudad+"&units="+a+"&lang="+i)

def hola():
    clear()
    print("Seleccione la accion a realizar: ")
    print("1. Descripcion")
    print("2. Temperatura")
    print("3. Humedad")
    print("4. Presion")
    print("5. Viento")
    print("6. Salir")
    o = input("-->")
    switch_o={
        "1":"desc",
        "2":"temp",
        "3":"hum",
        "4":"pre",
        "5":"vie"
    }
    if o == "1":
        desc()
    else:
        if o == "2":
            temp()
        else:
            if o == "3":
                hum()
            else:
                if o == "4":
                    pre()
                else:
                    if o == "5":
                        vie()
                    else:
                        if o == "6":
                            clear()
                            print("Gracias por usar el programa")
                            enter()
                            quit()
                        else:
                            print("Digite una opcion valida")
                            hola()

def desc():
    clear()
    print(f"{ciudad} se encuentra actualmente con la siguente descripcion: ")
    
    print(datos_clima.json()["weather"][1]["description"])
    print()
    enter()
    hola()

def temp():
    clear()
    print(f"{ciudad} actualmente tiene una temperatura de {datos_clima.json()['main']['temp']}°C (Se siente como{datos_clima.json()['main']['feels_like']}°C)")
    print(f"Temperatura maxima: {datos_clima.json()['main']['temp_max']}°C")
    print(f"Temperatura minima: {datos_clima.json()['main']['temp_min']}°C")
    print()
    enter()
    hola()

def hum():
    clear()
    print(f"{ciudad} actualmente tiene una hunedad del {datos_clima.json()['main']['humidity']}%")
    print()
    enter()
    hola()

def pre():
    clear()
    print(f"{ciudad} tiene una presion equivalente a {datos_clima.json()['main']['pressure']} hPa")
    print()
    enter()
    hola()

def vie():
    clear()
    print(f"{ciudad} tiene vientos de {round(((datos_clima.json()['wind']['speed'])/1000)*3600)} km/h, con direccion de {datos_clima.json()['wind']['deg']}°")
    print()
    enter()
    hola()

hola()