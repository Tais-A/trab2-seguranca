
S_BOX = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16
  )


InvSbox = (
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,
  )

Rcon = (
    0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36, 0x6C, 0xD8, 0xAB, 0x4D, 0x9A,
    0x2F, 0x5E, 0xBC, 0x63, 0xC6, 0x97, 0x35, 0x6A, 0xD4, 0xB3, 0x7D, 0xFA, 0xEF, 0xC5, 0x91, 0x39,
  )


# Função de substituição S-Box
def sub_bytes(state):
  for i in range(4):
    for j in range(4):
      state[i][j] = S_BOX[state[i][j]]

# Função de permutação de linhas
def shift_rows(state):
  for i in range(4):
    state[i] = state[i][i:] + state[i][:i]

def mix_columns(state):
  for i in range(4):
    s0 = state[i][0]
    s1 = state[i][1]
    s2 = state[i][2]
    s3 = state[i][3]

    state[i][0] = (2 * s0) ^ (3 * s1) ^ s2 ^ s3
    state[i][1] = s0 ^ (2 * s1) ^ (3 * s2) ^ s3
    state[i][2] = s0 ^ s1 ^ (2 * s2) ^ (3 * s3)
    state[i][3] = (3 * s0) ^ s1 ^ s2 ^ (2 * s3)



def key_expansion(key, round):
    key_schedule = [0] * 11  # AES-128 requer 11 rodadas com 16 bytes em cada rodada

    # Copie a chave mestra para a primeira palavra-chave do agendamento de chave
    key_schedule[0] = key

    for i in range(1, 11):
        temp = list(key_schedule[i - 1])

        # Etapa de rotação (apenas para a primeira palavra-chave de cada rodada)
        if i % 4 == 0:
            temp = temp[1:] + [temp[0]]

            # Substituição de bytes (usando a tabela S-box)
            temp = [S_BOX[b] for b in temp]

            # Realizar operação XOR com a rodada do Rcon
            temp[0] ^= RCON[i // 4]

        # Realizar operação XOR com a palavra anterior
        key_schedule[i] = [key_schedule[i - 1][j] ^ temp[j] for j in range(16)]

    return key_schedule[round]

# def cifra:

#   # Chave de 128, 192 ou 256 bits (16, 24 ou 32 bytes)
#   key = get_random_bytes(16)  # 128 bits (16 bytes)
#   iv = get_random_bytes(16)   # Vetor de inicialização de 128 bits (16 bytes)

#   #todo
#   mensagem = input()
#   rodadas = input()
#   cifra = addRoundKey(mensagem)
#   for i in range(rodadas):
#     subBytes(mensagem)
#     shiftRows(mensagem)
#     mixColumns(mensagem)
#     addRoundKey(mensagem)

#   print(mensagem)
def aes_round(state, round_key):
    sub_bytes(state)
    shift_rows(state)
    mix_columns(state)
    round_key = key_expansion(round_key, round)
    for i in range(4):
        for j in range(4):
            state[i][j] ^= round_key[i][j] 

def aes_encrypt(plaintext, key, num_rounds=10):
    state = [[plaintext[i + j * 4] for i in range(4)] for j in range(4)]
    round_key = key_expansion(key, 0)
    for round in range(1, num_rounds):
        aes_round(state, round_key)
    sub_bytes(state)
    shift_rows(state)
    round_key = key_expansion(key, num_rounds)
    for i in range(4):
        for j in range(4):
            state[i][j] ^= round_key[i][j]
    # Retorna a matriz de estado como o texto cifrado
    return [state[i][j] for i in range(4) for j in range(4)]


def to_hex(text):
  string_hex = []
  for i in text:
    string_hex.append(hex(ord(i)))
  return(string_hex)

def to_matrix(text):
  state = []
  
  if len(text) % 16 != 0:
    aux = 16 - (len(text) % 16)
    for i in range(aux):
      text += " "

  n = len(text) // 16

  for k in range(n):
    matriz = []
    # todo percorrer texto inteiro
    for i in range(16):
    # two hex characters == 1 byte
      byte = int(t[i*2:i*2+2], 16)
      if i % 4 == 0:
        matriz.append([byte])
      else:
        matriz[i // 4].append(byte)
    state.append(matriz)
       

  return state

def to_text(data):
  text = ""
  for k in range(len(data)):
    matrix = data[k]
    for i in range(4):
      for j in range(4):
        text += format(matrix[i][j], '02x')

  return text

# def addPad(data):
#   bits = []
#   while(True):
#     if(len(data) > bytes):
#       bits.append(data[:bytes])
#       data = data[bytes:]
#     else:
#       space = bytes-len(data)
#       bits.append(data+chr(space)*space)
#       break
#   return bits


def encrypt(mensagem, chave):
  print(mensagem)
  data = to_matrix(mensagem)
  print(data)
  text = to_text(data)
  print(text)
  pass

def descrypt(arquivo):
  #todo
  pass

def aes(arquivo,valor,chave):
  if valor == 1:
    encrypt(arquivo, chave)
  else:
    descrypt(arquivo, chave)

  

  
    
