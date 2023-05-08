import csv
import random

# Lista de cultivos
cultivos = ['maíz', 'trigo', 'arroz', 'café', 'banano', 'cacao']

# Lista de ubicaciones geográficas
ubicaciones = ['Almeria', 'Murcia', 'Valencia', 'Canarias','Granada']

# Lista de tamaños de fincas
tamanios = ['Pequeña', 'Mediana', 'Grande']

# Generar 100 filas de datos aleatorios
datos = []
for i in range(5000):
    # Seleccionar aleatoriamente un cultivo, una ubicación, un tamaño y un rendimiento
    cultivo = random.choice(cultivos)
    ubicacion = random.choice(ubicaciones)
    tamano = random.choice(tamanios)
    rendimiento = round(random.uniform(1, 10), 2) # Rendimiento aleatorio entre 1 y 10
    # Determinar si se utiliza o no fertilizantes
    fertilizantes = random.choice([False, True])
    # Agregar los datos a la lista
    datos.append([cultivo, ubicacion, tamano, rendimiento, fertilizantes])

# Guardar los datos en un archivo CSV
with open('datos_cultivo.csv', 'w', newline='') as archivo:
    writer = csv.writer(archivo)
    writer.writerow(['Cultivo', 'Ubicación', 'Tamaño', 'Rendimiento', 'Fertilizantes'])
    for dato in datos:
        writer.writerow(dato)
