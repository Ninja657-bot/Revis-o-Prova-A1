import os
import math
os.system("cls")

numero = int(input("Digite um número: "))

def verificar_numero(numero):
    if numero <= 0 :
        return False, 0, "Inválido"
    
    qtd_divisores = 0
    raiz = int(math.sqrt(numero))
    for i in range(raiz):
        i += 1
        if numero % i == 0:
            if numero // i != i:
                qtd_divisores += 2
            else:
                qtd_divisores += 1
    
        
    if qtd_divisores == 2:
        primo = True
    else: 
        primo = False
        
    if numero % 2 == 0:
        paridade = "Par"
    else: 
        paridade = "Impar"
    
    resultado = (primo, qtd_divisores, paridade)
    return resultado

resultado = verificar_numero(numero)

print(f"O número é Primo:", resultado[0])
print(f"Quantos divisores ele possui:", resultado[1])
print(f"É um número Par ou Ímpar:", resultado[2])