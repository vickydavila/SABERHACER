import xml.etree.cElementTree as et

root = et.Element("Edificio_TI")

se = et.SubElement(root,"Alumno_1")
et.SubElement(se, "Matricula").text = "18040101"
et.SubElement(se, "Carrera").text = "Redes inteligentes"
et.SubElement(se, "Nombre").text = "Aylin Ximena Arreozola Sanchez"

se = et.SubElement(root,"Alumno_2")
et.SubElement(se, "Matricula").text = "18040102"
et.SubElement(se, "Carrera").text = "Redes inteligentes"
et.SubElement(se, "Nombre").text = "Paula Leticia Chairez Vazquez"

se = et.SubElement(root,"Alumno_3")
et.SubElement(se, "Matricula").text = "18040103"
et.SubElement(se, "Carrera").text = "Redes inteligentes"
et.SubElement(se, "Nombre").text = "Adaia Victoria Davila Duran"

se = et.SubElement(root,"Alumno_4")
et.SubElement(se, "Matricula").text = "18040104"
et.SubElement(se, "Carrera").text = "Redes inteligentes"
et.SubElement(se, "Nombre").text = "Josue Fernando Flores Contreras"

se = et.SubElement(root,"Alumno_5")
et.SubElement(se, "Matricula").text = "18040105"
et.SubElement(se, "Carrera").text = "Redes inteligentes"
et.SubElement(se, "Nombre").text = "Jonathan Hernandez Rodriguez"

se = et.SubElement(root,"Alumno_6")
et.SubElement(se, "Matricula").text = "18040200"
et.SubElement(se, "Carrera").text = "Entornos Virtuales"
et.SubElement(se, "Nombre").text = "Heidy Medina Alvares"

se = et.SubElement(root,"Alumno_7")
et.SubElement(se, "Matricula").text = "18040201"
et.SubElement(se, "Carrera").text = "Entornos Virtuales"
et.SubElement(se, "Nombre").text = "Andrea Renteria Contreras"

se = et.SubElement(root,"Alumno_8")
et.SubElement(se, "Matricula").text = "18040202"
et.SubElement(se, "Carrera").text = "Entornos Virtuales"
et.SubElement(se, "Nombre").text = "Oscar Hernandez Mireles"

se = et.SubElement(root,"Alumno_9")
et.SubElement(se, "Matricula").text = "18040203"
et.SubElement(se, "Carrera").text = "Entornos Virtuales"
et.SubElement(se, "Nombre").text = "Jesus Armando Davila Valdes"

se = et.SubElement(root,"Alumno_10")
et.SubElement(se, "Matricula").text = "18040204"
et.SubElement(se, "Carrera").text = "Entornos Virtuales"
et.SubElement(se, "Nombre").text = "Harant Garcia Hernandez"

se = et.SubElement(root,"Alumno_11")
et.SubElement(se, "Matricula").text = "18040300"
et.SubElement(se, "Carrera").text = "Desarrollo de Software"
et.SubElement(se, "Nombre").text = "Getzel Charles Nuñez"

se = et.SubElement(root,"Alumno_12")
et.SubElement(se, "Matricula").text = "18040301"
et.SubElement(se, "Carrera").text = "Desarrollo de Software"
et.SubElement(se, "Nombre").text = "Carla Maria Rodriguez Ballesteros"

se = et.SubElement(root,"Alumno_13")
et.SubElement(se, "Matricula").text = "18040302"
et.SubElement(se, "Carrera").text = "Desarrollo de Software"
et.SubElement(se, "Nombre").text = "Tania Gaona Valdes"

se = et.SubElement(root,"Alumno_14")
et.SubElement(se, "Matricula").text = "18040303"
et.SubElement(se, "Carrera").text = "Desarrollo de Software"
et.SubElement(se, "Nombre").text = "Roberto Magallenas Casas"

se = et.SubElement(root,"Alumno_15")
et.SubElement(se, "Matricula").text = "18040313"
et.SubElement(se, "Carrera").text = "Desarrollo de Software"
et.SubElement(se, "Nombre").text = "Juan Carlos Revilla Zapata"

tree = et.ElementTree(root)
tree.write("Alumnos.xml", xml_declaration=True)




















