from funcao import *

inventario = {}
continuar = 's'
while continuar == 's':

    opcao = menu()

    match opcao:
        case 1:
            registrar_ativo(inventario)
        case 2:
            persistir_em_arquivo(inventario)
        case 3:
            exibir()
    
    continuar = input("Deseja voltar ao menu? Entre com 'S': ").lower()