import pandas as pd
import os

#-Funções para importar os arquivos
#-------------------------------------------//
def arq_csv(arquivo):
    df = pd.read_csv(arquivo, sep = ';')
    return df

def arq_excel(arquivo):
    df = pd.read_excel(arquivo)
    return df
#-------------------------------------------//


def filtroQuebra():

     while True:
        try:
            #Recebendo entrada do usuário para identificar o arquivo.
            arquivo_user = input('Digite apenas o nome do arquivo: ')

            #Recebendo arquivo no dataframe.
            excel = arq_excel('{}.xls'.format(arquivo_user))

            #Renomeando as colunas.
            excel.columns = ['ID', 'PRODUTO', 'QUANTIDADE', 'TOTALCUSTO']

            #Convertendo a coluna "TOTAL CUSTO" em float.
            excel[['TOTALCUSTO']].astype(float)

            #Agrupando por Produto, somando os valores e classificando em ordem decrescente.
            df = excel.groupby(by =['ID', 'PRODUTO']).sum().sort_values(by = ['TOTALCUSTO'], ascending=False)

            #Salvando o arquivo.
            return df.to_excel('Resultado.xls')

        except FileNotFoundError:
            print('\n ERROR. Arquivo não encontrado. \
            \n\n Possíveis erros: \n 1. Nome do arquivo incorreto. \
            \n 2. Arquivo não esta presente na pasta \
            \n 3. Digitando o nome do arquivo junto com a extensão \n')

    # Check para fechar o loop While.
        if os.path.isfile('Resultado.xls'):
            break
        else:
            continue


filtroQuebra()
