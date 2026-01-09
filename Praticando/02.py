#Definição de valores a variaveis
hamburguer = 18.50
batata_frita = 4.75
refrigerante_lata = 3.50
sobremesa = 10.00

#Entrada de dados - Usuario
quantidade_hamburguer = int(input("Digite a quantidade de hamburguer desejada:"))
quantidade_batata = int(input("Digite a quantidade de batata frita desejada:"))
quantidade_refrigerante = int(input("Digite a quantidade de latas desejadas:"))

#Calculo
valor_total = (hamburguer * quantidade_hamburguer) + (batata_frita * quantidade_batata) + (refrigerante_lata * quantidade_refrigerante)

#Saida de dados - Valor total
print("O valor total do seu pedido é: R$" ,valor_total)
