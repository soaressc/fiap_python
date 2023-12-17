from Funcoes_JSON import *

inventario = criar_inventario()
resposta = "s"
opcao = menu()

while opcao in range(1, 3):
    match opcao:
        case 1:
            registra_ativo(inventario)
            gravar_arquivo(inventario)
        case 2:
            exibir_arquivo(inventario)
    opcao = menu()