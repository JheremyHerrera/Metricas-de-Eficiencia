import os
import pandas as pd

# Directorio donde están los archivos .txt
directorio = r'C:\Users\PC\Documents\PYTHON'  # Cambia esto si los archivos no están en el directorio actual

# Listar todos los archivos .txt en el directorio
archivos_txt = [f for f in os.listdir(directorio) if f.endswith('.txt') and f.startswith('iteracion')]

# Lista para almacenar los datos de cada archivo
datos_combinados = []

# Función para leer un archivo y extraer los datos
def leer_archivo(archivo):
    with open(archivo, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        num_ensayo = int(lines[0].split(":")[1].strip())
        num_puntos = int(lines[1].split(":")[1].strip())
        tiempo_ejecucion = float(lines[2].split(":")[1].strip().split()[0])  
        iteraciones = float(lines[3].split(":")[1].strip().split()[0])  
        pi_estimada = float(lines[4].split(":")[1].strip())
        return [num_ensayo, num_puntos, iteraciones, tiempo_ejecucion, pi_estimada]

# Leer cada archivo y agregar los datos a la lista
for archivo in archivos_txt:
    datos = leer_archivo(os.path.join(directorio, archivo))
    datos_combinados.append(datos)

# Crear un DataFrame de Pandas con los datos combinados
df = pd.DataFrame(datos_combinados, columns=['Ensayo', 'Tamaño', 'Itera.', 'Tiempo', 'Estimación'])

# Ordenar el DataFrame por la columna 'Ensayo'
df = df.sort_values(by='Ensayo')

# Guardar el DataFrame en un nuevo archivo .txt
archivo_salida = os.path.join(directorio, 'tabla_final.txt')
df.to_csv(archivo_salida, sep='\t', index=False)

print(f'Tabla final guardada en {archivo_salida}')


