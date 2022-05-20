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
![Alt text](/Proyecto2/img/architecture.png "architecture")
https://lucid.app/lucidchart/0dd85e9e-5358-44b2-ba1e-d6d227aac993/edit?invitationId=inv_f68f263f-ef5f-4e34-8939-9f755543afa7

## Proceso de instalación:
### DNS:
[LB-BSFront-561551121.us-east-1.elb.amazonaws.com](LB-BSFront-561551121.us-east-1.elb.amazonaws.com)
### Dominio:
https://www.bookstorep2.tk/
### Cloudflare:
Se utilizó Cloudflare para los certificados SSL y la CDN.  
Lo primero que se realizó fue crear la cuenta y luego se ingresó el dominio para que el programa lo agregue.
![Alt text](/Proyecto2/img/cloudflare_1.jpg "cloud_flare1")
Luego se agregó el record con los valores de nuestra página que se encuentran en el load balancer.
![Alt text](/Proyecto2/img/cloudflare_2.jpeg "cloud_flare2")
Luego de darle continue en esta página se seleccionó la opción de check name servers.
![Alt text](/Proyecto2/img/cloudflare_3.jpeg "cloud_flare3")  
Luego apareció este mensaje que indicó que el proceso había sido completado con éxito y la aplicación ya cuenta con el certificado de seguridad y el CDN.
![Alt text](/Proyecto2/img/cloudflare_4.jpeg "cloud_flare4")
### Servicios utilizados en AWS:
#### VPC:
La creación de la VPC se realizó de la siguiente forma. Creando dos zonas de disponibilidad, dos subredes públicas, cuatro subredes privadas y una NAT gateway por cada zona de disponibilidad.  
También se asignaron las IPs a cada una de las subredes según como se indica en la arquitectura.
![Alt text](/Proyecto2/img/vpc_creation.jpg "vpc_creation")
#### EC2:
**Instancia bastion host:**
La creación de la instancia de bastion host se realizó:  
1. Seleccionando la AMI Amazon Linux 2 AMI (HVM) - Kernel 5.10, SSD Volume Type.
2. Se seleccionó esto en la configuración de la instancia para la configuración de la vpc.
![Alt text](/Proyecto2/img/vpc_bastion.jpg "vpc_bastion")
3. El grupo de seguridad se creó habilitando la conexión SSH mediante MyIp.
4. El resto de valores se dejaron por defecto y se creó la instancia.

Luego de que se crearon el resto de las instancias ya se pudo realizar la conexión ingresando desde este bastion host.

**Instancia base de datos:**
La creación de la instancia de la base de datos se realizó:  
1. Seleccionando la AMI Amazon Linux 2 AMI (HVM) - Kernel 5.10, SSD Volume Type.
2. Se seleccionó esto en la configuración de la instancia para la configuración de la vpc.
![Alt text](/Proyecto2/img/vpc_db.jpg "vpc_db")
3. El grupo de seguridad se creó habilitando la conexión SSH desde las IPs de las dos subredes públicas y también se habilitaron los puertos 27017 y 27039 para las IPs de las subredes privadas donde iban a estar el back y el frontend.
4. El resto de valores se dejaron por defecto y se creó la instancia.

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

**Instancia backend:**
La creación de la instancia del frontend se realizó:  
1. Seleccionando la AMI Amazon Linux 2 AMI (HVM) - Kernel 5.10, SSD Volume Type.
2. Se seleccionó esto en la configuración de la instancia para la configuración de la vpc.
![Alt text](/Proyecto2/img/vpc_backfront.jpg "vpc_backfront")
3. El grupo de seguridad se creó habilitando la conexión SSH desde las IPs de las dos subredes públicas y se habilitaron los puertos 80 y 5000 para http desde cualquier IP.
4. El resto de valores se dejaron por defecto y se creó la instancia.

Dentro de la instancia se configuró git y docker para clonar el repositorio donde se tenía el backend
```
sudo amazon-linux-extras install docker –y
sudo systemctl enable docker
sudo systemctl start docker
sudo usermod -a -G docker ec2-user

sudo yum install git –y
```

Luego de clonar el repositorio y ya dentro de la carpeta del backend se corre este comando para crear la imagen y posteriormente para correrla y dejarla corriendo.
```
sudo docker build -t <name> .
sudo docker run --restart=always -dit -p 5000:5000 <name>
```

**Instancia frontend:**
La creación de la instancia del backend se realizó:  
1. Seleccionando la AMI Amazon Linux 2 AMI (HVM) - Kernel 5.10, SSD Volume Type.
2. Se seleccionó esto en la configuración de la instancia para la configuración de la vpc.
![Alt text](/Proyecto2/img/vpc_backfront.jpg "vpc_backfront")
3. El grupo de seguridad se creó habilitando la conexión SSH desde las IPs de las dos subredes públicas y se habilitó el puerto 80 para http desde la IP del bastion host.
4. El resto de valores se dejaron por defecto y se creó la instancia.

