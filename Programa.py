import os

# Descobrir nova data
database = input('Qual é a data que você quer botar nos arquivos? ')
data = database.strip()

# Abrir pasta com arquivos
pasta = input(r'Os arquivos estão em qual diretório? ')
os.chdir(pasta)



for arquivo in os.listdir():
    x, extArquivo = os.path.splitext(arquivo)

    #Checa se é um arquivo do Excel e se o nome começa com 2
    if extArquivo == '.pdf' and arquivo[0] == '2':

        #Dividide a data do nome
        nomeAntigo = arquivo[11:]

        #Cria novo nome
        novoNome = f'{data} {nomeAntigo}'

        os.rename(arquivo, novoNome)
        print(f'O arquivo "{arquivo}" foi renomeado para "{novoNome}".')

