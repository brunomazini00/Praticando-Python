for raiz in range(32,100):
    num = raiz * raiz #Calcula o número gerado pela raiz
    menor = num % 100 #Obtem o número dos algarismos menos significativos
    maior = num // 100 #Obtem o número dos algarismos mais significativo

    if (maior + menor) == raiz:#Valida se a raiz corresponde a soma
        print(num)
        print(maior)
        print(menor)
        print(raiz)

print("Terminou!")
print("saiu",raiz)
