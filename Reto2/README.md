# Reto 2

En esta implementación de contenedores se tuvo dos enfoques principales, la dockerización de un servicio web usando CMS (En nuestro caso wordpress) y otra dockerización de una aplicación web con una arquitectura por capas (Front, Back, Base de Datos).

## Resumen Reto CMS

Dentro de esta primera parte el proceso constaba en crear un [Docker-Compose](https://github.com/PabloCorrea99/Telematica/blob/main/Reto2/WordPress/docker-compose) que separa la base de datos de la aplicación. Lo que resulta en 3 imagenes de Docker, esta tercera es generada gracias al proceso de aseguramiento del sistio web por medio del certificado ssl.
