"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Hecho por Homoero Ortega. Es un acumulador puro, va acumulando cada muestra entrante mientras entrega lo que lleva acumulado hasta el momento. Puede convertirse en un integrador si la salida se divide en la frecuencia de muestreo de la senal"""

    def __init__(self):  # only default arguments here
        gr.sync_block.__init__(
            self,
            name='e_Accum_ff',   # will show up in GRC
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
	self.memory=0.
    def work(self, input_items, output_items):
        """El acumulador"""
	in0=input_items[0]
	out0=output_items[0]
        L=len(in0)
	out0[:]=(self.memory+np.cumsum(in0))
	self.memory=out0[L-1]
        return len(out0)
