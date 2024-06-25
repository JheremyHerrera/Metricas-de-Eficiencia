import random # números aleatorios                      
import time   # valores de tiempo
import matplotlib.pyplot as plt # gráfica
import pandas as pd # manipulación y el análisis de datos

def estimar_pi(num_puntos):
    dentro_circulo = 0
    iteraciones = 0
    
    inicio = time.time() # iniciamos el tiempo
    for _ in range(num_puntos):
        iteraciones += 1
        x = random.uniform(-1, 1) # dimesinoes del cuadrado
        y = random.uniform(-1, 1)
        
        if x**2 + y**2 <= 1: # puntos dentro del circulo
            dentro_circulo += 1
    fin = time.time() # finalizamos el tiempo
    
    pi_estimada = (dentro_circulo / num_puntos) * 4 # pi
    tiempo_ejecucion = fin - inicio
    
    return pi_estimada, iteraciones, tiempo_ejecucion

# aqui guardamos los datos en un archivo .txt con 5 datos
def guardar_resultados(iteracion, num_puntos, iteraciones, tiempo_ejecucion, pi_estimada):
    with open(f"iteracion{iteracion}.txt", "w", encoding="utf-8") as file:
        file.write(f"Iteración: {iteracion}\n")
        file.write(f"Número de puntos: {num_puntos}\n")
        file.write(f"Tiempo de ejecución: {tiempo_ejecucion:.6f} segundos\n")
        file.write(f"Número de iteraciones del bucle: {iteraciones}\n")
        file.write(f"Estimación de π: {pi_estimada}\n")

resultados = []

for i in range(1, 101): # haremos 100 iteraciones 
    num_puntos = i * 100  # cada iteración será 100 - 200 - 300 - etc.
    pi_estimada, iteraciones, tiempo_ejecucion = estimar_pi(num_puntos)
    resultados.append((i, num_puntos, iteraciones, tiempo_ejecucion))  # guardamos en una lista
    guardar_resultados(i, num_puntos, iteraciones, tiempo_ejecucion, pi_estimada)
    print(f"Ensayo {i}: {num_puntos} puntos, {iteraciones} iteraciones, {tiempo_ejecucion:.6f} segundos")

# una tabla con todos los datos
df = pd.DataFrame(resultados, columns=['Ensayo', 'Tamaño de Puntos', 'Iteraciones', 'Tiempo de Ejecución'])

print(df)

# GRAFICO
plt.figure(figsize=(10, 6))  # tamaño del grafico
plt.plot(df['Tamaño de Puntos'], df['Tiempo de Ejecución'], marker='o') # variables en el gráfico
plt.title('Tamaño de Puntos vs Tiempo de Ejecución') # titulo 
plt.xlabel('Tamaño de Puntos') # titulo X
plt.ylabel('Tiempo de Ejecución (segundos)') # titulo Y
plt.grid(True) # cuadrícula
plt.show()
