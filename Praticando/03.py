#Declaração de variaveis
detergente = 2.10
sorvete = 13.99
papel_higienico = 19.50
arroz = 23.99

#Entrada de dados - Usuario
quantidade_detergente = int(input("Digite a quantidade de Detergente que deseja levar:"))
quantidade_sorvete = int(input("Digite a quantidade de sorvete que deseja levar:"))
quantidade_papel = int(input("Digite a quantidade de papel higienico deseja levar:"))
quantidade_arroz = int(input("Digite a quantidade de arroz deseja levar:"))

#Calculo
valor_total = (quantidade_detergente * detergente) + (quantidade_sorvete * sorvete) + (quantidade_papel * papel_higienico) + (quantidade_arroz * arroz)

#Saida de dados
print("O valor total é de: R$", valor_total)