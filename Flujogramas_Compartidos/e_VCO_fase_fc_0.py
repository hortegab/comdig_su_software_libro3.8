
import numpy as np
from gnuradio import gr


class blk(gr.sync_block):  
    """Done by Homero Ortega Boada. Es un VCO dos entradas: 
in0 para manipular la fase, in1 para manipular la 
magnitud. En el fondo es el equivalente a un generador
de una senal exponencial compleja. Sobre la configuracion:
cada valor de la senal en in0 es interpretada como la fase
deseada en radianes. cada valor de in0, es la magnitud deseada"""

    def __init__(self): 
        gr.sync_block.__init__(self,
            name='e_VCO_fase_fc',
            in_sig=[np.float32, np.float32],
            out_sig=[np.complex64]
        )
    def work(self, input_items, output_items):
        in0=input_items[0]
        in1=input_items[1]
        out0=output_items[0]
        out0[:] = in1*np.exp(1.j*in0)
        return len(out0)
