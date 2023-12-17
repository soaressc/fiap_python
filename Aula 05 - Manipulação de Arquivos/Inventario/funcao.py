def menu():
    opcao = 0
    while opcao not in range(1, 4):
        opcao = int(input("Digite: \n<1> para registrar ativo\n<2> para persistir em arquivo\n<3> para exibir ativos armazenados\nOpção "))
    return opcao

def registrar_ativo(inventario):
    resposta = "S"
    print("\n")
    while resposta == "S":
        no_patrimonio = input("Digite o número do patrimônio: ")
        inventario[no_patrimonio] = [input("Digite a data da última atualização: "), input("Digite a descrição: "), input("Digite o departamento: ")]
        resposta = input("Digite 'S' para continuar: ").upper()

def persistir_em_arquivo(inventario):
    with open("inventario.csv", "a") as inv:
        for chave, valor in inventario.items():
            inv.write(chave + ";" + valor[0] + ";" + valor[1] + ";" + valor[2] + "\n")
    print("Persistido com sucesso!")

def exibir():
    with open("inventario.csv", "r") as inv:
        for ativo in inv.readlines():
            linha = ativo.split(";")
            print("Descrição do ativo: " + linha[2])
            print("Departamento: " + linha[3])