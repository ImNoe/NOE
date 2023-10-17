import yaml
import json
import xml.etree.ElementTree as ET


# Definimos una función para crear un objeto docente
def crear_docente(nombre, numero_empleado, especialidad):
    return {
        "nombre": nombre,
        "numero_empleado": numero_empleado,
        "especialidad": especialidad
    }

# Creamos una lista de docentes
docentes = [
    crear_docente("Roberto Perez", 10023, "Haking etico"),
    crear_docente("Maria Azucena", 10024, "Direccion de proyectos 2"),
    crear_docente("Patricia Guadalupe", 10025, "Inteligencia de negocios"),

]
 