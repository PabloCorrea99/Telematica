import socket 
import os
from tkinter import SEPARATOR
import tqdm


SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096
host = "127.0.0.1"
port = 80

def sendFile():
    method = "PUT"
    filename = input("Type the archive Name: ")
    filesize = os.path.getsize(filename)
    print(f"[+] Connecting to {host}:{port}")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    print("[+] Connected.")
    s.send(f"{method}{SEPARATOR}{filename}{SEPARATOR}{filesize}{SEPARATOR}".encode())
    progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "rb") as f:
        while True:
            # read the bytes from the file
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                # file transmitting is done
                break
            # we use sendall to assure transimission in 
            # busy networks
            s.sendall(bytes_read)
            # update the progress bar
            progress.update(len(bytes_read))
    s.close()

def getFile():
    method = "GET"
    object_key = input("Type the file name: ")
    print(f"[+] Connecting to {host}:{port}")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    print("[+] Connected.")
    s.send(f"{method}{SEPARATOR}{object_key}{SEPARATOR}".encode())
    with open(object_key, "wb") as f:
        while True:
            # read 1024 bytes from the socket (receive)
            bytes_read = s.recv(BUFFER_SIZE)
            if not bytes_read:    
                # nothing is received
                # file transmitting is done
                break
            # write to the file the bytes we just received
            f.write(bytes_read)
            # update the progress bar
        
    s.close()

def deleteKey():
    method = "DELETE"
    object_key = input("Type the file name: ")
    print(f"[+] Connecting to {host}:{port}")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    print("[+] Connected.")
    s.send(f"{method}{SEPARATOR}{object_key}{SEPARATOR}".encode())
    print(s.recv(BUFFER_SIZE))        
    s.close()

def menu():
    run_client = True
    while(run_client):
        print("CHOOSE THE ACTION YOU WANT TO PERFORM")
        print("1.PUT")
        print("2.GET")
        print("3.DELETE")
        print("4.EXIT")
        try:
            opcion = int(input(": "))
            if ( opcion == 1):
                sendFile()
            elif ( opcion == 2):
                getFile()
            elif ( opcion == 3):
                deleteKey()
                
            elif(opcion == 4):
                run_client = False
        except Exception as e:
            print(e)

def startClient():
    menu()

startClient()
    
