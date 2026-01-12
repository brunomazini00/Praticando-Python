texto = "Programação"
letras_para_contar = "a"
contador = 0

for letra in texto:
    if letra == letras_para_contar:
        contador +=1

print(f"A letra '{letras_para_contar}' aparece {contador} vezes na palavra '{texto}'")