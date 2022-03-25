import socket 
import os
from tkinter import SEPARATOR
import tqdm

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096
host = "127.0.0.1"
port = 80

def enviarArchivo():
    method = "PUT"
    filename = input("ingrese el nombre del archivo: ")
    filesize = os.path.getsize(filename)
    print(f"[+] Connecting to {host}:{port}")
    s.connect((host, port))
    print("[+] Connected.")
    s.send(f"{method}{SEPARATOR}{filename}{SEPARATOR}{filesize}".encode())
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

def menu():
    exit = True
    while(exit):
        print("Bienvenido a la app, seleccione una opción digitando el número de esta")
        print("1.Guardar archivos en la bd")
        print("2.recuperar archivos de la bd")
        print("3.listar archivos de la bd")
        print("4.borrar archivos de la bd")
        try:
            opcion = int(input(": "))
            if ( opcion >= 1 & opcion <= 4):
                print("Vamos a hacer la opcion: ", opcion)
                exit = False
        except:
            print("Un error ha surgido, verifique que ingresó")
    return opcion

if __name__ == '__main__':
    opcion = menu()
    if (opcion == 1):
        enviarArchivo()
    s.close()
    
