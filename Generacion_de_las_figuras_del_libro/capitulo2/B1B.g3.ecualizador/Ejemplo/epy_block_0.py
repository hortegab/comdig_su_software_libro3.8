"""
Embedded Python Blocks:

Each this file is saved, GRC will instantiate the first class it finds to get
ports and parameters of your block. The arguments to __init__  will be the
parameters. All of them are required to have default values!
"""
import numpy as np
from gnuradio import gr
class blk(gr.sync_block):

    def __init__(self,taps=5,gain=0.5,train=20):  #Parametros por defecto
        gr.sync_block.__init__(
            self,
            name='Ecualizador LMS Final',
            in_sig=[np.complex64,np.complex64], #Dos entradas, una para referencia y una para canal
            out_sig=[np.complex64]
        )
	#Declaracion del vector de pesos 'w' con ancho del numero de taps
	self.w=np.zeros((taps,1),dtype=np.complex64)
	#Declaracion del valor alpha, representa la velocidad de aprendizaje
	self.alpha=gain
	#Declaracion del numero taps, representa la longitud del vector de pesos
	self.N=taps
	#Declaracion de la cantidad de entrenamiento a realizar
	self.train=train
	#Contador encargado de limitar el ciclo de entrenamiento
	self.count=0 

    def work(self, input_items, output_items,):
	#Entrada de la senal del canal
	x=input_items[0]
	#Entrada de la senal de referencia
	d=input_items[1]
	if(self.count<=self.train): 		#Mientras el contador sea menor a el valor de entrenamiento se mantiene entrenando
		#print 'Entrada entrenamiento'
		for i in range(self.N,len(x)):
			xt=x[(i-self.N):i]	#Seleccion de una muestra de la senal del canal, del mismo tamano del vector de pesos
			y=self.w.T.dot(xt)	#Producto punto entre el vector de pesos y la muestra del canal (Convolucion)
			e=d[i-1]-self.w.T.dot(xt) 	#Calculo del error, entre la senal de referencia y la salida calculada	
			w1 = self.w.T + self.alpha*(e*(xt.conjugate())) #Actualizacion del vector de pesos basada en el error
			self.w=w1.T		#Correcion de la forma del vector de pesos
				
	else:	
		for i in range(self.N,len(x)):
			#print 'Entrada convolucion'
			xt=x[(i-self.N):i]	#Seleccion de una muestra de la seal del canal
			y=self.w.T.dot(xt)	#Producto punto entre el vector de pesos YA ENTRENADO y la muestra del canal (Convolucion)
						#Como ya esta entrenado no es necesario calcular el error nuevamente, solo usar el vector
			output_items[0][i]=y[0]	#Entrega de datos a la salida del ecualizador
	#print self.count
	self.count=self.count+1 		#Aumento del conteo
        return len(output_items[0])
