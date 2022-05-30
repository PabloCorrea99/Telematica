## Documentación Laboratorio 1
# Prerequisitos:
- Contar con una key de aws para conectarse al cluster de EMR
- Crear un bucket de s3 el cual se va a conectar con nuestro EMR, en nuestro ejercicio este se llama `reto3jupyterpcorream2`
# Cluster de EMR:
A continuación se presenta el cluster de EMR que se creo y la configuración de este mismo: 
![](https://github.com/PabloCorrea99/Telematica/blob/main/Reto3/Lab1/imagenes/emrconf1.PNG?raw=true)
Cabe resaltar que no se estan utilizando maquinas m5, ya que estas no son soportadas en la capa gratuita de aws
![](https://github.com/PabloCorrea99/Telematica/blob/main/Reto3/Lab1/imagenes/emrconf2.PNG?raw=true)
Una vez creado se optiene lo siguiente: 
![](https://github.com/PabloCorrea99/Telematica/blob/main/Reto3/Lab1/imagenes/emrfinal.PNG?raw=true)
Para los puertos que se van a utilizar para conectarnos a las diferentes aplicaciones que seleccionamos, 
debemos abrir los siguientes tanto desde la interfaz del EMR como desde el grupo de seguridad en las reglas de entrada.

![](https://github.com/PabloCorrea99/Telematica/blob/main/Reto3/Lab1/imagenes/puertos.PNG?raw=true)

# HUE
Nos conectaremos a Hue una vez tengamos habilitado el puerto, alli deberemos crear un usuario y password. 
![](https://github.com/PabloCorrea99/Telematica/blob/main/Reto3/Lab1/imagenes/hue.PNG?raw=true)

# JupyterHub
Al igual que en Hue, necesitamos que el puerto de conexión este habilitado y 
tenemos que ingresar con el usuario default de la aplicación que es: `jovyan` con password `jupyter`.
![](https://github.com/PabloCorrea99/Telematica/blob/main/Reto3/Lab1/imagenes/jupyterhub.PNG?raw=true)
Una vez acá es recomendable crear un notebook con de PySpark y probar las variables `spark` y `sc` para verificar que si contamos con spark instalado.

# Nota
Para tener en cuenta, una vez se haya terminado un cluster porque el tiempo paso, simplemente este debe ser clonado y el nuevo tendra la misma configuración y sera ejecutado.
