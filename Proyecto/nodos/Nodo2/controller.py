import socket
import os
import tqdm
from pathlib import Path

# device's IP address
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 8001
# receive 4096 bytes each time
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"

def startServer():

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
        pass

    s.close()

def processFile(filename, filesize, client_socket):

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
        f.close()
    replicate(filename, filesize, filename_direction)

def replicate(filename, filesize, filename_direction):
    replicate_nodes = [8003, 8005]
    host = "127.0.0.1"
    for port in replicate_nodes:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(f"[+] Connecting to {host}:{port}")
        s.connect((host, port))
        print("[+] Connected.")
        s.send(f"PUT{SEPARATOR}{filename}{SEPARATOR}{filesize}".encode())
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

startServer()