from eyediagram.mpl import eyediagram
import matplotlib.pyplot as plt
import scipy 
import numpy as np

# Configuracion del Diagrama de Ojo
# Ndat: Es el numero de datos a graficar
# Sps: El numero de muestras por simbolo del archivo generado en gnuradio
Ndat=100000 
Sps = 8

# Leemos el archivo producido por gnuradio
y0=scipy.fromfile(open("senal0"), dtype=scipy.float32) 
y1=scipy.fromfile(open("senal1"), dtype=scipy.float32) 

#Escogemos una porcion de datos para graficar
y0=(y0[0:Ndat])
y1=(y1[0:Ndat])


#Grafica0
eyediagram(y0, 2*Sps, offset=16, cmap=plt.cm.coolwarm)
plt.title("Entrada")
plt.show()

#Grafica1
eyediagram(y1, 2*Sps, offset=16, cmap=plt.cm.coolwarm)
plt.title("Salida")
plt.show()


