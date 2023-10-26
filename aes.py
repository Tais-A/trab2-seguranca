SBOX = [
    ["63", "7C", "77", "7B", "F2", "6B", "6F", "C5", "30", "01", "67", "2B", "FE", "D7", "AB", "76"],
    ["CA", "82", "C9", "7D", "FA", "59", "47", "F0", "AD", "D4", "A2", "AF", "9C", "A4", "72", "C0"],
    ["B7", "FD", "93", "26", "36", "3F", "F7", "CC", "34", "A5", "E5", "F1", "71", "D8", "31", "15"],
    ["04", "C7", "23", "C3", "18", "96", "05", "9A", "07", "12", "80", "E2", "EB", "27", "B2", "75"],
    ["09", "83", "2C", "1A", "1B", "6E", "5A", "A0", "52", "3B", "D6", "B3", "29", "E3", "2F", "84"],
    ["53", "D1", "00", "ED", "20", "FC", "B1", "5B", "6A", "CB", "BE", "39", "4A", "4C", "58", "CF"],
    ["D0", "EF", "AA", "FB", "43", "4D", "33", "85", "45", "F9", "02", "7F", "50", "3C", "9F", "A8"],
    ["51", "A3", "40", "8F", "92", "9D", "38", "F5", "BC", "B6", "DA", "21", "10", "FF", "F3", "D2"],
    ["CD", "0C", "13", "EC", "5F", "97", "44", "17", "C4", "A7", "7E", "3D", "64", "5D", "19", "73"],
    ["60", "81", "4F", "DC", "22", "2A", "90", "88", "46", "EE", "B8", "14", "DE", "5E", "0B", "DB"],
    ["E0", "32", "3A", "0A", "49", "06", "24", "5C", "C2", "D3", "AC", "62", "91", "95", "E4", "79"],
    ["E7", "C8", "37", "6D", "8D", "D5", "4E", "A9", "6C", "56", "F4", "EA", "65", "7A", "AE", "08"],
    ["BA", "78", "25", "2E", "1C", "A6", "B4", "C6", "E8", "DD", "74", "1F", "4B", "BD", "8B", "8A"],
    ["70", "3E", "B5", "66", "48", "03", "F6", "0E", "61", "35", "57", "B9", "86", "C1", "1D", "9E"],
    ["E1", "F8", "98", "11", "69", "D9", "8E", "94", "9B", "1E", "87", "E9", "CE", "55", "28", "DF"],
    ["8C", "A1", "89", "0D", "BF", "E6", "42", "68", "41", "99", "2D", "0F", "B0", "54", "BB", "16"]
]


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

xtime = lambda a: (((a << 1) ^ 0x1B) & 0xFF) if (a & 0x80) else (a << 1)


# Função de substituição S-Box
def sub_bytes(matrix):
  for i in range(4):
    for j in range(4):
      x = int(matrix[i][j][0],16)
      y = int(matrix[i][j][1],16)
      matrix[i][j] = SBOX[x][y]
  return matrix

# Função de permutação de linhas
def shift_rows(est):
  est[0][1], est[1][1], est[2][1], est[3][1] = est[1][1], est[2][1], est[3][1], est[0][1]
  est[0][2], est[1][2], est[2][2], est[3][2] = est[2][2], est[3][2], est[0][2], est[1][2]
  est[0][3], est[1][3], est[2][3], est[3][3] = est[3][3], est[0][3], est[1][3], est[2][3]
  return est


def mix_columns(state):
  for i in range(4):
    s0 = int(state[i][0],16)
    s1 = int(state[i][1],16)
    s2 = int(state[i][2],16)
    s3 = int(state[i][3],16)

    state[i][0] = (2 * s0) ^ (3 * s1) ^ s2 ^ s3
    state[i][1] = s0 ^ (2 * s1) ^ (3 * s2) ^ s3
    state[i][2] = s0 ^ s1 ^ (2 * s2) ^ (3 * s3)
    state[i][3] = (3 * s0) ^ s1 ^ s2 ^ (2 * s3)

  return state


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
            temp = [SBOX[b] for b in temp]

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


def to_text(data):
  text = ""
  for k in range(len(data)):
    matrix = data[k]
    for i in range(4):
      for j in range(4):
        try:
          text += format(matrix[i][j], '02x')
        except:
          text += matrix[i][j]

  return text

#AddRoundKey
#SubBytes
#shift_rows
#AddRoundKwy



def change_key(chave):
  round_key = to_matrix(chave)
  for i in range(4, 4*11):
    round_key.append([])
    if i % 4 == 0:
      byte = round_key[i - 4][0] ^ S_BOX[round_key[i-1][1]] ^ Rcon[i/4]
      round_key[i].append(byte)
      for j in range(1,4):
        byte = round_key[i - 4][j] ^ S_BOX[round_key[i-1][(j + 1) % 4]]
        round_key[i].append(byte)
    else:
      byte = round_key[i - 4][j] ^ round_key[i-1][j]
      round_key[i].append(byte)


def encrypt(matrix, chave):
  dado = sub_bytes(matrix)
  dado = shift_rows(dado)
  dado = mix_columns(dado)
  print(dado)


  # data = to_matrix(mensagem)
  # print(data)
  # text = to_text(data)
  # print(text)
  pass

def descrypt(arquivo):
  #todo
  pass

def to_matrix(bloco):
  matrix = []
  cont = 0
  for i in range(4):
    linha = []
    for j in range(4):
      linha.append(bloco[cont])
      cont += 1
    matrix.append(linha)
  print(matrix)
  return matrix

def divideBlocks(lista):
  blocos = []
  cont = 0 

  if len(lista) % 16 != 0:
    for i in range(16 -(len(lista) % 16)):
      lista.append('00')

  n = len(lista) // 16
  
  for i in range(n):
    bloco = []
    for j in range(16):
      bloco.append(lista[cont])
      cont+= 1
    blocos.append(bloco)
  return blocos
  
def breakString(mensagem):
  lista = []
  for c in range(0,len(mensagem),2):
    lista.append(mensagem[c]+mensagem[c+1])
  return lista

def aes(arquivo,valor,chave):
  if valor == 1:
    lista_hex = breakString(arquivo)
    blocos = divideBlocks(lista_hex)
    lista_matrix = []
    for bloco in blocos:     
      lista_matrix.append(to_matrix(bloco))
    for matrix in lista_matrix:
      encrypt(matrix, chave)
  else:
    descrypt(arquivo, chave)

  

  
    
