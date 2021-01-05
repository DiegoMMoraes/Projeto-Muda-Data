import os

# Descobrir nova data
database = input('Qual é a data que você quer botar nos arquivos? ')
data = database.strip()

# Abrir pasta com arquivos
pasta = input(r'Os arquivos estão em qual diretório? ')
os.chdir(pasta)

# Renomear Arquivos
for arquivo in os.listdir():
    #Dividide nome em -
    nomeArquivo = arquivo.split('-')


    #Cria novo nome
    novoNome = f'{data} -{nomeArquivo[1]}'

    os.rename(arquivo, novoNome)
