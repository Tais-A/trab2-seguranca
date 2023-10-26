SBOX = [
    ["63", "7c", "77", "7b", "f2", "6b", "6f", "c5", "30", "01", "67", "2b", "fe", "d7", "ab", "76"],
    ["ca", "82", "c9", "7d", "fa", "59", "47", "f0", "ad", "d4", "a2", "af", "9c", "a4", "72", "c0"],
    ["b7", "fd", "93", "26", "36", "3f", "f7", "cc", "34", "a5", "e5", "f1", "71", "d8", "31", "15"],
    ["04", "c7", "23", "c3", "18", "96", "05", "9a", "07", "12", "80", "e2", "eb", "27", "b2", "75"],
    ["09", "83", "2c", "1a", "1b", "6e", "5a", "a0", "52", "3b", "d6", "b3", "29", "e3", "2f", "84"],
    ["53", "d1", "00", "ed", "20", "fc", "b1", "5b", "6a", "cb", "be", "39", "4a", "4c", "58", "cf"],
    ["d0", "ef", "aa", "fb", "43", "4d", "33", "85", "45", "f9", "02", "7f", "50", "3c", "9f", "a8"],
    ["51", "a3", "40", "8f", "92", "9d", "38", "f5", "bc", "b6", "da", "21", "10", "ff", "f3", "d2"],
    ["cd", "0c", "13", "ec", "5f", "97", "44", "17", "c4", "a7", "7e", "3d", "64", "5d", "19", "73"],
    ["60", "81", "4f", "dc", "22", "2a", "90", "88", "46", "ee", "b8", "14", "de", "5e", "0b", "db"],
    ["e0", "32", "3a", "0a", "49", "06", "24", "5c", "c2", "d3", "ac", "62", "91", "95", "e4", "79"],
    ["e7", "c8", "37", "6d", "8d", "d5", "4e", "a9", "6c", "56", "f4", "ea", "65", "7a", "ae", "08"],
    ["ba", "78", "25", "2e", "1c", "a6", "b4", "c6", "e8", "dd", "74", "1f", "4b", "bd", "8b", "8a"],
    ["70", "3e", "b5", "66", "48", "03", "f6", "0e", "61", "35", "57", "b9", "86", "c1", "1d", "9e"],
    ["e1", "f8", "98", "11", "69", "d9", "8e", "94", "9b", "1e", "87", "e9", "ce", "55", "28", "df"],
    ["8c", "a1", "89", "0d", "bf", "e6", "42", "68", "41", "99", "2d", "0f", "b0", "54", "bb", "16"]
]


INVSBOX = (
    ['52','09','6A','D5','30','36','A5','38','BF','40','A3','9E','81','F3','D7','FB'],
    ['7C','E3','39','82','9B','2F','FF','87','34','8E','43','44','C4','DE','E9','CB'],
    ['54','7B','94','32','A6','C2','23','3D','EE','4C','95','0B','42','FA','C3','4E'],
    ['08','2E','A1','66','28','D9','24','B2','76','5B','A2','49','6D','8B','D1','25'],
    ['72','F8','F6','64','86','68','98','16','D4','A4','5C','CC','5D','65','B6','92'],
    ['6C','70','48','50','FD','ED','B9','DA','5E','15','46','57','A7','8D','9D','84'],
    ['90','D8','AB','00','8C','BC','D3','0A','F7','E4','58','05','B8','B3','45','06'],
    ['D0','2C','1E','8F','CA','3F','0F','02','C1','AF','BD','03','01','13','8A','6B'],
    ['3A','91','11','41','4F','67','DC','EA','97','F2','CF','CE','F0','B4','E6','73'],
    ['96','AC','74','22','E7','AD','35','85','E2','F9','37','E8','1C','75','DF','6E'],
    ['47','F1','1A','71','1D','29','C5','89','6F','B7','62','0E','AA','18','BE','1B'],
    ['FC','56','3E','4B','C6','D2','79','20','9A','DB','C0','FE','78','CD','5A','F4'],
    ['1F','DD','A8','33','88','07','C7','31','B1','12','10','59','27','80','EC','5F'],
    ['60','51','7F','A9','19','B5','4A','0D','2D','E5','7A','9F','93','C9','9C','EF'],
    ['A0','E0','3B','4D','AE','2A','F5','B0','C8','EB','BB','3C','83','53','99','61'],
    ['17','2B','04','7E','BA','77','D6','26','E1','69','14','63','55','21','0C','7D'],
  )

Rcon = (
    "00", "01", "02", "04", "08", "10", "20", "40", "80", "1B", "36", "6C", "D8", "AB", "4D", "9A",
    "2F", "5E", "BC", "63", "C6", "97", "35", "6A", "D4", "B3", "7D", "FA", "EF", "C5", "91", "39",
  )


# Função de substituição S-Box
def sub_bytes(linha ,valor):

  if valor == 1: 
    substituicao = SBOX
  else:
    substituicao = INVSBOX

  resultado = []
  for item in linha:
    x = int(item[0],16)
    y = int(item[1],16)
    resultado.append(substituicao[x][y])

  return resultado

