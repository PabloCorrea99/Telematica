# Reto 2

<p>En esta implementación de contenedores se tuvo dos enfoques principales, la dockerización de un servicio web usando CMS (En nuestro caso wordpress) y otra dockerización de una aplicación web con una arquitectura por capas (Front, Back, Base de Datos).</p>

<hr/>

<p>Antes de pasar al resumen de cada implementación dejo la instalación de Docker y de Docker-Compose</p>

### Instalar Docker:
    sudo amazon-linux-extras install docker -y
    sudo systemctl enable docker
    sudo systemctl start docker
    sudo usermod -a -G docker ec2-user
    
### Instalar Docker-Compose:
    sudo curl -L https://github.com/docker/compose/releases/download/1.29.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
    
## Resumen reto CMS

Dentro de esta primera parte el proceso constaba en crear un [Docker-Compose](https://github.com/PabloCorrea99/Telematica/blob/main/Reto2/WordPress/docker-compose) que separa la base de datos de la aplicación. Lo que resulta en 3 imagenes de Docker, esta tercera es generada gracias al proceso de aseguramiento del sistio web por medio del certificado ssl. Se puede encontrar la página en el siguiente link: www.pcorreacmstelematica.ml


## Resumen reto aplicación por capas
En este caso el funcionamiento es un poco diferente puesto que se tuvieron que realizar 2 Dockerfiles, uno para cada ambiente. Ya que la aplicación esta separada entre Frontend (ReactJS) y Backend (NodeJS) en maquinas y contenederos diferentes. Adicional, y para cumplir con el aseguramiento del sistema, se creo otro Docker-Compose para conseguir el certificado ssl, este se ubica en la misma maquina del front pero en una imagen de docker diferente, lo que permite que si se quiere añadir otro conteneder de front esa este se le pueda crear el certificado de una manera muy dinamica. El link para conectarse a la aplicación es este: https://www.pcorreabookstore.ml/ 
