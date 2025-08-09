'''
Faça um Programa que pergunte em que turno você estuda.
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
'''

print("Qual turno você estuda?\n[ M ] Matutino\n[ V ] Vespertino\n[ N ] Noturno")

while True:
    resposta = input("Sua resposta: ").lower()

    if resposta not in ("m", "v", "n") or len(resposta) > 1:
        print("Valor Inválido!")
        continue
    else:
        break

match resposta:
    case "m":
        print("Bom dia!")
    case "v":
        print("Boa tarde!")
    case "n":
        print("Boa noite!")
