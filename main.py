from aes import aes
from aes_ctr import cifrar_aes_ctr
import entradas


opcao = entradas.menu()

if opcao == 1:
    plaintext = entradas.mensagem()
    chave = entradas.chaveCifra()
    rodadas = entradas.rodadas()

    print("\n\nCIFRAR-AES\n")
    print("CIFRADO: ", aes(plaintext, opcao, chave, rodadas))
    
elif opcao == 2:
    plaintext = entradas.mensagem()
    chave = entradas.chaveDecifra()
    rodadas = entradas.rodadas()

    print("\n\nDECIFRAR-AES\n")
    print("DECIFRADO: ", aes(plaintext, opcao, chave, rodadas))


elif opcao == 3:
    plaintext = entradas.mensagem()
    chave = entradas.chaveCifra()
    rodadas = entradas.rodadas()
    nonce = entradas.nonce()

    print("\n\nCIFRAR-AES/CTR\n")
    print("CIFRADO (AES-CTR):", cifrar_aes_ctr(plaintext, chave, nonce, rodadas))


elif opcao == 4:
    plaintext = entradas.mensagem()
    chave = entradas.chaveDecifra()
    rodadas = entradas.rodadas()
    nonce = entradas.nonce()
    
    print("\n\nDECIFRAR-AES/CTR\n")
    print("DECIFRADO (AES-CTR):", cifrar_aes_ctr(plaintext, chave, nonce, rodadas))
    
elif opcao == 5:
    caminho = entradas.caminho()
    arquivo = entradas.abreArquivo(caminho)
    chave = entradas.chaveCifra()
    rodadas = entradas.rodadas()
    nonce = entradas.nonce()
    nome,formato = caminho.split('.',1)

    cifra = cifrar_aes_ctr(arquivo, chave, nonce, rodadas)

    cifra_byte = bytes.fromhex(cifra)
    nome_novo = nome + "-cifrado-"+str(rodadas)+"-rods." + formato

    with open(nome_novo, "wb") as arquivo:
        arquivo.write(cifra_byte)

    print("\n\nCIFRAR-ARQUIVO-AES/CTR\n")
    print("ARQUIVO SALVO COMO:", nome_novo)


elif opcao == 6:
    caminho = entradas.caminho()
    arquivo = entradas.abreArquivo(caminho)
    chave = entradas.chaveDecifra()
    rodadas = entradas.rodadas()
    nonce = entradas.nonce()
    nome,formato = caminho.split('.',1)

    cifra = cifrar_aes_ctr(arquivo, chave, nonce, rodadas)

    cifra_byte = bytes.fromhex(cifra)
    nome_novo = nome + "-decifrado-"+str(rodadas)+"-rods." + formato

    with open(nome_novo, "wb") as arquivo:
        arquivo.write(cifra_byte)

    print("\n\nCIFRAR-ARQUIVO-AES/CTR\n")
    print("ARQUIVO SALVO COMO:", nome_novo)


