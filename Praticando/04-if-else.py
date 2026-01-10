print("Bem-vindo, Informações sobre voto!")

#Entrada de dados do usuário
idade = int(input("Informe sua idade:"))

#Logica
if idade <16:
    print("Você ainda não pode votar!")
elif idade < 18 or idade > 70:
    print("Seu voto é opcional!")
else:
    print("Seu voto é obrigatorio!")

