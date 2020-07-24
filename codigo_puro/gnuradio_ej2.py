#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# Nota: este codigo esta guardodo como gnuradio_ej2.py en:
# https://sites.google.com/saber.uis.edu.co/comdig/sw
##################################################

###########################################################
###           IMPORTACION DE LIBRERIAS                  ###
###########################################################

# Libreria obligatoria
from gnuradio import gr

# Librerias particulares
from gnuradio import analog
from gnuradio import blocks
from gnuradio.filter import firdes

# Librerias para poder incluir graficas tipo QT
from gnuradio import qtgui
from PyQt4 import QtGui as Qt # si no se acepta PyQt4 cambia esto por: from PyQt5 import Qt
import sys, sip

###########################################################
###           LA CLASE DEL FLUJOGRAMA                   ###
###########################################################
class flujograma(gr.top_block):
    def __init__(self):
        gr.top_block.__init__(self)

        # Para que lo nuestro sea considerado una aplicación tipo QT GUI
        self.qapp = Qt.QApplication(sys.argv) 

        ################################################
        ###   EL FLUJOGRAMA                          ###
        ################################################

        # Las variables
        samp_rate = 1e6
        fftsize = 2048

        # Los bloques
        self.src = analog.sig_source_c(samp_rate, analog.GR_SIN_WAVE, 0.1, 1, 0)
        self.nse = analog.noise_source_c(analog.GR_GAUSSIAN, 0.1)
        self.add = blocks.add_cc()
        self.thr = blocks.throttle(gr.sizeof_gr_complex, samp_rate, True)
        self.snk = qtgui.sink_c(
            fftsize, #fftsize
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
        )

        # Las conexiones
        self.connect(self.src, (self.add, 0))
        self.connect(self.nse, (self.add, 1))
        self.connect(self.add, self.thr, self.snk)

        # La configuracion para graficar
        self.pyobj = sip.wrapinstance(self.snk.pyqwidget(), Qt.QWidget)
        self.pyobj.show()

###########################################################
###                LA CLASE PRINCIPAL                   ###
###########################################################
def main():
    simulador_de_la_envolvente_compleja = flujograma()
    simulador_de_la_envolvente_compleja.start()
    simulador_de_la_envolvente_compleja.qapp.exec_()

# Codigo usado para lanzar el main() preveniendo fallas e interrupciones
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
