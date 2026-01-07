#Atribuição de valores a variáveis
nome = "Bruno Mazini de Almeida"
idade = 25

#Tratamento de vulnerabilidade
def ler_valor_correto (mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor <=0:
                print("ERRO: Digite um valor maior que zero.")
            else:
                return valor
        except ValueError:
            print("Valor inválido. Digite apenas números.")

#Entrada de dados do usuário
altura = ler_valor_correto("Digite sua altura em metros: ")
peso = ler_valor_correto ("Digite seu peso em Kg: ")

#Calculo IMC
IMC = peso/ (altura **2)

print()

#Saida de dados formatada
print(f"Nome:{nome}")
print(f"Idade: {idade}")
print(f"Altura: {altura} M")
print(f"Peso: {peso} Kg")
print(f"IMC: {IMC}")
