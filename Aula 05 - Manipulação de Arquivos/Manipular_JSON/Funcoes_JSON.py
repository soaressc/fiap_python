import json
import os

def criar_inventario():
    if os.path.exists("inventario_json.json"):
        with open("inventario_json.json", "r") as arq_json:
            inventario = json.load(arq_json)
            return inventario
    else:
        inventario = {}
        return inventario
    
def menu():
    opcao = 0
    while opcao not in range(1, 3):
        opcao = int(input("Digite: \n<1> para registrar ativo\n<2> para exibir ativos armazenados\nOpção "))
    return opcao

def registra_ativo(inventario):
    resposta = "S"
    while resposta == "S":
        inventario[input("Digite o número patrimonial: ")] = [input("Digite a data da última atualização: "), input("Digite a descrição: "), input("Digite o departamento: ")]
        resposta = input("Digite <S> para continuar: ").upper()

def gravar_arquivo(inventario):
    with open("inventario_json.json", "w") as arq_json:
        json.dump(inventario, arq_json)
    print("JSON gerado!")

def exibir_arquivo(inventario):
    for dado in inventario.values():
                print("Data: ", dado[0])
                print("Descrição: ", dado[1])
                print("Departamento: ", dado[2])
                print("\n")