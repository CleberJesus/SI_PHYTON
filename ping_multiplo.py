import os
import time

with open('hosts.txt') as file:
    dump = file.read()

    dump = dump.splitlines()

for ip in dump:
    print('verificando o ip: {}'.format(ip))
    print('-' * 60)
    os.system('ping -n 2 {}'.format(ip))
    print('-' * 60)
    time.sleep(2)

