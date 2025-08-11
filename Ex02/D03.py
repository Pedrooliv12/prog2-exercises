'''
Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
'''

numbers = []

while True:
    try:
        valor = int(input("Digite o valor (0 a 1000): "))

        if not 0 <= valor < 1000:
            print("Erro: digite um número entre 0 e 1000")
            continue
    except ValueError:
        print("Digite um número inteiro")
        continue
    
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
