import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from Bar import bar


class Login:
    def __init__(self):
            #Aqui hacemos que nos muestre la ventana de Inicio, en la que se encuentra el loggin
            builder2 = Gtk.Builder()
            builder2.add_from_file("inicio.glade")

            self.nombre = builder2.get_object("nombre")
            self.contraseña = builder2.get_object("contraseña")
            self.ventanaEntrada = builder2.get_object("inicio")

            sinais = {"on_Entrada_clicked": self.on_Entrada_clicked,
                      "delete-event": self.cerrar}

            builder2.connect_signals(sinais)
            self.ventanaEntrada.set_title("Log in.")
            self.ventanaEntrada.show_all()

    # Loggin que nos permite acceder a la ventana de pedidos, siempre y cuando sea corecto el usuario y contraseña, sino se muestra en la interfaz que pruebes otra vez
    def on_Entrada_clicked(self, widget):
        nombre = self.nombre.get_text();
        contraseña = self.contraseña.get_text();
        #usuario = daniel / conraseña = bar
        if nombre == "daniel" and contraseña == "bar":
            bar()
            self.ventanaEntrada.destroy()

        else:
            self.popup("Prueba otra vez")

    #este metodo destruye las ventanas
    def cerrar(self, widget):
        widget.destroy()

    #Metodo para que salga una ventana emergente segun el metodo en el que lo llame
    def popup(self, texto):
        window = Gtk.Window(title="Warning")
        label = Gtk.Label(texto)
        label.set_padding(15,15)
        window.add(label)
        window.connect("delete-event", self.cerrar)
        window.set_position(Gtk.PositionType.RIGHT)
        window.show_all()



Login()
#Hacemos que esta clase sea el Main para que se inicie de primera
Gtk.main()