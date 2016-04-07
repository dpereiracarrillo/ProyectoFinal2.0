#paquetes importados, previa instalación de pygobejct para tener el Gtk3+
import sqlite3 as dbapi
import gi
#especifico la versión de Gtk para que no me de errores
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# He mejorado la aplicación de la siguiente forma:
#                       -Cambiando lo que imprimía por pantalla por unos popup para los avisos
#                       -Incluyendo un botón de ayuda al usuario
#                       -Añadiendo un treeview para consultar los datos
#                       -Con un diseño más moderno de la interfaz para añadir clientes
#                       -Añadiendo iconos y colores en la interfaz
#                       -Le añadí excepciones para que no se pueda repetir la clave primaria
#

#creamos nuestra clase
class bar:


    def __init__(self):
        # Conexión con la base de datos, creada desde SQLiteMan, en la que existe una tabla llamada bar con todos nuestros atributos
        self.bd = dbapi.connect("bar.dat")
        self.cursor = self.bd.cursor()
        #Abrimos y conectamos a la interfaz de taller
        self.builder = Gtk.Builder()
        self.builder.add_from_file("pedido.glade")
        self.mostrar()
        self.ventana = self.builder.get_object("Bar")

        #Declaramos los nombres de los métodos para que al pulsar el boton tenga función
        sinais = {"on_insertar_clicked": self.on_insertar_clicked,
                      "on_consultar_clicked": self.on_consultar_clicked,
                      "on_borrar_clicked": self.on_borrar_clicked,
                      "on_Modificar_clicked": self.on_Modificar_clicked,
                      "on_ayuda_clicked":self.on_ayuda_clicked,
                      "delete-event": Gtk.main_quit}
        self.builder.connect_signals(sinais)
        self.ventana.set_title("Pedido")
        self.ventana.show_all()

    def mostrar(self):
        #Aqui montamos el treeview para que nos muestre las consultas que hacemos en la base de datos
        self.box = self.builder.get_object("box2")
        self.scroll = Gtk.ScrolledWindow()
        self.scroll.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        self.vista = Gtk.TreeView()
        self.box.add(self.scroll)
        self.scroll.add(self.vista)
        self.scroll.set_size_request(500, 500)
        self.scroll.show()

        self.lista = Gtk.ListStore(str, str, str, str, str, str, str, str)

        self.lista.clear()
        self.cursor.execute("select * from bar")
        for merla in self.cursor:
            self.lista.append(merla)

        self.vista.set_model(self.lista)

        for i, title in enumerate(["codigo","producto","precio","cantidad","cliente","mesa", "telefono", "camarero"]):
            render = Gtk.CellRendererText()
            columna = Gtk.TreeViewColumn(title, render, text=i)
            self.vista.append_column(columna)

    #Método insertar
    def on_insertar_clicked(self, control):
        codigo = self.builder.get_object("codigo").get_text()
        producto = self.builder.get_object("producto").get_text()
        precio = self.builder.get_object("precio").get_text()
        cantidad = self.builder.get_object("cantidad").get_text()
        cliente = self.builder.get_object("cliente").get_text()
        mesa = self.builder.get_object("mesa").get_text()
        telefono = self.builder.get_object("telefono").get_text()
        camarero = self.builder.get_object("camarero").get_text()
        try:
            self.cursor.execute(
                "insert into bar values('" + codigo + "'"
                                         ",'" + producto + "'"
                                         ",'" + precio + "'"
                                         ",'" + cantidad +"'"
                                         ",'" + cliente + "'"
                                         ",'" + mesa +"'"
                                         ",'" + telefono +"'"
                                         ",'" + camarero +"')")
            self.popup("Insertado")
            self.actualizar()
            # Siempre se debe hacer un commit al final de cada evento
            self.bd.commit()
            #esta excepción hace que no se pueda repetir la primary key
        except dbapi.IntegrityError:
            self.popup("ERROR! El código ya existe")

    #Metodo ayuda que nos da unas fáciles instrucciones para utilizar la interfaz
    def on_ayuda_clicked(self, widget):
        self.popup("Boton Añadir:\nDespués de rellenar todos los campos, se le hace click para añadir un registro en la base de datos\nBoton Eliminar\nElimina el cliente seleccionado de la base de datos\nBoton Editar:\nPermite modificar los registros según su clave primaria\nBotón Actualizar:\nNos actualiza los registros cada vez que le hacemos click.")
    # Método consultar, que nos enseña lo que se encuentra en la base de datos
    def on_consultar_clicked(self, control):
        self.actualizar()

    #Metodo borrar
    def on_borrar_clicked(self, widget):
        selection = self.vista.get_selection()
        model, selec = selection.get_selected()
        if selec != None:
            self.codigo = model[selec][0]
            self.cursor.execute("delete from bar where codigo ='" + self.codigo + "'")
            self.actualizar()
            self.bd.commit()
            self.popup("El elemento ha sido borrado")

    #Método modificar. A través de la primary key (codigo) nos permite editar el resto de atributos
    def on_Modificar_clicked(self, modificar):
        codigo = self.builder.get_object("codigo").get_text()
        producto = self.builder.get_object("producto").get_text()
        precio = self.builder.get_object("precio").get_text()
        cantidad = self.builder.get_object("cantidad").get_text()
        cliente = self.builder.get_object("cliente").get_text()
        mesa = self.builder.get_object("mesa").get_text()
        telefono = self.builder.get_object("telefono").get_text()
        camarero = self.builder.get_object("camarero").get_text()

        self.cursor.execute("update bar set producto ='" + producto + "'"
                                             ",precio='" + precio + "'"
                                             ",cantidad='" + cantidad + "'"
                                             ",cliente='" + cliente + "'"
                                             ",mesa='" + mesa +"'"
                                             ",telefono='" + telefono +"'"
                                             ",camarero='" + camarero +"' where codigo='" + codigo + "'")
        self.popup("Modificado")
        self.bd.commit()
        self.actualizar()


    #Método actualizar, que actualiza los datos de la tabla cada vez que le hacemos click
    def actualizar(self):
        self.lista.clear()
        self.cursor.execute("select * from bar")
        for merla in self.cursor:
            self.lista.append(merla)

        self.vista.set_model(self.lista)

    #El método popup nos permite crear ventanas emergentes con los avisos
    def popup(self, texto):
        window = Gtk.Window(title="Aviso")
        label = Gtk.Label(texto)
        label.set_padding(15, 15)
        window.add(label)
        window.connect("delete-event", self.cerrar)
        window.set_position(Gtk.PositionType.RIGHT)
        window.show_all()

    #Para cerrar los popups y que se destruyan
    def cerrar(self, widget):
        widget.destroy()




