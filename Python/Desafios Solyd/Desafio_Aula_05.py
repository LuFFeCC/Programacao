#Exercicio: Faça um programa que leia a quantidade de pessoas que serao convidadas para uma festa.
#Após isso o programa irá perguntar o nome de todas as pessoas e colocar numa lista de convidados
#Após isso irá imprimir todos os nomes da lista
#FernandoCosta
#30/11/2021

convidados = int(input("Quantos convidados estarão na lista de convidados: "))
totalconvidados = []
i=1

while i <= convidados:

    lista_convidados = input(print("Digite o nome do convidado #{}: ".format(i)))
   
    totalconvidados.append(lista_convidados)

print(totalconvidados)