# import json

# data={}





# f= open("archivo.txt","a") 
# f.write("\nHola")
# f.write("\nAdios!final")
# f.close()

# print("hoola")
# print("adios")
# print("cual")

class Persona:
    def __init__(self):
        self.nombre = input("Ingrese el nombre: ")
        self.edad = input("Ingrese la edad: ")

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")

# Crear una instancia de la clase Persona
nueva_persona = Persona()

# Mostrar la información ingresada por el usuario
nueva_persona.mostrar_informacion()