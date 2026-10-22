import os
os.system("cls")

print("- Programa de Analise de risco -")
print()
valor = float(input("Digite o valor do faturamento Mensal: "))
os.system("cls")

if valor <0:
    print("Erro")
    
elif valor == 0:
    print("Faturamento igual a 0.0: Risco Extremamente Alto (Sem Operação)")

elif valor <= 10000.00:
    print("Faturamento entre 0.0 (exclusive) e 10000.00 (inclusive): Risco Alto")

elif valor <= 50000.00:
    print("Faturamento entre 10000.00 (exclusive) e 50000.00 (inclusive): Risco Médio")

elif valor <= 150000.00:
    print("Faturamento entre 50000.00 (exclusive) e 150000.00 (inclusive): Risco Baixo")

else:
    print("Faturamento superior a 150000.00: Risco Mínimo (Cliente Premium)")

print()
print("Encerrando o programa")
input("Presione ENTER para continuar")