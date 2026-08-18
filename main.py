import os 

def cal_final(base,desc):
    return base - base * (desc/100)

def exibir(nome, base, fin):
    economia = base - fin
    limpar()
    print("-" * 40)
    print(f"PRODUTO: {nome}\nPreço Original: R$ {base}\nPreço com Desconto: R$ {fin}\nEconomia Gerada: R$ {economia}")
    print("-" * 40)
    input("Pressione ENTRE para ir para o proximo produto.")
    limpar()

def limpar():
    os.system("clear")

for i in range(3):
    nome =  input(f"Digite o nome do {i+1} produto: ")
    preço_base = float(input(f"Digite o preço do {i+1} produto: R$"))
    desconto = float(input(f"Digite a procentagem de {i+1} desconto: %"))
    preco_fin = cal_final(preço_base, desconto)
    exibir(nome,preço_base,preco_fin)
