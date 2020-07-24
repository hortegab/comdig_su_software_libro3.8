"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Gray Code Converter. Supongamos que tienes una senal dada en simbolos M_PAM, pero necesitas que esos valores M-PAM se expresen en codigo Gray. Esta seria la solucion"""

    def __init__(self):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Gray Decoder',   # will show up in GRC
            in_sig=[np.int8],
            out_sig=[np.int8]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
    def gray_decoder(n):
        inv=0
        while(n):
            inv=inv^n
            n=n>> 1
        return inv

    def work(self, input_items, output_items):
        """la conversion a gray code"""
        output_items[0][:] = gray_decoder(input_items[0])
        return len(output_items[0])
