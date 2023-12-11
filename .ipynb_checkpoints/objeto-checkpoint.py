from funciones import *
from librerias import *

class vector():
    def __init__(self,x,y,i=1,j=1):
        self.vector      = np.array([x,y])
        self.vector_base = np.array([i,j])
        self.fig = crear_figura(self.vector, self.vector_base)
        self.vector_i = np.array([1,0])
        self.vector_j = np.array([0,1])
        
        
    def __add__(self, otro_objeto):
        if isinstance(otro_objeto, vector):
            fig_suma = crear_figura_suma(self.vector, otro_objeto,self.vector_base)
            fig_suma.show()
            lista_other   = list(self.vector + otro_objeto.vector)
            return vector(lista_other[0],lista_other[1])
        else:
            raise TypeError("No se puede sumar con un objeto de otra clase")
            
    def __mul__(self, otro_objeto):
        if isinstance(otro_objeto, (int, float)):
            lista_other = list(self.vector * otro_objeto)
            return vector(lista_other[0],lista_other[1])
        else:
            raise TypeError("No se puede multiplicar con un objeto de otra clase") 
            
    def mostrar(self):
        self.fig.show()
        
    def subespacio(self, otro_objeto):
        if np.all(np.cross(self.vector, otro_objeto.vector) == 0):
            fig_em = espacio_muestral()
            fig_em.show()
            print("Espacio limitado, dado que existe colinealidad entre los vectores")            
            
        else:
            fig_em = espacio_muestral("global")
            fig_em.show()
            print("Todo el plano, dado que no existe colinealidad entre los vectores")
            
    def transformación_lineal(self,vec_i = [1,0], vec_j = [0,1]):
        fig_inicial = transformacion_lineal(vec_i, vec_j )
        fig_inicial.show()
        