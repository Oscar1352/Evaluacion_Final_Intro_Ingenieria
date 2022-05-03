#Datos del estudiante
from traceback import print_tb


print("Nombre: Oscar Alejandro Luna Ordoñez")
print("Carné: 1530622")
print("Curso: Introducción a la Ingeniería en Informática y Sistemas")
print("Sección: 01")


# Serie V
# Solicitar los datos al usuario
animal_personal = "Monos"

animal_usuario = input("Por favor ingrese un animal que le guste: ")

#Comparación de los datos
if animal_personal == animal_usuario:
    print(f"A mí también me gustan los {animal_personal}")
else:
    print(f"Es un animal interesante, pero me gustan más los {animal_personal}")