'''
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é 
aquele que é divisível somente por ele mesmo e por 1.
'''

number = int(input("Digite um número: "))

if number <= 1:
    print("Não é primo")
else:
    primo = True

    for i in range(2, number):
        if number % i == 0:
            primo = False
            break
    
    if primo:
        print("Primo") 
    else:
        print("Não é primo")
        