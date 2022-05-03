<h3 align="Center"> RPC y Redis </h3>

_Proyecto donde se trabaja con redis, rpc en python y postgres_

---------------------------------------

<p>Para poder iniciar esta aplicación es importante realizar un unico ajuste (el cual dependera netamente de la decision personal de cada uno) para poder decidir que política de remoción sera utilizada por el servidor de redis, tambien se podra cambiar la memoria máxima asignada </p>

<p>Se deberá dirigir al archivo api.py, ubicado en en la ruta Tarea1SD/Cliente. Una vez dentro del archivo iremos a la línea número 14 y 15, donde podremos asignar la memoria máxima de nuestro caché (escrita en bytes) y la politica de remoción (Esta por defaulta LRU o Least Recently Used)</p>

![imagen](https://user-images.githubusercontent.com/69986261/166571463-a62d398f-cb4a-433c-acb9-f425f56548f8.png)

<p> Una vez realizado el ajuste inicial se procede a ejecutar los siguientes comandos, sin embargo para que funcionen debemos estar en la raíz de la carpeta </p>

<h4> Comandos </h4>

```
$ docker-compose build --no-cache
$ docker-compose up --force-recreate
```

<p>Una vez inicializado el sistema se podran realizar las consultas al cliente, se podran realizar a traves del navegador o postman. Para ello se deberá utilizar el siguiente link para el navegador: </p>

```
localhost:8000
```

<p> Y para utilizar postman, se deberá utilizar la siguiente ruta: </p>

```
http://localhost:8000/search?search=
```
<p> Donde despúes del signo "=" se debe escribir la cadena de caracteres a buscar. </p>

---------------------------------------

<h3 align="Center">Política de Remoción</h3>

<p> Para este trabajo, se revisaron dos opciones de las tantas que permite redis. Nosotros creemos que para este tipo de sistemas y plataformas es mejor "allkeys-lfu", ya que es importante mantener en caché aquellas búsquedas que presentan una mayor frecuencia frente a otras. Permitiendo así que en situaciones de "e-commerce" por ejemplo, los artículos que sean más buscados y/o cotizados tengan un acceso más rápido para aquellas que no presentan la misma frecuencia de búsqueda. </p> 

