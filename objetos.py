
import numpy as np
import matplotlib.pyplot as plt


class Vector:
    def __init__(self , x , y ):
        self.x = x
        self.y = y

    def __add__(self , other):
        return Vector(self.x + other.x , self.y + other.y)

    def __sub__(self , other):
        return Vector(self.x - other.x , self.y - other.y )

    def __mul__(self , other):
        return Vector(self.x * other , self.y * other )

    def __str__(self):
        return f"({self.x} , {self.y})"

    def norm(self):
        return (self.x**2 + self.y**2 )**0.5

    def norm2(self):
        return self.x**2 + self.y**2 

    def normalize(self):
        return self / self.norm()

    def dot(self , other):
        return self.x * other.x + self.y * other.y 

    def __eq__(self , other):
        return self.x == other.x and self.y == other.y 

    def __iadd__(self , other):
        self.x += other.x
        self.y += other.y
        return self

    def __isub__(self , other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __imul__(self , other):
        self.x *= other
        self.y *= other
        return self

    def __itruediv__(self , other):
        self.x /= other
        self.y /= other
        return self

    def __neg__(self):
        return Vector(-self.x , -self.y )

    def __abs__(self):
        return self.norm()


class Newton_mechanics:
    def __init__(self):
        pass

    G = 0.6

    @staticmethod
    def law2( body1 , force ):
        return force / body1.mass

    @staticmethod
    def law4( body1 , body2 ):
        #Fuerza que siente el cuerpo 1 debido al cuerpo 2
        r_12 = body1.position - body2.position
        f = ( (G*body1.mass*body2.mass)/r_12.norm2())*r_12.normalize()
        return f

    def mass_center(self , cuerpos):
        total_mass = 0
        center = Vector(0,0,0)

        for body in cuerpos:
            total_mass += body.mass
            center += body.position * body.mass

        return center / total_mass
    
    def a_constant( i_position , i_velocity , a , t_step):
        return i_position + i_velocity * t_step + a*0.5*t_step**2
        
    



class body:
    def __init__(self , x , y  , mass , vx , vy ,
                 aceleration = Vector(0,0) ):
        self.position = Vector(x,y)
        self.mass = mass
        self.velocity = Vector(vx,vy)
        self.aceleration = aceleration
    
    

