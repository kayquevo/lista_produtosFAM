# -*- coding: utf-8 -*-
"""

@author: prof. Gregorio
Disciplina: Estrutura de Dados
"""

"""
Integrantes do Grupo:
    RA  00352250    Gustavo Figueiredo Chapekausko:
    RA  00351864    Gustavo Stabile
    RA  00351772    Kayque Viana Oliveira
    RA  00353170    Mariana Pirani da Silva
    RA  00353171    Vinicius Joaquim da Silva

"""

PRODUTOS = "lista_produtos.txt"


def carregar():
    """
    Retorna uma string dos produtos e seus preços no formato:
        produto1 preco1 produto2 preco2 ... produtoN precoN
    Todas os produtos estão escrito em letras minúsculas.
    O teste do programa será feito com um arquivo com dados
        diferentes
    """
    print("\nCarregando os produtos do arquivo...\n")

    # inFile: file
    inFile = open(PRODUTOS, 'r')

    # dados: string
    dados = inFile.readline()
    inFile.close()
    return dados


'''
 As linhas seguintes são para testes, podem ser comentadas
 para o programa final
'''
#prod = carregar()
#print(prod)


def lista_tupla(aLista):
    '''
    Parameters
    ----------
    aLista : lista com os produtos

    Returns
    -------
    Uma Tupla com os produtos no formato
    ( (<str>produto1, <int>valor1), (<str>produto1, <int>valor1), ... )
    '''
    tupla = [] #Troquei "tupla" de tupla pra lista para usar o comando .append() pra adicionar valores mais facilmente na tupla
    for i in range(0, len(aLista), 2):
        produto = aLista[i]
        preco = int(aLista[i+1])
        tupla.append((produto, preco))

    return tuple(tupla)#Transformar "tupla" em tupla


def get_Produtos(aTupla):
    '''
    Parameters
    ----------
    aTupla : Uma Tupla com os produtos no formato
    ( (<str>produto1, <int>valor1), (<str>produto1, <int>valor1), ... )

    Returns
    -------
    uma tupla com 3 informações abaixo:
    1. O produto mais Barato (tupla): <produto> <valor>
    2. O produto mais caro   (tupla): <produto> <valor>
    3. Quantidade de Produtos Diferentes : <int>
    '''
    produto_mais_barato = aTupla[0]
    produto_mais_caro = aTupla[0]
    for produto in aTupla:
        if produto[1] < produto_mais_barato[1]:
            produto_mais_barato = produto
        if produto[1] > produto_mais_caro[1]:
            produto_mais_caro = produto

    quantidade = len(aTupla)

    return (produto_mais_barato, produto_mais_caro, quantidade)


def main():
    texto = carregar()
    lista = texto.split()
    dados = lista_tupla(lista)
    resultado = get_Produtos(dados)
    print("Produto mais barato: {}".format(resultado[0]))
    print("Produto mais caro: {}".format(resultado[1]))
    print("Quantidade de produtos: {}".format(resultado[2]))

main()
