import os 
os.system("cls")
dados = []
quantidade = 0
loops = 0

while True:
    os.system("cls")
    print("- Analisador de Pacotes -")
    print()
    peso = float(input("Digite o peso em Kg do pacote: "))
    
    if peso <= 0:
        os.system("cls")
        print("Valor inválido")
        print("Seguindo para relatório")
        print()
        input("Pressione ENTER para prosseguir")
        break
    
    elif peso >= 30:
        os.system("cls")
        loops += 1
        print("ERRO")
        print("Peso acima do valor permitido")
        print()
        input("Pressione ENTER para prosseguir")
        continue
    
    else:
        os.system("cls")
        quantidade += 1
        loops += 1
        dados.append(peso)
        print("Pacote registrado com Sucesso")
        print()
        input("Pressione ENTER para prosseguir")
        continue

if not dados:
    os.system("cls")
    print("ERRO")
    print("Nenhum pacote válido foi registrado")
    print("Encerrando programa")
    exit()
    
pacotes_invalidos = loops - quantidade
maior = max(dados)
menor = min(dados)
soma = sum(dados)
media = soma / len(dados)
os.system("cls")

print("- Relatório -")
print()
print(f"Total de pacotes registrados: {loops}")
print(f"Pacotes válidos: {quantidade}")
print(f"Pacotes inválidos: {pacotes_invalidos}")
print(f"Peso total dos pacotes: {soma} kg")
print(f"Média de peso dos pacotes: {media} kg")
print(f"Pacote mais pesado: {maior} kg")
print(f"Pacote mais leve: {menor} kg")