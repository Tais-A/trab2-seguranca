from aes import aes


def cifrar_aes_ctr(texto, chave, nonce, rodadas):
    
    contador = int(nonce, 16)
    ciphertext = ""

    for i in range(0, len(texto), 32):
        bloco = texto[i:i+32]

        contador_str = format(contador, '032x')
        bloco_cifrado = aes(contador_str, 1, chave, rodadas) #criptografaa o contador com a chave usando a função aes

        if bloco_cifrado is not None:
            #faz operação xor entre bloco_cifrado e bloco
            resultado_xor = ''.join(format(int(a, 16) ^ int(b, 16), 'x') for a, b in zip(bloco_cifrado, bloco))

            ciphertext += resultado_xor #concatena o resultado xor ao texto cifrado

        contador += 1 #incrementa o contador para o próximo bloco
    
    return ciphertext
