nome = ""
preco = 0.0
desconto = 0.0
preco_final = 0.0
produtos = []

def CalcularValorFinal(Valor_base = 0.0, taxa_desconto = 0.0):
    valor_com_desconto = Valor_base - (Valor_base * (taxa_desconto/100))
    return valor_com_desconto

def ExibirRecibo(nome_produto = "", valor_original = 0.0, valor_pago = 0.0):
    print("-" * 20)
    print(f"Produto: {nome_produto} \nVocê economizou: R${(valor_original - valor_pago):.2f} \nValor a pagar: R${valor_pago:.2f}")
    print("-" * 20)

while True:
    nome =  input(f"Digite o nome do produto: ")
    preco = float(input(f"Digite o preço do produto: R$"))
    desconto = float(input(f"Digite a procentagem de desconto: %"))

    preco_final = CalcularValorFinal(preco, desconto)

    produto = [nome, preco, desconto, preco_final]
    produtos.append(produto)

    opcao = input("Deseja incluir um novo produto? s/n").lower()

    if opcao != "s":
        for produto in produtos:
            ExibirRecibo(produto[0], produto[1], produto[3])
        break