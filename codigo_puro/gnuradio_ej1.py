#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# Nota: este codigo esta guardodo como gnuradio_ej1.py en:
# https://sites.google.com/saber.uis.edu.co/comdig/sw
##################################################

##################################################
# LO QUE HAY QUE IMPORTAR
##################################################
from gnuradio import gr
from gnuradio import audio
from gnuradio import analog

#######################################################
# LA CLASE QUE DESCRIBE TODO EL FLUJOGRAMA
######################################################
class my_top_block(gr.top_block):        # hereda de gr.top_block
     def __init__(self):
         gr.top_block.__init__(self)     # otra vez la herencia
  
         sample_rate = 32000
         ampl = 0.1
 
         src0 = analog.sig_source_f(sample_rate, analog.GR_SIN_WAVE, 350, ampl)
         src1 = analog.sig_source_f(sample_rate, analog.GR_SIN_WAVE, 440, ampl)
         dst = audio.sink(sample_rate, "")
         self.connect(src0, (dst, 0))
         self.connect(src1, (dst, 1))
#######################################################
# EL CÓDIGO PARA LLAMAR EL FLUJOGRAMA “my_top_block”
######################################################
my_top_block().run()

#if __name__ == '__main__':
#    try:
#         my_top_block().run()
#    except [[KeyboardInterrupt]]:
#         pass
