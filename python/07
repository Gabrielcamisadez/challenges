import socket

HOST = "temperance.hackmyvm.eu"
PORT = 9988

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    print('Receiving Intro')
    data = s.recv(1024)
    print(data)

    s.send(b'levelx07')

    print('Receiving first challenge.')
    data2 = s.recv(1024)
    print(data2)

    # convert 
    hex_str = data2.decode('utf-8')
    result = bytearray.fromhex(hex_str).decode()
    
    # send 
    se = result.encode('utf-8')
    s.send(se)
    
    print('recv flag')
    data4 = s.recv(1024)
    print(data4)

    






