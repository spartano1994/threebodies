import numpy as np
import matplotlib.pyplot as plt
import pygame 
from objetos import *


body1 = body( x = 128 , y = 256 , mass = 25 , vx =  7 , vy = 1  )
body2 = body( x = 400 , y = 580 , mass = 7 , vx =  -2 , vy = -4  ) 
body3 = body( x = 128 , y = 256 , mass = 20 , vx =  -2 , vy = 5  ) 

img_body1 = pygame.image.load( "./images/mercurio.png" )
img_body2 = pygame.image.load( "./images/neptuno.png" )
img_body3 = pygame.image.load( "./images/venus.png" )


# iniciar pygame		
pygame.init()

# crear la pantalla
pantalla = pygame.display.set_mode( ( 800 , 600 ) ) 
	
# título e ícono
pygame.display.set_caption( "Tres cuerpos" )
icono = pygame.image.load( "./images/planeta.png" )
pygame.display.set_icon( icono )
	
#Colocar cuerpos en la pantalla
def cuerpo1( x , y ):
	pantalla.blit( img_body1 , ( x, y ) )
		
def cuerpo2( x , y ):
	pantalla.blit( img_body2 , ( x, y ) )

def cuerpo3( x , y ):
	pantalla.blit( img_body3 , ( x, y ) )
		
# fondo de pantalla
fondo = pygame.image.load( "./images/espacio.jpg" )
     

cuerpo1( 1,2 )
cuerpo2( 1,2 )
cuerpo3( 1,2 )


# loop de la simulación
ejecucion = True
    
while ejecucion:
    pantalla.blit( fondo , ( 0 , 0 ))

    for evento in pygame.event.get():
        # evento cerrar
        if evento.type == pygame.QUIT:
            ejecucion = False

            
    # modificar ubicación del jugador
    jugador_x += jugador_x_cambio
    jugador_y += jugador_y_cambio

    jugador( jugador_x , jugador_y )

    mostrar_puntaje( texto_x , texto_y )

    # actualizar
    pygame.display.update()