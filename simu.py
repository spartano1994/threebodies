import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Definir los polinomios P1, P2, P3 y P4
def P1(x):
    return x**2 * (1 - (x + 1)**3)

def P2(x):
    return (1 - x**3) * (x + 1)**2

def P3(x):
    return (x + 1)**3 - x**3

def P4(x):
    return x**4 + 2*x**3 + x**2 + 2*x + 1

# Quíntica de Euler para m1=2, m2=1, m3=5
def f(x):
    return 2*P1(x) + 1*P2(x) + 5*P3(x)



# Derivada numérica de f(x)
def df(x, h=1e-6):
    return (f(x + h) - f(x - h)) / (2*h)

# Método de Newton-Raphson
def newton_raphson(x0, tol=1e-6, max_iter=100):
    x = x0
    for _ in range(max_iter):
        fx = f(x)
        if abs(fx) < tol:
            return x
        dx = -fx / df(x)
        x += dx
    raise ValueError("No converge")

# Encontrar la raíz (usamos x0=0.8 como guess inicial)
x_root = newton_raphson(0.8)

# Calcular las posiciones z_i
T1 = P1(x_root) / P4(x_root)
T2 = P2(x_root) / P4(x_root)
T3 = P3(x_root) / P4(x_root)

# Normalizar r12 = 1 (distancia entre cuerpo 1 y 2)
r12 = 1
z1 = T1 * r12
z2 = T2 * r12
z3 = T3 * r12

# Verificar centro de masa
m_total = 2 + 1 + 5
cm = (2*z1 + 1*z2 + 5*z3) / m_total



# Datos del ejemplo anterior (masas y posiciones z_i)
m1, m2, m3 = 2, 1, 5
z1 = -1.598745
z2 = -0.598745
z3 = 0.759247

# Calcular mu (potencial gravitatorio efectivo)
r12 = abs(z1 - z2)
r23 = abs(z2 - z3)
r13 = abs(z1 - z3)
mu = (m1*m2)/r12 + (m2*m3)/r23 + (m1*m3)/r13

# Calcular I (momento de inercia)
I = m1*z1**2 + m2*z2**2 + m3*z3**2

# Asumir J = 0 (movimiento puramente radial para simplificar)
J = 0

# Ecuación diferencial para R(t)
def R_dynamics(t, y):
    R, dRdt = y
    d2Rdt2 = -mu / R**2 + (J**2) / (I**2 * R**3)
    return [dRdt, d2Rdt2]

# Condiciones iniciales (R(0) = 1, dR/dt(0) = 0 para ejemplo)
R0 = 1.0
dRdt0 = 0.0
t_span = [0, 10]  # Intervalo de tiempo [0, 10]

# Resolver la EDO
sol = solve_ivp(R_dynamics, t_span, [R0, dRdt0], method='RK45', t_eval=np.linspace(0, 10, 1000))

# Extraer R(t) y Z_i(t)
R_t = sol.y[0]
Z1_t = R_t * z1
Z2_t = R_t * z2
Z3_t = R_t * z3
time = sol.t



# Datos del ejemplo anterior (masas y posiciones z_i)
m1, m2, m3 = 2, 1, 5
z1 = -1.598745
z2 = -0.598745
z3 = 0.759247

# Valores de R(t) y tiempo obtenidos previamente
# (Asumimos R(t) calculado con J=0 y condiciones iniciales R(0)=1, dR/dt(0)=0)
time = np.linspace(0, 10, 1000)
R_t = np.linspace(1, 0.1, 1000)  # Ejemplo de R(t) colapsando (ajustar según tus datos)

# Calcular posiciones Z_i(t)
Z1_t = R_t * z1
Z2_t = R_t * z2
Z3_t = R_t * z3






# Datos del ejemplo anterior (masas y posiciones z_i)
m1, m2, m3 = 2, 1, 5
z1 = -1.598745
z2 = -0.598745
z3 = 0.759247

# Parámetros del sistema
I = m1*z1**2 + m2*z2**2 + m3*z3**2  # Momento de inercia
mu = (m1*m2)/abs(z1 - z2) + (m2*m3)/abs(z2 - z3) + (m1*m3)/abs(z1 - z3)  # Potencial efectivo
J = 2.5  # Momento angular no nulo (para órbitas elípticas)

