import math
import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    """genera una senoidad cuyos parametros pueden ser manipulados por las senales entrantes asi: la primera senal manipula la amplitud; la segunda la frecuencia; la tercera la fase"""
    def __init__(self):  # only default arguments here
        gr.sync_block.__init__(
            self,
            name='VCO_hob',   # will show up in GRC
            in_sig=[np.float32, np.float32, np.float32],
            out_sig=[np.float32]
        )
        self.n_m=0 # guarda el ultimo valor de n

    def work(self, input_items, output_items):
        A=input_items[0]
        F=input_items[1]
        P=input_items[2]
        out=output_items[0]
        L=len(A)
        n=np.linspace(self.n_m, self.n_m+L-1,L)
        self.n_m += L
        out[:]=A*np.cos(2*math.pi*F*n+P)
        return len(out)
