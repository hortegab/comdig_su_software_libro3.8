
#SE IMPORTAN LAS LIBRERIAS NECESARIAS PARA PODER IMPLEMENTAR EL PLL

import numpy as np
import pdb
from gnuradio import gr


class blk(gr.sync_block):

    def __init__(self, lf_bandwidth=0.002):  # SE DECLARAN LOS ARGUMENTOS DE LA ENTRADA
        
        gr.sync_block.__init__(
            self,
            name='PLL_H',   # will show up in GRC
            in_sig=[np.complex64],
            out_sig=[np.complex64]
        )
        #LOS ATRIBUTOS POR DEFECTO
	self.phase_out = 0.0
	self.freq_out = 0.0
	self.vco = np.exp(1j*self.phase_out)
	self.phase_difference = 0.0
        self.bw = lf_bandwidth
        self.beta = np.sqrt(lf_bandwidth)        
        self.lf_bandwidth = lf_bandwidth
		
    def update_phase_estimate(self):
        self.vco = np.exp(1j*self.phase_out)

    def update_phase_difference(self, in_sig):
        self.phase_difference = np.angle(in_sig*np.conj(self.vco))

    def step(self, in_sig):
	#TOMA LA MUESTRA INSTANTANEA DE LA SENAL, AL ESTADO DEL PLL        
        self.update_phase_difference(in_sig)
        self.freq_out += self.bw * self.phase_difference
        self.phase_out += self.beta * self.phase_difference + self.freq_out
        self.update_phase_estimate()

##############################

    def work(self, input_items, output_items):
    
  	self.step(input_items[0])
	output_items[0][:] = self.vco
 	return len(output_items)









