# Author: Thayna Santana ;)
# Github: https://www.github.com/thaynasantana
import os
import mimetypes
import shutil

# Nome do usuario do sistema
username = os.getenv('USERNAME')
diretorio = f'C:/Users/{username}/Downloads'
caminho = f'C:/Users/{username}/'
# Listar todos os arquivos
lista_arquivos = os.listdir(diretorio)
print('Listando arquivos do diretorio Downloads...')
###########  As funcoes!!! ################

# Funcao de mover images
def moveToPicture(picture):
    destino = os.path.join(caminho, "Pictures", arquivo)  # Construir o caminho completo do arquivo de destino
    shutil.move(os.path.join(diretorio, arquivo), destino)  # Mover o arquivo

# Funcao de mover videos
def moveToVideo(video):
    destino = os.path.join(caminho, "Videos", arquivo)  # Construir o caminho completo do arquivo de destino
    shutil.move(os.path.join(diretorio, arquivo), destino)  # Mover o arquivo

# Funcao de mover musicas/audios
def moveToMusic(music):
    destino = os.path.join(caminho, "Music", arquivo)  # Construir o caminho completo do arquivo de destino
    shutil.move(os.path.join(diretorio, arquivo), destino)  # Mover o arquivo

# Funcao de mover documentos
def moveToDocs(doc):
    destino = os.path.join(caminho, "Documents", arquivo)  # Construir o caminho completo do arquivo de destino
    shutil.move(os.path.join(diretorio, arquivo), destino)  # Mover o arquivo

# For Loop
for arquivo in lista_arquivos:
    # Selecionando cada arquivo com diretorio
    caminho_com_arquivo = os.path.join(diretorio, arquivo)
    # Pegando o tipo do arquivo e associando a variavel
    tipo, _ = mimetypes.guess_type(caminho_com_arquivo)
    print('Movendo os arquivos para cada pasta apropriada...')
    # Encaminhar pelo TIPO dos arquivos aos diretorios corretos
    if tipo:
        # PNG,JPEG, GIF -> Pictures/
        if tipo.startswith('image'):
            moveToPicture(arquivo)
        # MP4,AVI -> Movies/
        if tipo.startswith('video'):
            moveToVideo(arquivo)
        # PDF,TXT,DOCS,XLSX -> Documents/
        if tipo.startswith('text') or tipo == "application/pdf" or tipo == "application/rtf" or tipo == "application/vnd.ms-excel" or tipo == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" or tipo == "application/msword" or tipo == "application/vnd.openxmlformats-officedocument.presentationml.presentation" or tipo == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            moveToDocs(arquivo)
        # MP3 -> Music/
        if tipo.startswith('audio'):
            moveToMusic(arquivo)
    else:
        print(f'Não foi conseguimos entender o arquivo com extensao de {tipo}')


print('FIM.')