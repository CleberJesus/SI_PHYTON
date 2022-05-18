import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
    except socket.error as e:
        print("A conexão falhou!!!")
        print("Erro: {}".format(e))
        sys.exit()

    print("socket criado com sucesso!")

    hostAlvo = input("Digite o Host ou ip a ser conectado: ")
    portaAlvo = input("Digite a porta a ser conectada: ")

    try:
        s.connect((hostAlvo, int(portaAlvo)))
        print("Cliente tcp conectado com sucesso no Host: " + hostAlvo + " e na porta: " + portaAlvo)
        s.shutdown(2)
    except socket.error as e:
        print("A conexão falhou ao conectar no Host: " + hostAlvo + " - Porta: " + portaAlvo)
        print("Erro: {}".format(e))
        sys.exit()

if __name__ == "__main__":
    main()