Dentro de la instancia se configuró git y docker para clonar el repositorio donde se tenía el frontend
```
sudo amazon-linux-extras install docker –y
sudo systemctl enable docker
sudo systemctl start docker
sudo usermod -a -G docker ec2-user

sudo yum install git –y
```

Luego de clonar el repositorio y ya dentro de la carpeta del frontend se corre este comando para crear la imagen y posteriormente para correrla y dejarla corriendo.
```
sudo docker build -t <name> .
sudo docker run --restart=always -dit -p 80:80 <name>
```

Como se crearon dos load balancer, uno para el front y otro para el back, desde acá en adelante se mostrará el proceso de implementación de cada servicio especificando las cosas que se utilizaron en cada uno de los dos.

#### AMI:
Para la creación de las AMI se realizó este proceso:  
1. Se seleccionó la instancia a la cual se le quería crear la AMI y luego en Actions -> Image and Templates -> Create Image.
2. Se definió el nombre y la descripción de la imagen.
3. Se dio en Create Image y ya la imagen fue creada.

#### Target group:
Para la creación de los target groups se realizó este proceso:
1. Se ingresó a Target Groups desde EC2.
2. Se dio en crear un nuevo target group.
3. En el target type se señaló Instances.
4. En el target group name se definió el nombre.
5. En el protocolo se seleccionó para el target group del backend HTTP:5000 y para el del frontend HTTP:80.
6. En la VPC se seleccionó la VPC que se creó.
7. En protocol version HTTP1.
8. Se da en Next y en la siguiente página no se configuró nada y se dio click en create target group.

#### Load balancer:
Para la creación de los load balancers se realizó este proceso:
1. Se ingresó a Load balancers desde EC2.
2. En la configuración básica se definió el nombre y en scheme para el del backend se puso internal y en el del frontend se puso Internet facing.
3. En Network mappings se seleccionó la VPC de Bookstore. En mappings las dos subredes públicas para el frontend y dos de las subredes privadas para el backend.
4. Se creó un security group para el load balancer que permita tráfico http al puerto 5000 para el backend y al 80 para el frontend.
5. En Listener se seleccionó Protocol HTTP. 5000 para el backend y 80 para el frontend.
6. En Forward to se seleccionó el Target group que se creó previamente.
7. Se dio en create load balancer.

#### Launch template:
Para la creación de los launch templates se siguieron estos pasos:
1. Se ingresó a Launch templates desde EC2.
2. Se ingresó a create launch template.
3. En Launch template name and description se definió el nombre y la descripción y se activó la casilla de auto scaling guidance.
4. En Launch template contents se seleccionó MyAMIs y en Owned by me se seleccionó la AMI correspondiente.
5. En Instance Type se seleccionó t2.micro.
6. Se dio en create launch template.

#### Auto scaling group:
Para la creación de los auto scaling groups se realizó el siguiente proceso:
1. Se ingresó a la pestaña de auto scaling groups en EC2.
2. Se dio en create auto scaling group.
3. En Name se definió el nombre.
4. En Launch template se seleccionó el launch template correspondiente que se había creado.
5. En choose instance launch options se seleccionó la VPC de Bookstore y en Availability zones and subnets las dos subredes privadas en las que iban a estar back y frontend.
6. En advanced options se seleccionó la opción de attach to an existing load balancer.
7. Se seleccionó luego la opción de choose from your load balancer target groups y se seleccionó el target group correspondiente.
8. Se marcó la casilla de enable group metrics collections within cloudwatch.
9. Se creó un target tracking scalling policy con un target value de 60.
10. Luego se creó un tag con el Name para cada caso de front y back.
11. Se creo el auto scaling group

Después de un momento se verificó en los Target groups que estuviera todo correcto y apareció de esta forma.
![Alt text](/Proyecto2/img/targetgroup_healthy.jpg "targetgroup_healthy")

### Sistema de monitoreo de disponibilidad:
Para el sistema de monitoreo de disponibilidad se utilizó la herramienta Uptime Robot. Primero se creó la cuenta y luego se da click en el botón de Add new monitor y se llena con esta información.
![Alt text](/Proyecto2/img/monitor_creation.jpg "monitor_creation")
Luego de que se crea el monitor y ya se tiene la aplicación corriendo se puede observar la información acerca de la disponibilidad del sistema.
![Alt text](/Proyecto2/img/monitor_monitoring.jpg "monitor_monitoring")