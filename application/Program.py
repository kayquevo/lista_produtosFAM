# -*- coding: utf-8 -*-
"""
@author: prof. Gregorio
Disciplina: Estrutura de Dados
"""
"""
Integrantes do Grupo:
00351772 Kayque Viana Oliveira
"""

PRODUTOS = "lista_produtos.txt"

def carregar():
    try:
        print("\nCarregando os produtos do arquivo...\n")
        inFile = open(PRODUTOS, 'r', encoding='utf-8')

        dados = inFile.read()
        inFile = inFile.read()

        dados_limpos = dados.lower().strip()

        return dados_limpos
    except FileNotFoundError:
        print("Erro: arquivo não encontrado!")
        return ""
    
prod = carregar()
print(prod)


        
            
    