# Função de permutação de linhas
def shift_rows(estado,valor):
  if valor == 1:
    return [estado[0]] + [estado[i][i:] + estado[i][:i] for i in range(1,4)]
  else:
    return [estado[0]] + [estado[i][-i:] + estado[i][:-i] for i in range(1,4)] 
    

def gmul(a, b):
    p = 0
    for counter in range(8):
        if b & 1:
            p ^= a
        hi_bit_set = a & 0x80
        a <<= 1
        if hi_bit_set:
            a ^= 0x1b
        b >>= 1
    return p % 256

def mix_columns(estado):
  resultado = [[[] for _ in range(4)] for _ in range(4)]

  for i in range(4):
    coluna = [estado[j][i] for j in range(4)]
    
    column_hex = []
    for x in coluna:
      column_hex.append(int(x,16))
    
    resultado[0][i] = format((gmul(0x02, column_hex[0]) ^ gmul(0x03, column_hex[1]) ^ column_hex[2] ^ column_hex[3]) & 0xff, '02x')
    resultado[1][i] = format((column_hex[0] ^ gmul(0x02, column_hex[1]) ^ gmul(0x03, column_hex[2]) ^ column_hex[3]) & 0xff, '02x')
    resultado[2][i] = format((column_hex[0] ^ column_hex[1] ^ gmul(0x02, column_hex[2]) ^ gmul(0x03, column_hex[3])) & 0xff, '02x')
    resultado[3][i] = format((gmul(0x03, column_hex[0]) ^ column_hex[1] ^ column_hex[2] ^ gmul(0x02, column_hex[3])) & 0xff, '02x')

  return resultado

def rot_word(linha):
  return(linha[1:]+[linha[0]])

def transpose(matrix):
    return [list(row) for row in zip(*matrix)]

def key_expansion(chave, rodadas=10):
    len_word = (rodadas + 1) * 4
    lista = []
    for linha in chave:
      for item in linha:
        lista.append(item)
    
    word = [[[] for _ in range(len_word)] for _ in range(len_word)]
    for i in range(4):
      word[i] = chave[i]

    for i in range(4,len_word):
      temp = word[i-1]
      if i % 4 == 0:
        temp = rot_word(temp)
        temp = sub_bytes(temp,1)
        temp[0] = xor(temp[0], Rcon[i//4])

      aux = []
      for j in range(4):
        aux.append(xor(word[i-4][j],temp[j]))
      word[i]= aux
    
    chaves = []
    for i in range(0,len(word),4):
      grupo = transpose(word[i:i+4])
      chaves.append(grupo)

    return chaves

def xor(dado1, dado2):
  int1 = int(dado1,16)
  int2 = int(dado2,16)
  xor = int1 ^ int2
  resultado = format(xor, '02x')
  return resultado

def add_round_key(matrix, chave):
  resultado = [[[] for _ in range(4)] for _ in range(4)]
  for i in range(4):
      for j in range(4):
        resultado[i][j] = xor(matrix[i][j],chave[i][j])

  return resultado


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
  
def to_matrix(bloco):
  matrix = []
  cont = 0
  for i in range(4):
    linha = []
    for j in range(4):
      linha.append(bloco[cont]+bloco[cont+1])
      cont += 2
    matrix.append(linha)
  return matrix

def to_text(matrix):
  text = ""
  for linha in matrix:
    for item in linha:
      text += item
  return text

def estado_rod(matrix, chave):
  estado = []
  for linha in matrix:
    x = sub_bytes(linha,1)
    estado.append(x)
  estado = shift_rows(estado,1)
  estado = mix_columns(estado,1)
  estado = add_round_key(estado,chave)
  return estado

def estado_rod_inv(matrix, chave):
  estado = mix_columns(matrix,1)
  estado = []
  for linha in matrix:
    x = sub_bytes(linha,1)
    estado.append(x)
  estado = shift_rows(estado,1)
  estado = add_round_key(estado,chave)
  return estado
  
def aes(plaintext,valor,chave):
  matrix_text = transpose(to_matrix(plaintext))
  matrix_chave = to_matrix(chave)
  chave_expandida = key_expansion(matrix_chave)
  
  if valor == 1:

    #Primeira rodada
    estado = add_round_key(matrix_text, chave_expandida[0])
    rodadas = 10

    #Rodadas
    for i in range(1,rodadas):
      estado = estado_rod(estado,chave_expandida[i],valor)

    #Ultima rodadada
    cifra = []
    for linha in estado:
      x = sub_bytes(linha,1)
      cifra.append(x)
    cifra = shift_rows(cifra, valor)
    cifra = add_round_key(cifra,chave_expandida[-1])
    print(to_text(cifra))


  else:
    #Primeira rodada
    # estado = add_round_key(matrix_text,chave_expandida[-1])
    print(estado)
    print(chave_expandida[-1])

    rodadas = 10
    #Rodadas
    for i in range(rodadas-1,0,-1):
      print(i)
      estado = estado_rod_inv(estado,chave_expandida[i], valor)
      print(estado)
      print(chave_expandida[1])

    #Ultima rodadada
    # cifra = []
    # for linha in estado:
    #   x = sub_bytes(linha,2)
    #   cifra.append(x)
    # cifra = shift_rows(cifra,valor)
    # cifra = add_round_key(cifra,chave_expandida[-1])
    # print(to_text(cifra))





  

  
    
