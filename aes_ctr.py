from aes import aes

def remove_zeros(string): #remove zeros extras que aparecem à esquerda de cada caractere
    nova_string = ""
    for i in range(len(string)):
        if i % 2 == 0:
            nova_string += string[i+1]
    return nova_string

def cifrar_aes_ctr(texto, chave, nonce):
    
    contador = int(nonce, 16)
    ciphertext = ""

    for i in range(0, len(texto), 32):
        bloco = texto[i:i+32]

        contador_str = format(contador, '032x')
        bloco_cifrado = aes(contador_str, 1, chave) #criptografaa o contador com a chave usando a função aes

        if bloco_cifrado is not None:
            #faz operação xor entre bloco_cifrado e bloco
            resultado_xor = ''.join(format(int(a, 16) ^ int(b, 16), '02x') for a, b in zip(bloco_cifrado, bloco))

            ciphertext += resultado_xor #concatena o resultado xor ao texto cifrado

        contador += 1 #incrementa o contador para o próximo bloco
    
    return remove_zeros(ciphertext)
