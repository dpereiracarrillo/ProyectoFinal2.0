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
En el método mostrar nos crea el treeview que muestra en la interfaz todo lo que hacemos en el programa
