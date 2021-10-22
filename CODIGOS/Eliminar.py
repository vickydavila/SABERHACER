from xml.etree.ElementTree import parse, Element

file_name = 'Alumnos.xml'
doc_xml = parse(file_name)
root = doc_xml.getroot()

root.remove(root.find('Alumno_1'))

new_file = 'Alumno2.xml'
doc_xml.write(new_file, xml_declaration=True)
