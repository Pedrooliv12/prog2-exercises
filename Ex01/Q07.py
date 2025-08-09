'''
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
a. "Telefonou para a vítima?"
b. "Esteve no local do crime?"
c. "Mora perto da vítima?"
d. "Devia para a vítima?"
e. "Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
'''

contador = 0

def perguntar(pergunta):
    print(pergunta)

    while True:
        resposta = input("Responda com s/n: ").lower()

        if resposta not in ("s", "n") or len(resposta) > 1:
            print("Valor Inválido!")
            continue
        else:
            break
    
    return resposta


perguntas = ["Telefonou para a vítima?",
             "Esteve no local do crime?",
             "Mora perto da vítima?",
             "Devia para a vítima?",
             "Já trabalhou com a vítima?"]

for pergunta in perguntas:
    if perguntar(pergunta) == "s":
        contador += 1

if contador == 5:
    print("Assassino")
elif 3 <= contador <= 4:
    print("Cúmplice")
elif contador == 2:
    print("Suspeito")
else:
    print("Inocente")
