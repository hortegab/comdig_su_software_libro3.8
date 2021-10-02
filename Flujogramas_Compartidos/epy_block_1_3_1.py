"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """sss"""

    def __init__(self, N=32):  # only default arguments here
        """ """
        gr.sync_block.__init__(
            self,
            name='e_SERtool',   # will show up in GRC
            in_sig=[(np.int8,N),(np.int8,N)],
            out_sig=[(np.float32,N)]
        )
        
        # N: Una curva de SER tiene N puntos
        # cada vez que se procesan N puntos es un ensayo
        # count: cuenta los ensayos procesados
        # errores: vector de N valores para contar errores en
        # cada punto de la SER a medida que ocurren nuevos ensayos.
        
        self.N=N
        self.errors_N = np.zeros(self.N) 
        self.count_trials=int(1) 
        
    def work(self, input_items, output_items):
        # in0  y in1: son matrices de LxN
        # L: numero de vectores  de N elementos de matrix LxN
        # osea, vamos a procesar a la vez L curvas de SER y cada una tiene N puntos
                                
        in0=input_items[0]
        in1=input_items[1]
        out=output_items[0]
        L=len(in0) 
        self.count_trials +=L # ajusta la cantidad de curvas ya procesadas
        
        errores_LxN = (in0!=in1).astype(int) # deteccion de errores en toda la matrix LxN
        self.errors_N += np.sum(errores_LxN, axis=0) # vector acumula suma de columnas de matrix
        SER = self.errors_N/self.count_trials # obtengo la SER como un vector
        
        out[:]=SER # lleno la matrix out con el vector SER, entonces una SER
                   # sale L veces pero el ojo humano no lo notará
        return len(output_items[0])
