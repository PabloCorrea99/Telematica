import socket
import os
import tqdm
from pathlib import Path

# device's IP address
SERVER_HOST = "127.0.0.1"
REPLICATE_PORT = 8004
# receive 4096 bytes each time
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"

def startSockets():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((SERVER_HOST, REPLICATE_PORT))

    s.listen(4)
    print(f"[*] Listening as {SERVER_HOST}:{REPLICATE_PORT}")

    client_socket, address = s.accept() 

    print(f"[+] {address} is connected.")

    received = client_socket.recv(BUFFER_SIZE).decode()
    msg = received.split(SEPARATOR)
    if msg[0] == "PUT":
        processFile(msg[1],msg[2],msg[3], client_socket)
    elif msg[0] == "GET":
        pass
    elif msg[0] == "EXIT":
        exit(0)
    elif msg[0] == "DELETE":
        deleteFile(msg[1],msg[2], client_socket)


    s.close()

def processFile(filename, filesize,replication_dir, client_socket):
    print("REPLICATION ",filename, filesize)
    filename_direction = replication_dir+os.path.basename(filename)
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

def deleteFile(filename, replication_dir, client_socket):
    print("REPLICATION DELETION",filename)
    filename_direction = replication_dir+os.path.basename(filename)
    try:
        os.remove(filename_direction)
        client_socket.sendall(b"SE ELEMINO CORRECTAMENTE EN LA REPLICA")
    except Exception as e:
        print(e)

def startServer():   
    while True:
        startSockets()

startServer()