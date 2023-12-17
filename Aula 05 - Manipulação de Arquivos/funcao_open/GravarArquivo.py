"""
open() junto ao comando “with”, permite representar, dentro do bloco
identado, o arquivo “teste.txt” por meio do apelido arquivo

o controle de encerramento fica por contado with, não é necessário fechar
o arquivo não ficará aberto na memória sem necessidade

como o caminho é apenas "teste.txt", ele considera que o documento está
na pasta main

parâmetro "r", de leitura (read). a função read() lê o conteúdo do teste.txt

with open("teste.txt", "r") as arquivo:
    conteudo = arquivo.read()

"""

# write() passar o conteúdo dentro do arquivo
with open("teste.txt", "w") as arquivo:
    arquivo.write("Nunca foi tão fácil criar um arquivo.")

# o parâmetro "a" permite adicionar
with open("teste.txt", "a") as arquivo:
    arquivo.write("\nContinuação do texto.")