# Ecuaciones diferenciales para R(t) y ψ(t)
def dynamics(t, y):
    R, dRdt, psi = y
    d2Rdt = -mu/(I * R**2) + J**2/(I**2 * R**3)
    dpsidt = J/(I * R**2)
    return [dRdt, d2Rdt, dpsidt]

# Condiciones iniciales
R0 = 1.0      # R(0) = 1
dRdt0 = 0.0   # Velocidad radial inicial cero
psi0 = 0      # Ángulo inicial ψ(0) = 0
t_span = [0, 20]  # Intervalo de tiempo

# Resolver las EDOs
sol = solve_ivp(dynamics, t_span, [R0, dRdt0, psi0], method='RK45', t_eval=np.linspace(0, 20, 1000))
R_t = sol.y[0]
psi_t = sol.y[2]

# Calcular posiciones (x, y) para cada cuerpo
x1 = R_t * z1 * np.cos(psi_t)
y1 = R_t * z1 * np.sin(psi_t)
x2 = R_t * z2 * np.cos(psi_t)
y2 = R_t * z2 * np.sin(psi_t)
x3 = R_t * z3 * np.cos(psi_t)
y3 = R_t * z3 * np.sin(psi_t)





# Parámetros del sistema
m1, m2, m3 = 2, 1, 5
z1 = -1.598745
z2 = -0.598745
z3 = 0.759247

# Constantes dinámicas
I = m1*z1**2 + m2*z2**2 + m3*z3**2
mu = (m1*m2)/abs(z1 - z2) + (m2*m3)/abs(z2 - z3) + (m1*m3)/abs(z1 - z3)
J = 3.0  # Momento angular

# Resolver ecuaciones diferenciales (CORRECCIÓN APPLICADA)
def dynamics(t, y):
    R, dRdt, psi = y
    d2Rdt = (-mu/I)/R**2 + (J**2/I**2)/R**3  # Usar ** para potencias
    dpsidt = J/(I * R**2)                      # Operador corregido aquí
    return [dRdt, d2Rdt, dpsidt]

# Resolver el sistema
sol = solve_ivp(dynamics, [0, 30], [1.0, 0.0, 0], 
                t_eval=np.linspace(0, 30, 200))

# Resto del código sin cambios...
R_t = sol.y[0]
psi_t = sol.y[2]

x1 = R_t * z1 * np.cos(psi_t)
y1 = R_t * z1 * np.sin(psi_t)
x2 = R_t * z2 * np.cos(psi_t)
y2 = R_t * z2 * np.sin(psi_t)
x3 = R_t * z3 * np.cos(psi_t)
y3 = R_t * z3 * np.sin(psi_t)

# Configurar figura
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.grid(True)
ax.set_aspect('equal')
ax.set_title('Animación del movimiento colineal de Euler')

# Elementos de la animación
cm = ax.scatter([0], [0], c='black', marker='*', s=200)
body1, = ax.plot([], [], 'ro', ms=10, alpha=0.8)
body2, = ax.plot([], [], 'go', ms=8, alpha=0.8)
body3, = ax.plot([], [], 'bo', ms=12, alpha=0.8)
trace1, = ax.plot([], [], 'r-', lw=1, alpha=0.4)
trace2, = ax.plot([], [], 'g-', lw=1, alpha=0.4)
trace3, = ax.plot([], [], 'b-', lw=1, alpha=0.4)

def init():
    body1.set_data([], [])
    body2.set_data([], [])
    body3.set_data([], [])
    trace1.set_data([], [])
    trace2.set_data([], [])
    trace3.set_data([], [])
    return body1, body2, body3, trace1, trace2, trace3, cm

def update(frame):
    # Actualizar cuerpos como secuencias
    body1.set_data([x1[frame]], [y1[frame]])
    body2.set_data([x2[frame]], [y2[frame]])
    body3.set_data([x3[frame]], [y3[frame]])
    
    # Actualizar trayectorias
    trace1.set_data(x1[:frame+1], y1[:frame+1])
    trace2.set_data(x2[:frame+1], y2[:frame+1])
    trace3.set_data(x3[:frame+1], y3[:frame+1])
    
    return body1, body2, body3, trace1, trace2, trace3, cm

ani = FuncAnimation(fig, update, frames=len(x1),
                    init_func=init, blit=True, interval=200)

plt.legend([body1, body2, body3, cm],
           [f'Cuerpo 1 (m={m1})', f'Cuerpo 2 (m={m2})',
            f'Cuerpo 3 (m={m3})', 'Centro de masa'],
           loc='upper right')
plt.show()