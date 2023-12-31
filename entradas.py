import base64, os

def menu():
  opcao = int(input("ESCOLHA UMA OPÇÃO\n=========================\n"
            "1 - Cifrar [AES]\n"
            "2 - Decifrar [AES]\n"
            "3 - Cifrar [AES/CTR]\n"
            "4 - Decifrar [AES/CTR]\n"
            "5 - Cifrar Arquivo ou Imagem [AES/CTR]\n"
            "6 - Decifrar Arquivo ou Imagem [AES/CTR]\n"
            "-------------------------\n"))
  return opcao

def mensagem():
  return input("Digite a mensagem: ")

def chaveCifra():
  chave = input("Digite uma chave (deve ser uma string hexadecimal de 32 caracteres), ou deixe em branco se quiser uma chave aleatória: ")
  if chave == "":
      chave = os.urandom(16)
      chave = str(chave.hex())
  print("\n\nSALVE SUA CHAVE\n=============================\n",
         chave,"\n-----------------------------\n")
  return chave

def rodadas():
    rodadas = input("Digite o número de rodadas, ou deixe em branco para utilizar o padrão: ")
    if rodadas == "":
        rodadas = 10
    return int(rodadas)

def chaveDecifra():
  return input("Digite uma chave (deve ser uma string hexadecimal de 32 caracteres): ")

def nonce():   
  nonce = input("Digite o vetor de inicialização (deve ser uma string hexadecimal de 32 caracteres), ou deixe em branco se quiser gerar um aleatório: ")
  if nonce == "":
    nonce = os.urandom(16)
    nonce = str(nonce.hex())
  print("\n\nSALVE SEU VETOR DE INICIALIZAÇÃO\n=============================\n",
         nonce,"\n-----------------------------\n")
  return nonce


def nonceDes():   
  nonce = input("Digite o vetor de inicialização (deve ser uma string hexadecimal de 32 caracteres: ")
  return nonce


def caminho():
  return input("Digite o caminho do arquivo: ")

def abreArquivo(caminho):
  try:
    with open(caminho, "rb") as arquivo:
      data = base64.b16encode(arquivo.read())
      data = str(data,"ascii").lower()
      return data       
  except Exception as e:
      print(f"Não foi possível ler o arquivo: {e}")


