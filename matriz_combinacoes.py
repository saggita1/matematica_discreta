def gerar_combinacoes(lista, numero):
    def combinacao_atual(lista, prefixo, numero, indice):
        if numero == 0:
            resultado.append(prefixo)
            return
        for i in range(indice, len(lista)):
            novo_prefixo = prefixo + ',' + lista[i] if prefixo else lista[i]
            combinacao_atual(lista, novo_prefixo, numero - 1, i + 1)

    resultado = []
    for n in range(1, numero + 1):  # Gera combinações para todos os tamanhos de 1 até o número
        combinacao_atual(lista, "", n, 0)
    return resultado

# Receber entrada do usuário
entrada = input("Digite os caracteres separados por vírgula: ")
numero = int(input("Digite o número máximo de elementos nas combinações: "))

# Transformar a string de entrada em uma lista de caracteres
lista_caracteres = entrada.split(',')

# Gerar combinações
combinacoes = gerar_combinacoes(lista_caracteres, numero)

print("{}")
# Exibir o resultado
for combinacao in combinacoes:
    print(f"{{{combinacao}}}")
