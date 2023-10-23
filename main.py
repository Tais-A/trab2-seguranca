import base64

from aes import aes

def open_file(file_path):
    try:
        with open(file_path, "rb") as file:
          data = base64.b16encode(file.read())
          data = str(data, "utf-8").lower()
          return data       
    except Exception as e:
        print(f"Não foi possível ler o arquivo: {e}")
        return None


caminho_arquivo = input("Informe o caminho do arquivo: ")

arquivo = open_file(caminho_arquivo)
chave = 0x2b7e151628aed2a6abf7158809cf4f3c
aes(arquivo, 1, chave)
