preco = float(input("Digite o preço unitário do produto: "))
quant = int(input("Digite a quantidade do produto: "))
dinheiro = float(input("Digite o preço recebido: "))

total = preco * quant

if dinheiro > total:
    troco = dinheiro - total
    print(f"Troco: {troco}")    
else: 
    troco = total - dinheiro
    print(f"Dinherio insuficiente. Ainda faltam R${troco}")


