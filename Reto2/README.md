# Reto 2

<p>En esta implementación de contenedores se tuvo dos enfoques principales, la dockerización de un servicio web usando CMS (En nuestro caso wordpress) y otra dockerización de una aplicación web con una arquitectura por capas (Front, Back, Base de Datos).</p>
<hr/>
## Resumen Reto CMS

<p>Dentro de esta primera parte el proceso constaba en crear un [Docker-Compose](https://github.com/PabloCorrea99/Telematica/blob/main/Reto2/WordPress/docker-compose) que separa la base de datos de la aplicación. Lo que resulta en 3 imagenes de Docker, esta tercera es generada gracias al proceso de aseguramiento del sistio web por medio del certificado ssl.</p>
<ul>
  <li> ### Instalar Docker:
    sudo amazon-linux-extras install docker -y
    sudo yum install git -y
    sudo systemctl enable docker
    sudo systemctl start docker
    sudo usermod -a -G docker ec2-user
  </li>
  <li>Second item</li>
  <li>Third item</li>
  <li>Fourth item</li>
</ul>
