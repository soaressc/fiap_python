"""
parâmetro do tipo: para string como modo de saída
o padrão é "t"(text), por isso "r" ou "rt" ou "r+t"

a função .readlines() imprime uma lista com uma linha do arquivo em cada posição
útil para quebrar grandes documentos de texto em partes
"""

with open("teste.txt", "rt") as arquivo:
    conteudo = arquivo.read()

print("Tipo de dado da variável: ", type(conteudo))
print("\nConteúdo do arquivo:\n",conteudo)