#EXERCICIO: Faça um programa que pergunte a idade, o peso e a altura de uma pessoa, e decide se ela está apta a ser do Exercito, para entrar no exercito é preciso ter mais de 18anos
#e pesar mais ou igual a 60kilos, e medir mais ou igual a 1.70metros.
#FernandoCosta
#30/11/2021


idade = int(input(print("DIGITE SUA IDADE: ")))
altura = float(input(print("DIGITE SUA ALGURA: ")))
peso = float(input(print("DIGITE SEU PESO: ")))


if idade > 18 and altura >= 1.70 and peso >= 60:
    print("Parabéns você está apto para entrar no Exercito")
else:
    print("Infelizmente você não está apto")
