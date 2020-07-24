# this module will be imported in the into your flowgraph
import numpy
import math
#######################################################
##        Done by Homero Ortega Boada              ##
##        comdiguis@saber.uis.edu.co                 ##
##     Universidad Industrial de Santander           ##
#######################################################
#######################################################
##       Constellation map  identification           ##
#######################################################                  
# Constellation points are analyzed to determine the 
# the map used for ordering of the constellation points
def sum_modulus(a,b,modulus):
    # realiza una suma de a y b en modulo modulus
    return (a+b)%modulus

def angle_map(constellation_points):
    # esta funcion entrega todos los angulos positivos entre 0 y 2pi
    angles=numpy.angle(constellation_points)
    return sum_modulus(angles, 2*math.pi, 2*math.pi)

def inverse_map(constellation_points):
    M=len(constellation_points)
    angles=angle_map(constellation_points)
    angles=sum_modulus(angles,-angles[0], 2*math.pi) # giro a agulo cero
    delta_angle= 2*math.pi/M     # angulo entre puntos
    cod_inv=numpy.round(angles/delta_angle)
    cod_inv=cod_inv.astype(numpy.int) #conversion a entero 
    return cod_inv

def direct_map(constellation_points):
    M=len(constellation_points)
    codinv=inverse_map(constellation_points)
    coddirect=numpy.array([0]*M)
    for j in range(M):
        temp=numpy.where(codinv==j)
        coddirect[j]=temp[0][0]
    return coddirect

""" # SECCION DE PRUEBAS DEL CODIGO
import gnuradio.digital as digital
constelacion=digital.constellation_8psk().points()
print("constelacion = ", constelacion)
mapdirect=direct_map(constelacion)
print("codigo directo = ", mapdirect)
mapinverse=inverse_map(constelacion)
print("codigo inverso = ", mapinverse)
"""






