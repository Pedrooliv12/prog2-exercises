'''
Faça um programa, utilizando while, que mostre na tela de 0 até N, em que N é o limite 
inserido pelo usuário.
'''

contador = 0
limite = int(input("Contar até: "))

while contador <= limite:
    print(contador)
    contador += 1
