import csv
from faker import Faker
import random

fake = Faker()

# Lista de cultivos
cultivos = ['bola', 'cherry', ' de pera', 'kumato', 'rosa', 'verde','Raf','corazon de buey']

# Lista de ubicaciones geográficas
lista_ubicaciones = ['El Ejido','La Mojonera','El Alquian','Nijar','Campohermoso']

# Definimos la lista de cabezales de las columnas
headers = ['Cultivo',  'Ubicaciones', 'Rendimiento','Tamano','Fertilizantes']

# Definimos el nombre del archivo CSV
filename = 'lista_tomates.csv'

# Definimos el número de filas que deseamos generar
num_rows = 5000

# Abrimos el archivo CSV en modo escritura
with open(filename, mode='w', newline='') as csv_file:
    # Creamos el objeto writer para escribir en el archivo CSV
    writer = csv.writer(csv_file)
    
    # Escribimos la fila de cabezales en el archivo CSV
    writer.writerow(headers)
    
    # Generamos las filas de datos aleatorios y las escribimos en el archivo CSV
    for i in range(num_rows):
        cultivo = random.choice(cultivos)
        ubicaciones = random.choice(lista_ubicaciones)
        row = [
            cultivo,           # Cultivo
            ubicaciones,        # Ubicaciones
            fake.random_number(digits=3)/100,        # Rendimiento
            fake.random_int(min=1,max=4),      # Tamaño 1-pequeño 2-mediano 3-grande 4-muy grande
            fake.boolean()         # Fertilizantes
        ]
        writer.writerow(row)
        
print(f'Se ha generado el archivo "{filename}" con {num_rows} filas de datos ficticios.')
