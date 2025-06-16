import hashlib

def calcula_hash(valor):
    hashlib.md5(valor.encode('utf-8')).hexdigest ()

nome_arquivo = input("Digite o nome o arquivo: ")

with open(nome_arquivo, "rb") as f:
        print( calcula_hash(f.read ()))

        texto = input("Digite um texto: ")
        print( calcula_hash(texto))
