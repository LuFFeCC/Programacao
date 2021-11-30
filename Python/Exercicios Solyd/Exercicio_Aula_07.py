#Exercicio: Escreva uma função que receça um objeto de coleção e retorna o valor do maior numero dentro dessa coleção.
#Faça outra função que retorna o menor numero dessa coleção.

def maior_valor(lista):
        maior = 0
        for name in lista:
            if name > maior:
                maior = name
        else:
            print("O maior numero é {}".format(maior))
            return maior


def menor_valor(lista):
        menor = 10
        for name in lista:
            if name < menor:
                menor = name
        else:
            print("O menor numero é {}".format(menor))
        return menor



lista = (4,6,2,3,1,64,25)
maior_valor(lista)
menor_valor(lista)