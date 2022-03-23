# Importar la biblioteca de sockets: 
import socket 
 # Crear un socket: 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 # Establecer una conexión: 
s.connect(('127.0.0.1', 9999)) 
 # Recibir mensaje de bienvenida: 
print(s.recv(1024).decode('utf-8')) 
for data in [b'Michael', b'Tracy', b'Sarah']: 
    # Enviar datos: 
    s.send(data) 
    print(s.recv(1024).decode('utf-8')) 
    
s.send(b'exit') 
s.close()