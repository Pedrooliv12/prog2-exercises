'''
Faça um programa, utilizando while, que permita o usuário fazer contas de adição enquanto 
quiser.
'''

print("Operação - Adição\n")

while True:
    number1 = int(input("Digite um número: "))
    number2 = int(input("Digite outro número: "))
    print(f"{number1} + {number2} = {number1 + number2}")

    print("Deseja realizar mais uma soma: [S ou N]")

    while True:
        resposta = input("Resposta: ").lower()

        if resposta not in ("s", "n"):
            print("Valor errado")
            continue
        else:
            break

    if resposta == 's':
        continue
    else:
        break 
