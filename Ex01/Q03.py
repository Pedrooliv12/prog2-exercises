'''
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
'''

vogais = "aeiou"
consoantes = "bcdfghjklmnpqrstvwxyz"
letra = input("Digite uma letra: ").lower()

if letra not in vogais and letra not in consoantes:
    print("Isso não é uma letra, animal.")
elif letra in vogais:
    print("Essa letra é uma vogal.")
elif letra in consoantes:
    print("Essa letra é uma consoante.")
