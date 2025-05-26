
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

    def norm3(self):
        return (self.x**2 + self.y**2)**1.5 

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

    @staticmethod
    def law2( body1 , force ):
        return force * (1/body1.mass)  

    @staticmethod
    def law4( body1 , body2 ):
        #Fuerza que siente el cuerpo 1 debido al cuerpo 2
        r_12 = body1.position - body2.position
        f = r_12*( (-G*body1.mass*body2.mass)/r_12.norm3())
        return f

    def mass_center(self , cuerpos):
        total_mass = 0
        center = Vector(0,0,0)

        for body in cuerpos:
            total_mass += body.mass
            center += body.position * body.mass

        return center / total_mass
    
    def update_position( position0 , velocity0 , a , t_step ):
        return position0 + velocity0 * t_step + a*0.5*t_step**2
    
    def update_velocity( velocity0 , a , t_step ):
        return velocity0 + a*t_step
        


class Body:
    def __init__(self , label, x , y  , mass , vx , vy ,
                 aceleration = Vector(0,0) ):
        self.position = Vector(x,y)
        self.mass = mass
        self.velocity = Vector(vx,vy)
        self.aceleration = aceleration
    
    def x(self):
        return self.position.x
    
    def y(self):
        return self.position.x
    
    def change_position(self,new_x, new_y):
        self.position = Vector(new_x, new_y)

    def change_velocity( self, new_vx , new_vy ):
        self.velocity = Vector( new_vx , new_vy )

    def change_aceleration( self , new_ax , new_ay ):
        self.aceleration = Vector( new_ax , new_ay )
    
    def __str__(self):
        return f"{self.label} = {self.mass}kg , position = {self.position} , velocity = {self.velocity}, aceleration = {self.aceleration}"
    

G = 0.6