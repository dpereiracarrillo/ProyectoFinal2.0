__author__ = 'dani'


import os

from reportlab.platypus import Paragraph
from reportlab.platypus import Image
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

from reportlab.platypus import Table

import sqlite3 as dbapi
bbdd=dbapi.connect("bar.dat")
cursor=bbdd.cursor()

#cursor.execute("""create table usuarios(dni text,nombre text,direccion text)""")
#cursor.execute("""insert into usuarios values('3333333-A','Maria','Canceleiro')""")

#bbdd.commit()


#creación del informe en PDF llamado Ticket
cursor.execute("select * from bar")
tablaBaseDatos=[]

for fila in cursor:
    tablaBaseDatos.append(fila)

tabla=Table(tablaBaseDatos)

guion=[]

guion.append(tabla)
doc=SimpleDocTemplate("Ticket.pdf",pagesize=A4,showBoundary=1)
doc.build(guion)
cursor.close()
bbdd.close()