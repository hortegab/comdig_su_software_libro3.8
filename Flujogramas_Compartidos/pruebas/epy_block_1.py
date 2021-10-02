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
        self.N=N
        self.errores = np.float64(np.zeros(self.N)) # N contadores de errores.
        self.count=1 # contador de curvas procesadas
        # self.SER=np.ones(self.N) #N puntos de la ultima curva calculada


    def work(self, input_items, output_items):
        in0=input_items[0]
        in1=input_items[1]
        L=len(in0) # numero de vectores  de N elementos
        errores_matrix = self.errores+(in0!=in1).astype(int)
        SER = errores_matrix/self.count # count no esta subiendo de 1 en 1, sino de L en L pero el ojo no va a notar los saltos.
        self.count +=L
        self.errores=errores_matrix[L-1]
        output_items[0][:]=SER
        #output_items[0][:]=np.log10(SER)
        return len(output_items[0])
