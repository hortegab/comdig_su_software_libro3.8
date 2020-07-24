# Copyright (c) 2015, Warren Weckesser.  All rights reserved.
# This software is licensed according to the "BSD 2-clause" license.


from eyediagram.demo_data import demo_data
from eyediagram.mpl import eyediagram
import matplotlib.pyplot as plt


#Generamos senal de ejemplo  
num_symbols = 1000
samples_per_symbol = 24
y = demo_data(num_symbols, samples_per_symbol)

#Llamamos el modulo que instalamos
eyediagram(y, 2*samples_per_symbol, offset=16, cmap=plt.cm.coolwarm)

#Graficamos
#plt.plot(y)
plt.show()
