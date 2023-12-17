"""
- Qual o total de voos internacionais que partiram do aeroporto de Logan no
ano de 2014?
- Quando (mês/ano) ocorreu o maior trânsito de passageiros no aeroporto de
Logan?
- Qual o total de passageiros que passaram pelo aeroporto de Logan, no ano
que for especificado pelo usuário?
- Qual o mês que possui a maior média da diária de um hotel, com base no
ano especificado pelo usuário?
"""

# ano [0], mes [1], passageiros [2], voos-internacionais [3]
# ocupacao-hotel [4], media-diaria-hotel[5], empregos[6]
# taxa-desemprego [7]

with open("economic-indicators.csv", "r") as boston:
    total_voos = 0
    total_voos_user = 0
    ano_user = int(input("Entre com o ano que deseja verificar o trânsito: "))
    for linha in boston.readlines() [1:-1]:
        if linha.split(',')[0] == '2014':
            #soma com a quantidade de voos que partiram de Logan
            total_voos = total_voos + int(linha.split(",")[3])
        if int(linha.split(',')[0]) == ano_user:
            total_voos_user = total_voos_user + int(linha.split(',')[3])
    print("O total de vôos internacionais que partiram do aeroporto de Logan em %d é de %d" %(ano_user, total_voos_user))
    print("O total de vôos internacionais que partiram do aeroporto de Logan em 2014 é de ", total_voos)

with open("economic-indicators.csv", "r") as boston:
    transito = []
    ano = 0
    mes = 0
    maior = 0
    for linha in boston.readlines() [1:-1]:
        transito.append(linha.split(",")[2])
        if transito.index(max(transito)):
            print(mes, ano)
            ano = int(linha.split(',')[0])
            mes = int(linha.split(',')[1])
    print("O mês e ano de maior trânsito no aeroporto é %d/%d" %(mes, ano))