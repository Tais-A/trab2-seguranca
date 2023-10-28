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
    ['52','09','6a','d5','30','36','a5','38','bf','40','a3','9e','81','f3','d7','fb'],
    ['7c','e3','39','82','9b','2f','ff','87','34','8e','43','44','c4','de','e9','cb'],
    ['54','7b','94','32','a6','c2','23','3d','ee','4c','95','0b','42','fa','c3','4e'],
    ['08','2e','a1','66','28','d9','24','b2','76','5b','a2','49','6d','8b','d1','25'],
    ['72','f8','f6','64','86','68','98','16','d4','a4','5c','cc','5d','65','b6','92'],
    ['6c','70','48','50','fd','ed','b9','da','5e','15','46','57','a7','8d','9d','84'],
    ['90','d8','ab','00','8c','bc','d3','0a','f7','e4','58','05','b8','b3','45','06'],
    ['d0','2c','1e','8f','ca','3f','0f','02','c1','af','bd','03','01','13','8a','6b'],
    ['3a','91','11','41','4f','67','dc','ea','97','f2','cf','ce','f0','b4','e6','73'],
    ['96','ac','74','22','e7','ad','35','85','e2','f9','37','e8','1c','75','df','6e'],
    ['47','f1','1a','71','1d','29','c5','89','6f','b7','62','0e','aa','18','be','1b'],
    ['fc','56','3e','4b','c6','d2','79','20','9a','db','c0','fe','78','cd','5a','f4'],
    ['1f','dd','a8','33','88','07','c7','31','b1','12','10','59','27','80','ec','5f'],
    ['60','51','7f','a9','19','b5','4a','0d','2d','e5','7a','9f','93','c9','9c','ef'],
    ['a0','e0','3b','4d','ae','2a','f5','b0','c8','eb','bb','3c','83','53','99','61'],
    ['17','2b','04','7e','ba','77','d6','26','e1','69','14','63','55','21','0c','7d'],
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

def mix_columns(estado, valor):
  aux = [[[] for _ in range(4)] for _ in range(4)]

  for i in range(4):
    coluna = [estado[j][i] for j in range(4)]
    
    column_hex = []
    for x in coluna:
      column_hex.append(int(x,16))

    if valor == 1:
      aux[0][i] = (gmul(0x02, column_hex[0]) ^ gmul(0x03, column_hex[1]) ^ column_hex[2] ^ column_hex[3]) & 0xff
      aux[1][i] = (column_hex[0] ^ gmul(0x02, column_hex[1]) ^ gmul(0x03, column_hex[2]) ^ column_hex[3]) & 0xff
      aux[2][i] = (column_hex[0] ^ column_hex[1] ^ gmul(0x02, column_hex[2]) ^ gmul(0x03, column_hex[3])) & 0xff
      aux[3][i] = (gmul(0x03, column_hex[0]) ^ column_hex[1] ^ column_hex[2] ^ gmul(0x02, column_hex[3])) & 0xff
    
    else:
      aux[0][i] = (gmul(0x0e, column_hex[0]) ^ gmul(0x0b, column_hex[1]) ^ gmul(0x0d, column_hex[2]) ^ gmul(0x09, column_hex[3])) & 0xff
      aux[1][i] = (gmul(0x09, column_hex[0]) ^ gmul(0x0e, column_hex[1]) ^ gmul(0x0b, column_hex[2]) ^ gmul(0x0d, column_hex[3])) & 0xff
      aux[2][i] = (gmul(0x0d, column_hex[0]) ^ gmul(0x09, column_hex[1]) ^ gmul(0x0e, column_hex[2]) ^ gmul(0x0b, column_hex[3])) & 0xff
      aux[3][i] = (gmul(0x0b, column_hex[0]) ^ gmul(0x0d, column_hex[1]) ^ gmul(0x09, column_hex[2]) ^ gmul(0x0e, column_hex[3])) & 0xff
  
  resultado = [[[] for _ in range(4)] for _ in range(4)]
  for i in range(4):
    for j in range(4):
      resultado[i][j] = format(aux[i][j],'02x')

  return resultado

def rot_word(linha):
    return(linha[1:]+[linha[0]])
    #return [str(linha[1])] + [linha[0]] 


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
      #grupo = word[i:i+4]
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
            resultado[i][j] = xor(matrix[i][j], chave[i][j])
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
  estado = shift_rows(matrix,2)
  dado = []
  for linha in estado:
    x = sub_bytes(linha,2)
    dado.append(x)
  estado = add_round_key(chave, dado)
  estado = mix_columns(estado,2)
  
  return estado
  
def aes(plaintext,valor,chave):
  matrix_text = transpose(to_matrix(plaintext))
  matrix_chave = to_matrix(chave)
  chave_expandida = key_expansion(matrix_chave)
  rodadas = 10
  
  if valor == 1:

    #Primeira rodada
    estado = add_round_key(matrix_text, chave_expandida[0])

    #Rodadas
    for i in range(1,rodadas):
      estado = estado_rod(estado,chave_expandida[i])

    #Ultima rodadada
    cifra = []
    for linha in estado:
      x = sub_bytes(linha,1)
      cifra.append(x)
    cifra = shift_rows(cifra, valor)
    cifra = add_round_key(cifra,chave_expandida[-1])
    return (to_text(transpose(cifra))) 

  elif valor == 2:

    #Primeira rodada
    estado = add_round_key(chave_expandida[-1],matrix_text)

    #Rodadas
    for i in range(rodadas-1,0,-1):
      print(i)
      estado = estado_rod_inv(estado,chave_expandida[i])
      print('estado', to_text(estado))


    #Ultima rodadada
    estado = shift_rows(estado,2)
    texto = []
    for linha in estado:
       x = sub_bytes(linha,2)
       texto.append(x)

    texto = add_round_key(texto,chave_expandida[0])
    return (to_text(transpose(texto)))



  
