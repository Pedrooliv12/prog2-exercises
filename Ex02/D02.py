'''
Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos 
valores.
'''

numbers = []

while True:
    valor = int(input("Digite o valor: "))
    numbers.append(valor)

    while True:
        resposta = input("Deseja adicionar mais números [s/n]: ").lower()

        if resposta not in ("s", "n"):
                print("Valor errado")
                continue
        else:
            break
    
    if resposta == "s":
            continue
    else:
        break

print(f"Menor valor: {min(numbers)}, maior valor: {max(numbers)}, soma dos valores: {sum(numbers)}")
