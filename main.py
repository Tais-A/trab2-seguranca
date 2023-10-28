import base64

from aes import aes
from aes_ctr import cifrar_aes_ctr


def open_file(file_path):
    try:
        with open(file_path, "rb") as file:
          data = base64.b16encode(file.read())
          data = str(data,"ascii").lower()
          return data       
    except Exception as e:
        print(f"Não foi possível ler o arquivo: {e}")
        return "text-short.txt"





opcao = int(input("ESCOLHA UMA OPÇÃO\n=========================\n"
            "1 - Cifrar [AES]\n"
            "2 - Decifrar [AES]\n"
            "3 - Cifrar [AES/CTR]\n"
            "4 - Decifrar [AES/CTR]\n"
            "-------------------------\n"))

#caminho_arquivo = input("Informe o caminho do arquivo: ")

# arquivo = open_file(caminho_arquivo)
# print(arquivo)
# chave = "91a0546ab37caff0"
# chave = chave.lower()
# aes(arquivo, 1, chave)
#plaintext = "43747273726f6f737920636f70506572"
#plaintext = "0123456789abcdeffedcba9876543210"
#plaintext="ff0b844a0853bf7c6934ab4364148fb9"


#############################################plaintext="0123456789abcdeffedcba9876543210"
#chave = "6d11dbca880bf900a33e86937afd41fd"
#chave = "ead27321b58dbad22312bf5607f8d292f"
############################################chave = "0f1571c947d9e8590cb7add6af7f6798"
#######aes(plaintext, 1, chave)
#######################################nonce = "0f0e0d0c0b0a09080706050403020100"


plaintext="0123456789abcdeffedcba9876543210"
#plaintext = input("Informe a mensagem: ")

chave = "0f1571c947d9e8590cb7add6af7f6798"
#chave = input("Informe a chave: ")


if opcao == 1:
    print("\n\nCIFRAR-AES\n")
    print("CIFRADO: ", aes(plaintext, opcao, chave))
    
elif opcao == 2:
    print("\n\nCIFRAR-AES\n")
    print("DECIFRADO: ", aes(plaintext, opcao, chave))

elif opcao == 3:
    print("\n\nCIFRAR-AES/CTR\n")
    nonce = "0f0e0d0c0b0a09080706050403020100"
    #nonce = input("Informe o nonce (deve ser uma string hexadecimal de 32 caracteres): ")

    print("CIFRADO (AES-CTR):", cifrar_aes_ctr(plaintext, chave, nonce))

elif opcao == 4:
    print("\n\nDECIFRAR-AES/CTR\n")
    nonce = "0f0e0d0c0b0a09080706050403020100"
    #nonce = input("Informe o nonce (deve ser uma string hexadecimal de 32 caracteres): ")
    print("DECIFRADO (AES-CTR):", cifrar_aes_ctr(plaintext, chave, nonce))

