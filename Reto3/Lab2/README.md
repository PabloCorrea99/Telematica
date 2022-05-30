## Documentación Laboratorio 2
# Prerequisitos
Para la elaboración de este laboratorio necesitamos haber completado el Laboratorio 1 y contar con un cluster de EMR activo.
# Hue
Una vez en Hue en la zona de files debemos replicar la estructura de archivos que se tiene en el repositorio de la materia. De allí tomaremos los datos
![image](https://user-images.githubusercontent.com/38085662/170907809-1a02693e-c8dd-4413-9e30-f24555e5ddec.png)
Lo que buscamos conseguir es poder copiar los archivos tambien vía ssh haciendo uso del los steps en el cluster de EMR, s3 y la consola de nuestro cluster.
# Step
Se debe crear un step el cual puede tener el nombre que se quiera, en el comando se debe colocar `command-runner.jar` y en el argumento debe ir:
<s3-dist-cp --src=s3://s3distcp-source/input-data --dest=hdfs:///output-folder1>
Una vez completado el step podemos ejecutar el comando `hdfs dfs -ls /dataset` en el cual veremos que se pasaron los archivos.
![image](https://user-images.githubusercontent.com/38085662/170912551-5997bd19-a7f2-4a74-80ea-86ff2f59302d.png)
# Consola Bash
  En la consola de nuestro EMR se debe correr los siguientes comandos para tomar los datos que pasamos desde s3 e insertarlos en hadoop.
  ![image](https://user-images.githubusercontent.com/38085662/170912713-2774a6a5-f3ae-43d3-bd51-d890185379b6.png)
  ![image](https://user-images.githubusercontent.com/38085662/170912739-991c10f4-4f76-494c-a08c-755f93dc1615.png)
  Como podemos ver reultamos con las misma estructura quen en s3, tanto en Hue como en el Hadoop dentro del Cluster de EMR

  
# Nota
  Profe por temas laborales y personales no me fue posible documentar bien lo que queda faltando del laboratorio
