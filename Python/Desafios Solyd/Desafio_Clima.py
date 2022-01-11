import requests
import json
import os
import time

while True:
    os.system('cls')
    api = ... #digite a sua api aqui
    cidade = input("Digite sua cidade: ")
    resposta = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+cidade+"&appid="+api)
    previsao = json.loads(resposta.text)

    print("### PREVISÃO DO TEMPO NA SUA CIDADE")
    print("")
    print("Codição: ", previsao['weather'][0]['main'])
    print("Temperatura: {}ºC" .format(round(float(previsao['main']['temp']) - 273.15)))
    print("Temperatura Minima {}ºC".format(round(float(previsao['main']['temp_min']) - 273.15)))
    print("Temperatura Minima {}ºC".format(round(float(previsao['main']['temp_max']) - 273.15)))
    print("Humidade: {}%".format(previsao['main']['humidity']))
    print("Velocidade do Vento: {} Km/h".format(float(previsao['wind']['speed']) * 3.6))
    time.sleep(5)