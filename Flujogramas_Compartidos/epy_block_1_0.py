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
        self.errores = np.float64(np.zeros(self.N)) 
        self.count=1 
        
    def work(self, input_items, output_items):
        # in0  y in1: son matrices de LxN
        # L: numero de vectores  de N elementos de matrix LxN
        # osea, vamos a procesar a la vez L curvas de SER y cada una tiene N puntos
        # count_vec: es para tener un contador para a cada curva de SER en la matrix
        # le corresponda el contador apropiado. count_vect es una matrix de Lx1
                        
        in0=input_items[0]
        in1=input_items[1]
        L=len(in0) 
        count_vec=np.arange(self.count,self.count+L)
        count_matrix=np.transpose(np.array([count_vec]*self.N))
        errores_matrix = self.errores+(in0!=in1).astype(int)
        SER = errores_matrix/count_matrix # aqui se presenta error a dividir una matrix por un vector
        self.count +=L 
        self.errores=errores_matrix[L-1] 
        output_items[0][:]=SER
        return len(output_items[0])
