'''
A série de Fibonacci é formada pela sequência 0,1,1,2,3,5,8,13,21,34,55,...
Faça um programa que gere a série até que o valor seja maior que 500.
'''

def fibonacci():
    fib = [0, 1]
    index = 2

    while True:
        if fib[-1] >= 500:
            break
        else:
            fib.append(fib[index -1] + fib[index - 2])
            index += 1
    
    return fib


print(fibonacci())
