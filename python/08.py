# EN
# Codename: levelx08
# Mission: In this mission you will receive 2 numbers, you must return the result of adding both.

import socket

HOST = "temperance.hackmyvm.eu"
PORT = 9988

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    print('Receiving Intro')
    data = s.recv(1024)
    print(data)

    s.send(b'levelx08')

    print('Receiving first challenge.')
    data2 = s.recv(1024)
    print(data2)

    numbers = data2.decode('utf-8')
    print(numbers)
    splited = numbers.split()
    n1 = int(splited[0])
    n2 = int(splited[1])
    
    # adding numbers
    result = str(n1 + n2)
    print(result)

    # sending back
    to_send = result.encode('utf-8')
    s.send(to_send)    
    

    print('recv flag')
    data4 = s.recv(1024)
    print(data4)

    





