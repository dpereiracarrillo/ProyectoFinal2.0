#Proyecto final de Python:
He mejorado la aplicación de la siguiente forma: 


                                      -Cambiando lo que imprimía por pantalla por unos popup para los avisos 
                                      
                                      
                                      -Incluyendo un botón de ayuda al usuario 
                                      
                                      
                                      -Añadiendo un treeview para consultar los datos 
                                      
                                      
                                      -Con un diseño más moderno de la interfaz para añadir clientes 
                                      
                                      
                                      -Añadiendo iconos y colores en la interfaz 
                                      
                                      
                                      -Le añadí excepciones para que no se pueda repetir la clave primaria
                                      
                                      
Mi proyecto consiste en una interfaz de gestión para un bar, tiene 3 clases: una para el login, otra para interactuar con la base de datos y otra para generar el pdf con el ticket.


##Inicio.py


En la primera clase llamada Inicio.py encontramos el login, que nos llama a la siguiente clase, donde interactuamos con la base. Sólo nos dejará acceder a la siguiente ventana en caso de poner correctamente el usuario y la contraseña. El usuario es "daniel" y la contraseña "bar".


##Bar.py


Es la clase principal del proyecto, en ella encontramos todos los métodos para utilizar los botones de la interfaz. 


En el método def nos conectamos con la base de datos , que hemos creado anteriormente en el programa SQLiteMan. La tabla dentro de la base de datos se llama bar y tiene como clave primaria un Codigo y como claves secundarias Producto,Precio,Cantidad,Cliente,Mesa,Telefono y Camarero. 


En el método mostrar nos crea el treeview que muestra en la interfaz todo lo que hacemos en el programa. El treeview nos selecciona directamente todo lo que tenemos en la base con un "select * from bar".


Método insertar. Una vez rellenamos todos los campos de texto hacemos click en el botón insertar, que está unido a este método y nos añadirá el pedido en la base de datos. Al acabar de insertar los pedidos podemos hacer click en el botón Actualizar para que nos muestre al momento como se encuentra la base actualmente.
Este método cuenta con excepciones, es decir, al insertar la clave primaria código no podemos repetirla, si no nos saltará un aviso y no nos lo insertará en la base.


Método modificar. Nos permite cambiar todos los atributos a parir de la primary key. Muy útil por si te confundes en un dato al meter el registro en la base de datos, sólo tendrías que poner el código y volver a inertar el registro correcatmente para cambiarlo.


Método ayuda. Nos saltará una pequeña ventana emergente con unas sencillas instrucciones para usar los botones de nuestra interfaz


Método consultar. Nos enseñe todo lo que se encuentra en la base de datos.


Método borrar. Borra para siempre los datos en nuestra base. Para usar est método solo tienes que colocarte en el treeviw de la interfaz y hacer click sobre el registro que quieras borrar, darle click a borrar y listo.


Método popup. Hace que nos slaten ventanas emergentes cada vez que hacemos click a un botón. Útil por si hacemos click en algo sin querer, ya que nos avisa de lo que hicimos en la base.


Método actualizar. Actualiza todo lo que hay dentro de la base.







