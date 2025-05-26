import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.collections import LineCollection
from objetos import *

# Creación de las masas
bodies = [
    Body( "m_1" , 25 , 25, 10 , 0.1 , 0.1 ),
    Body( "m_2" , 12 , 20, 11 , 0.2 , 0.7 ),
    Body( "m_3" , 37 , 9, 12 , 0.1 , -0.5 ) ]

# Posiciones iniciales (todas en (1,1))
positions = np.array([[25 , 25] , [12 , 20] , [37 , 9 ]])

# Configuración inicial
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_xlim(0, 50)
ax.set_ylim(0, 50)
ax.set_aspect('equal')
ax.grid(True)
ax.set_title('Problema de los tres cuerpos')

# Ángulos de movimiento (en grados)
colors = ['red', 'green', 'blue']
labels = ['$m_1$', '$m_2$', '$m_3$']

# Listas para almacenar las trayectorias (para las estelas)
trajectories = [[] for _ in bodies]

# Crear puntos iniciales
points = [ax.plot([], [], 'o', color=colors[i], label=labels[i])[0] for i in range(len(bodies))]
ax.legend()

# Crear colecciones de líneas para las estelas
line_segments = [LineCollection([], colors=colors[i], linewidths=1, alpha=0.5) for i in range(len(bodies))]
for line in line_segments:
    ax.add_collection(line)

def init():
    for point in points:
        point.set_data([], [])
    for line in line_segments:
        line.set_segments([])
    return points + line_segments

def update(frame):
    global positions
    
    # Actualizar posiciones
    for i in range(len(bodies)):
        first_index = (i+1)%3
        F1 = Newton_mechanics.law4( bodies[i] , bodies[first_index] )
        second_index = (i+2)%3
        F2 = Newton_mechanics.law4( bodies[i] , bodies[second_index])
        F = F1+F2

        a = Newton_mechanics.law2( bodies[i] , F  )

        # Calcular nuevo punto 1
        new_x = Newton_mechanics.update_position( bodies[i].position , bodies[i].velocity , a , t_step=0.5 ).x
        new_y = Newton_mechanics.update_position( bodies[i].position , bodies[i].velocity , a , t_step=0.5 ).y
        positions[i] = [new_x, new_y]

        new_vx = Newton_mechanics.update_velocity(bodies[i].velocity, a , t_step=0.5).x
        new_vy = Newton_mechanics.update_velocity(bodies[i].velocity, a , t_step=0.5).y



        #Actualiza nuevas velocidades y posiciones en el objeto Body
        bodies[i].change_position( new_x , new_y )
        bodies[i].change_velocity(new_vx , new_vy )

        
        # Añadir a la trayectoria
        trajectories[i].append(positions[i].copy())
        
        # Actualizar punto (usando listas para x e y)
        points[i].set_data([new_x], [new_y])
        
        # Actualizar estela (mostrar solo los últimos 20 puntos)
        if len(trajectories[i]) > 1:
            segments = np.array([trajectories[i][j:j+2] for j in range(len(trajectories[i])-1)])
            line_segments[i].set_segments(segments[-20:])  # Limitar la longitud de la estela
    
        # Ajustar límites si los puntos se salen del área visible
    if np.any(positions > 9) or np.any(positions < 1):
        ax.set_xlim(min(1, *positions[:, 0]-1), max(10, *positions[:, 0]+1))
        ax.set_ylim(min(1, *positions[:, 1]-1), max(10, *positions[:, 1]+1))
    
    return points + line_segments

# Crear la animación
ani = FuncAnimation(fig, update, frames=800, init_func=init, 
                    blit=True, interval=50)

plt.show()