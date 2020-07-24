import math
import numpy as np
# Cada funcion siguinete es una forma de pulso para una senal digital
# Los parametros comunmente usados son:
# Sps (Samples per simbol): Duracion de un simbolo en tiempo discreto
# ntaps: es el numero de muestras a generar por simbolo. Esto debido a que,
# en la practica, un simbolo puede invadir a otros simbolos (ISI), asi que
# las muestras de un simbolo se pueden expandir mas alla de Sps

# Bipolar non return to zero level signal
def B_NRZ_L(Sps):
    return Sps*[1.,]
##  Forma sinc 
def sinc(Sps,ntaps):
    n=np.linspace(-int(ntaps/2), int(ntaps/2-1),ntaps)
    h=np.sinc(n/Sps)
    return h
# forma diente se sierra
def saw(Sps):
    return np.linspace(0,Sps-1,Sps)	
# Bipolar non return to zero signal
def RZ(Sps):
    h=Sps*[1.,]
    Sps_m=int(Sps/2)
    h[Sps_m+1:Sps:1]=np.zeros(Sps-Sps_m)
    return h

