# -*- coding: utf-8 -*-
"""
@author: prof. Gregorio
Disciplina: Estrutura de Dados
"""
"""
Integrantes do Grupo:
00351772 Kayque Viana Oliveira
"""

PRODUTOS = "application/lista_produtos.txt"

def carregar():
    try:
        print("\nCarregando os produtos do arquivo...\n")
        inFile = open(PRODUTOS, 'r', encoding='utf-8')

        dados = inFile.read()

        dados_limpos = dados.lower().strip()

        return dados_limpos
    except FileNotFoundError:
        print("Erro: arquivo não encontrado!")
        return ""
    
prod = carregar()


def lista_tupla(aLista):

    lista_dos_produtos = aLista.split()
    lista_de_pares = []

    for i in range(0, len(lista_dos_produtos), 2):
        produto = lista_dos_produtos[i]
        preco = int(lista_dos_produtos[i+1])

        lista_de_pares.append((produto, preco))
        
    tupla = tuple(lista_de_pares)
    
    return tupla

tup = lista_tupla(prod)
print(tup)


        
            
    