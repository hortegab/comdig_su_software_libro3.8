"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
import math
from gnuradio import gr


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """
Es un canal AWGN (Additive White Gaussian Noise, en banda base), con entrada vectorial. Recibe la envolvente compleja de una senal con modulacion digital. Entrega la misma senal recibida pero con ruido blanco gausiano aditivo con diferentes valores de potencia que corresponden a N diferentes valores de Es/No entre EsNOmin y EsN0max (valores dados en dB). Este bloque se diferencia de otros bloques tradicionales de canal AWGN en lo siguiente: Tiene internamente una funcion que mide la potencia promedio de la senal entrante Ps, de modo que puede calcular Es=Ps/Rs; de esa manera puede N valores de potencia Pn para el ruido Pn para lograr los N valores de la relacion Es/No. Con esto ha completado el primer ensayo para que otro sea el bloque que calcule la Curva de SER. Pero alli no para, sino que sigue realizando tantos ensayos como lo permita el tiempo de simulacion, para que el bloque que calcula la Curva de BER la pueda ir perfeccionando cada vez mas.

Datos de configuracion del bloque:
N: Es la longitud del vector y coincide con el numero de puntos discretos que va a tener la curva de BER. Tambien corresponde al numero de valores que tomará la relacion Es/No
EsN0min: El minimo valor a tener en cuenta para Es/No
EsN0max: El maximo valor a tener en cuenta para Es/No
Rs: es la rata de simbolos.
Sps: El numero de muestras por simbolo. Usualmente es 1, pero pueden darse excepciones. 
Es: es la energia de un simbolo

Algunas variables internas son:
No: es la Densidad espectral del potencia del ruido blanco.
SNR: es la relacion senal a ruido
"""


    def __init__(self, N=32, EsN0min=0, EsN0max=16,Sps=1,Rs=1):  # only default arguments here
        """ """
        gr.sync_block.__init__(
            self,
            name='e_SER_Channel',   # will show up in GRC
            in_sig=[(np.complex64,N)],
            out_sig=[(np.complex64,N)]
        )
        samp_rate=Rs*Sps
        EsN0dB=np.linspace(EsN0min,EsN0max,N)
        EsN0=pow(10.,EsN0dB/10.) 
        self.SNR=EsN0*Rs/samp_rate
        
        
    def work(self, input_items, output_items):
        L=len(input_items[0]) # la entrada en una matrix de L filas y N columnas
        SNR_matrix=np.array([self.SNR]*L) # convertimos SNR a matrix
        P_s=np.mean(np.absolute(input_items[0])**2)  # La potencia de la senal
        P_n = P_s/SNR_matrix                    # la potencia del ruido
        output_items[0][:] = input_items[0]+noise_c(np.sqrt(P_n))
        #output_items[0][:] = input_items[0]*1.5
        return len(output_items[0])
        
def noise_c(Vrms):
    # random.normal() pide la desviacion standard pero es el mismo Valor RMS
    # Vrms es el Valor RMS de la Envolvente compleja del ruido, pero la vamos
    # a generar como un ruido real mas un ruido imaginario. Pero esas dos
    # senales tienen un valor RMS un tanto diferente: Vrms_q=Vrms/math.sqrt(2.)
    Vrms_q= Vrms/math.sqrt(2.)
    n= np.random.normal(0.,Vrms_q)+np.random.normal(0.,Vrms_q)*1.j
    return n 
