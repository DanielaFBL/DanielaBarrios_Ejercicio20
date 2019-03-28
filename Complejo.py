import unittest
import complejo
import math
import numpy as np

class Complejo():
    
    def __init__(self, imaginario, real):
        self.imaginario = Im
        self.real = Re
        self.norma=np.sqrt(Im**2+Re**2)
        
    def conjugado(self):
        self.imaginario=-self.imaginario
        
    def calcula_norma(self):
        self.norma = np.sqrt(Im**2+Re**2)
        
    def pow(self, potencia):
        return self.imaginario**potencia