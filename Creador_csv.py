import csv
import random

# Lista de cultivos
cultivos = ['bola', 'cherry', ' de pera', 'kumato', 'rosa', 'verde','Raf','corazon de buey']

# Lista de ubicaciones geográficas
ubicaciones = ['El Ejido','La Mojonera','El Alquián','Nijar','Campohermoso']

# Lista de tamaños de fincas
tamanos = ['Pequeno', 'Mediana', 'Grande']

# Generar 5000 filas de datos aleatorios
datos = []
for i in range(5000):
    # Seleccionar aleatoriamente un cultivo, una ubicación, un tamaño y un rendimiento
    cultivo = random.choice(cultivos)
    ubicacion = random.choice(ubicaciones)
    if cultivo == 'cherry':
        tamano = 'Pequeno'
    elif cultivo == 'rosa' or cultivo == 'corazon de buey':
        tamano = 'Grande'
    else:
        tamano = random.choice(tamanos)

    rendimiento = int(round(random.uniform(1, 10), 0)) # Rendimiento aleatorio entre 1 y 10
    # Determinar si se utiliza o no fertilizantes
    fertilizantes = random.choice([False, True])
    # Agregar los datos a la lista
    datos.append([cultivo, ubicacion, tamano, rendimiento, fertilizantes])

# Guardar los datos en un archivo CSV
with open('datos_cultivo.csv', 'w', newline='') as archivo:
    writer = csv.writer(archivo)
    writer.writerow(['Cultivo', 'Ubicacion', 'Tamaño', 'Rendimiento', 'Fertilizantes'])
    for dato in datos:
        writer.writerow(dato)
