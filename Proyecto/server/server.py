import socket
import os
import tqdm
from pathlib import Path
from HashTable import HashTable

# device's IP address
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 80
# receive 4096 bytes each time
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"
NODOS_DIR = Path(__file__).resolve().parent.parent

def startSockets(hash_table):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((SERVER_HOST, SERVER_PORT))

    s.listen(4)
    print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

    client_socket, address = s.accept() 

    print(f"[+] {address} is connected.")

    received = client_socket.recv(BUFFER_SIZE).decode()
    msg = received.split(SEPARATOR)
    if msg[0] == "PUT":
        processFile(msg[1],msg[2], client_socket, hash_table)
    elif msg[0] == "GET":
        getFile(msg[1], client_socket, hash_table)
    elif msg[0] == "EXIT":
        exit(0)
    elif msg[0] == "DELETE":
        pass

    s.close()

def processFile(filename, filesize, client_socket, hash_table):
    temp_key = filename.split(".")[0]
    node = hash_table.set_val(temp_key, filename)
    print(hash_table)
    filename_direction = os.path.basename(filename)
    filesize = int(filesize)
    progress = tqdm.tqdm(range(filesize), f"Receiving {filename_direction}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename_direction, "wb") as f:
        while True:
            # read 1024 bytes from the socket (receive)
            bytes_read = client_socket.recv(BUFFER_SIZE)
            if not bytes_read:    
                # nothing is received
                # file transmitting is done
                break
            # write to the file the bytes we just received
            f.write(bytes_read)
            # update the progress bar
            progress.update(len(bytes_read))
    #Decidir hacia que nodo enviar
    write_into_node(node, filename, filesize, filename_direction)

def getFile(filename, client_socket, hash_table):
    temp_key = filename.split(".")[0]
    filename, node = hash_table.get_val(temp_key)
    method = "GET"
    port, host = calc_node(node.value)# Decides which node to search the object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f"[+] Connecting to {host}:{port}")
    s.connect((host, port))
    print("[+] Connected.")
    s.send(f"{method}{SEPARATOR}{filename}{SEPARATOR}".encode())
    while True:
        bytes_read = s.recv(BUFFER_SIZE)
        if not bytes_read:    
            # nothing is received
            # file transmitting is done
            break
        client_socket.sendall(bytes_read)

    s.close()


def calc_node(node):
    host = SERVER_HOST
    if(node == "1"):
        port = 8000
    elif(node == "2"):
        port = 8001
    elif(node == "3"):
        port = 8002
    else:
        node = "Nodo1"
    #Solución temporal para el guardado
    #write_direction = str(NODOS_DIR) + r'\nodos'+ f"\{node}\Almacenamiento"
    return port, host

def write_into_node(node, filename, filesize, filename_direction):
    method = "PUT"
    port, host = calc_node(node.value)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f"[+] Connecting to {host}:{port}")
    s.connect((host, port))
    print("[+] Connected.")
    s.send(f"{method}{SEPARATOR}{filename}{SEPARATOR}{filesize}{SEPARATOR}".encode())
    with open(filename_direction, "rb") as f:
        while True:
            # read the bytes from the file
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                # file transmitting is done
                break
            # we use sendall to assure transimission in 
            # busy networks
            s.sendall(bytes_read)
        f.close()
    os.remove(filename_direction) 

def startServer():
    hash_table = HashTable(150)
    while True:
        startSockets(hash_table)

startServer()




