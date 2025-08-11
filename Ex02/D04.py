'''
Faça um programa que leia e valide as seguintes informações:
1. Nome: maior que 3 caracteres;
2. Idade: entre 0 e 150;
3. Salário: maior que zero;
4. Sexo: 'f' ou 'm';
5. Estado Civil: 's', 'c', 'v', 'd';
5. Use a função len(string) para saber o tamanho de um texto (número de caracteres).
'''

while True:
    nome = input("Digite seu nome: ").lower()

    if not 3 < len(nome):
        print("Nome deve ter ao menos 3 caracteres")
        continue
    else:
        break

while True:
    idade = int(input("Digite sua idade: "))

    if not 0 <= idade < 150:
        print("Digite um valor entre 0 e 150")
        continue
    else:
        break

while True:
    salario = float(input("Digite seu salário: "))

    if not salario > 0:
        print("Digite um valor maior que 0")
        continue
    else:
        break

while True:
    sexo = input("Digite seu sexo [m/f]: ").lower()

    if sexo not in ("m", "f"):
        print("Digite [ m ] o [ f ]")
        continue
    else:
        break

while True:
    estado_civil = input("Onde se encontra seu estado civil atual:\n[ s ] - Solteiro\n[ c ] - Casado\n[ v ] - Viuvo\n[ d ] - Divorciado\n\nResposta:").lower()

    if estado_civil not in ("s", "c", "v", "d"):
        print("Digite a resposta correta")
        continue
    else:
        match estado_civil:
            case "s":
                estado_civil = "Solteiro"
            case "c":
                estado_civil = "Casado"
            case "v":
                estado_civil = "Viuvo"
            case "d":
                estado_civil = "Divorciado"

        break

print("=-" * 10)
print(f"Nome: {nome}.\nIdade: {idade}.\nSalário: {salario}.\nSexo: {"Masculino" if sexo == "m" else "Feminino"}.\nEstado civil: {estado_civil}.")
