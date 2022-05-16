# Documentacion Proyecto 2

## Integrantes:
Santiago Albisser Cifuentes  
Pablo Correa Morales  
Juan Pablo Leal Jaramillo  

## Requisitos no funcionales:
### Disponibilidad:
- El sistema debe estar disponible para operar con alta cantidad de peticiones.
- El sistema debe tener una disponibilidad mínima del 95%.
### Rendimiento:
- El tiempo de respuesta de la aplicación debe estar entre 1 y 2 segundos.
- El sistema debe estar diseñado para 1000 usuarios con un nivel de concurrencia del 10%.
### Seguridad:
- El sistema debe permitir la implementación de certificados digitales.
- El sistema debe tener implementado un mecanismo de autenticación.

## Diseño para escalabilidad:
### Buenas practicas:
- Para manejar la escalabilidad de la aplicación la práctica que se utilizó fue auto escalamiento. Esto para que el sistema varíe por sus propios medios para manejar la carga total, ya sea aumentar o disminuir.
- Para el diseño se tuvo en cuenta encerrar las subredes privadas con las instancias en las que corría la aplicación dentro de un grupo de auto escalamiento que provee AWS.
### Herramientas:
- Para el uso del auto escalamiento se utilizó la herramienta de AWS Auto Scaling Group que permite manejar las instancias necesarias para poder controlar la carga de la aplicación.

## Arquitectura:

## Proceso de instalación:
### DNS:
### Dominio:
### Certificados de seguridad:
### Servicios utilizados en AWS:
#### VPC:
![Alt text](/Proyecto2/img/vpc_creation.jpg "Title")
#### EC2:
**Instancia base de datos:**  
Para la configuración de la instancia de la base de datos primero se instaló el motor de base de datos dentro de la instancia que en este caso fue MongoDB y se corrieron estos comandos.
```
sudo yum install -y mongodb-org
sudo systemctl daemon-reload
sudo systemctl start mongod
```
Luego de tener MongoDB instalado se crea la base de datos que se va a utilizar.
```
use bookstore
```
Posteriormente se inserta en esa base de datos la información que se utilizará.
```
db.books.insertMany([{
        "name":"Leonardo Davinci: La Biografia",
        "image":"/images/img-ld-labiografia.jpeg",
        "author":"Walter Issacson",
        "description":"Basándose en las miles de páginas de los cuadernos manuscritos de Leonardo y nuevos descubrimientos sobre su vida y su obra, Walter Isaacson teje una narración que conecta el arte de Da Vinci con sus investigaciones científicas, y nos muestra cómo el genio del hombre más visionario de la historia nació de habilidades que todos poseemos y podemos estimular, tales como la curiosidad incansable, la observación cuidadosa y la imaginación juguetona. Su creatividad, como la de todo gran innovador, resultó de la intersección entre la tecnología y las humanidades. Despellejó y estudió el rostro de numerosos cadáveres, dibujó los músculos que configuran el movimiento de los labios y pintó la sonrisa más enigmática de la historia, la de la Mona Lisa. Exploró las leyes de la óptica, demostró como la luz incidía en la córnea y logró producir esa ilusión de profundidad en la Última cena.",
        "countInStock":"2",
        "price":"$50.000.oo"
    },
    {
        "name":"Inteligencia Genial",
        "image":"/images/img-ld-inteligenciagenial.jpeg","author":"Michael Gelb",
        "description":"El que, para muchos, ha sido el mayor genio de todos los tiempos, Leonardo da Vinci, puede servir de inspiración a todo aquel que quiera desarrollar al máximo su potencial intelectual y su creatividad. Paso a paso, mediante ejercicios, técnicas y lecciones, este libro muestra el camino para ampliar los horizontes de la mente",
        "countInStock":"3",
        "price":"$30.000.oo"
    }])
```
Finalmente se crea el usuario para que tenga los permisos de la edición de la base de datos.
```
db.createUser({
    user: 'telematica',
    pwd: 'telematica123',
    roles: [{ role: 'readWrite', db:'bookstore'}]
})
```

### Sistema de monitoreo de disponibilidad:
### Análisis del costo de la solución: