import socket
import threading
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Puerto de escucha vinculante: 
s.bind(('127.0.0.1', 9999))
s.listen (5) #Liste, el parámetro pasado especifica el número máximo de conexiones en espera
print('Waiting for connection...')

def tcplink(sock, addr): 
    print('Accept new connection from %s:%s...' % addr) 
    sock.send(b'Welcome!') 
    while True: 
        data = sock.recv(1024) 
        time.sleep(1) 
        if not data or data.decode('utf-8') == 'exit': 
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8')) 
    sock.close() 
    print('Connection from %s:%s closed.' % addr)

while True: 
         # Aceptar una nueva conexión: 
    sock, addr = s.accept() 
         # Cree un nuevo hilo para manejar conexiones TCP:
    t = threading.Thread(target=tcplink, args=(sock, addr)) 
    t.start()

