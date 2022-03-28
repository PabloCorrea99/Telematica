import socket
import os
import tqdm
from pathlib import Path
import ast
# device's IP address
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 8000
# receive 4096 bytes each time
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"

def startSockets():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((SERVER_HOST, SERVER_PORT))

    s.listen(4)
    print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

    client_socket, address = s.accept() 

    print(f"[+] {address} is connected.")

    received = client_socket.recv(BUFFER_SIZE).decode()
    msg = received.split(SEPARATOR)
    if msg[0] == "PUT":
        processFile(msg[1],msg[2], client_socket)
    elif msg[0] == "GET":
        sendFile(msg[1], client_socket)
    elif msg[0] == "EXIT":
        exit(0)
    elif msg[0] == "DELETE":
        pass

    s.close()

def processFile(filename, filesize, client_socket):
    print("NODO1: ",filename, filesize)
    try:
        filename_direction = "Almacenamiento/"+os.path.basename(filename)
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

            f.close()
        replicate(filename, filesize, filename_direction)
    
    except Exception as e:
        print(e)

def sendFile(filename, client_socket):
    files_list = ast.literal_eval(filename)
    print("ESTE ES EL ACRHIVO", files_list[0])
    try:
        for file in files_list:
            filename_direction = "Almacenamiento/" + os.path.basename(file)
            with open(filename_direction, "rb") as f:
                while True:
                    # read the bytes from the file
                    bytes_read = f.read(BUFFER_SIZE)
                    if not bytes_read:
                        # file transmitting is done
                        break
                    # we use sendall to assure transimission in 
                    # busy networks
                    client_socket.sendall(bytes_read)
                f.close()
    except Exception as e:
        print(e)
    
def replicate(filename, filesize, filename_direction):
    method = "PUT"
    print("DIRECCION PARA REPLICAR ", filename_direction)
    print(filename, filesize, filename_direction)
    replicate_nodes = [{"port":8004, "node":"ReplicacionNodo1/"}, {"port":8005, "node":"ReplicacionNodo1/"}]
    host = "127.0.0.1"
    for replica in replicate_nodes:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(f"[+] Connecting to {host}:{replica['port']}")
        s.connect((host, replica['port']))
        print("[+] Connected.")
        print(f"{method}{SEPARATOR}{filename}{SEPARATOR}{filesize}{SEPARATOR}")
        s.send(f"{method}{SEPARATOR}{filename}{SEPARATOR}{filesize}{SEPARATOR}{replica['node']}{SEPARATOR}".encode())
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

def startServer():   
    while True:
        startSockets()

startServer()