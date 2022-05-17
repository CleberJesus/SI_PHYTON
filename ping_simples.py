import os # importar a biblioteca os integra os programas e recursos do sistema operacional

print('#' * 60) # imprimindo o sustenido 60 vezes
# criando uma variável onde o usuário vai digitar o ip ou host
ip_ou_host = input("Digite um IP ou host a ser verificado: ")
print('-' * 60) # imprimindo o traço 60 vezes
#chamando o system da biblioteca os - comando ping e formatando a variável digitada pelo usuário
os.system('ping -n 6 {}'.format(ip_ou_host))
print('-' * 60) # imprimindo o traço 60 vezes


