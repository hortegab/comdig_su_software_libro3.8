from eyediagram.demo_data import demo_data
from eyediagram.mpl import eyediagram
import matplotlib.pyplot as plt
import scipy 
import numpy as np


f=scipy.fromfile(open("datos"), dtype=scipy.float32) #Importamos los datos desde GNU RADIO
fp=(f[0:10000]) #ESCOJEMOS UN INTERVALO DE ESTOS DATOS , PUEDE SER CUALQUIERA RESPETANDO LA CANTIDAD DE MUESTRAS
#plt.plot(fp) #GRAFICA DE LOS DATOS RECIBIDOS
samples_per_symbol = 8 #SPS
eyediagram(fp, 2*samples_per_symbol, offset=16, cmap=plt.cm.coolwarm)
#plt.plot(fp)
plt.show()




