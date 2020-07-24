#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: SER Simulation
# Author: Homero Ortega Boada
# Description: dale un valor a Eb/No, corre el flujograma y obten la SER. Puedes sacar tantos valores como para construir una curva de SER
# Generated: Thu May  9 16:35:25 2019
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import BER
import math
import numpy
import sip
import sys
from gnuradio import qtgui


class ser_simulation(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "SER Simulation")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("SER Simulation")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "ser_simulation")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.const = const = [(1+1.j)/4.24,(3+1.j)/4.24,(3+3.j)/4.24,(1+3.j)/4.24,(-1+1.j)/4.24,(-3+1.j)/4.24,(-3+3.j)/4.24,(-1+3.j)/4.24,(-1-1.j)/4.24,(-3-1.j)/4.24,(-3-3.j)/4.24,(-1-3.j)/4.24,(1-1.j)/4.24,(3-1.j)/4.24,(3-3.j)/4.24,(1-3.j)/4.24]
        self.M = M = len(const)
        self.samp_rate = samp_rate = 100e3
        self.run_stop = run_stop = True

        self.MiconstellationObject = MiconstellationObject = digital.constellation_calcdist((const), (), 4, 1).base()

        self.MaxErrors = MaxErrors = 1e3
        self.MaxCount = MaxCount = int(1e7)
        self.EbN0 = EbN0 = 28
        self.Bps = Bps = int(math.log(M,2))

        ##################################################
        # Blocks
        ##################################################
        _run_stop_check_box = Qt.QCheckBox('Inicial/Parar')
        self._run_stop_choices = {True: True, False: False}
        self._run_stop_choices_inv = dict((v,k) for k,v in self._run_stop_choices.iteritems())
        self._run_stop_callback = lambda i: Qt.QMetaObject.invokeMethod(_run_stop_check_box, "setChecked", Qt.Q_ARG("bool", self._run_stop_choices_inv[i]))
        self._run_stop_callback(self.run_stop)
        _run_stop_check_box.stateChanged.connect(lambda i: self.set_run_stop(self._run_stop_choices[bool(i)]))
        self.top_grid_layout.addWidget(_run_stop_check_box, 0, 0, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_number_sink_0_0_0_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_VERT,
            3
        )
        self.qtgui_number_sink_0_0_0_0.set_update_time(0.10)
        self.qtgui_number_sink_0_0_0_0.set_title("")

        labels = ['Simbolos Procesados', 'Errores encontrados', 'BER', 'SER', 'log10(SER)',
                  '', '', '', '', '']
        units = ['', '', '', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("blue", "red"), ("black", "white"), ("blue", "red"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(3):
            self.qtgui_number_sink_0_0_0_0.set_min(i, 0)
            self.qtgui_number_sink_0_0_0_0.set_max(i, MaxCount)
            self.qtgui_number_sink_0_0_0_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_0_0_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_0_0_0.set_label(i, labels[i])
            self.qtgui_number_sink_0_0_0_0.set_unit(i, units[i])
            self.qtgui_number_sink_0_0_0_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0_0_0_0.enable_autoscale(True)
        self._qtgui_number_sink_0_0_0_0_win = sip.wrapinstance(self.qtgui_number_sink_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_number_sink_0_0_0_0_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.digital_constellation_decoder_cb_0 = digital.constellation_decoder_cb(MiconstellationObject)
        self.digital_chunks_to_symbols_xx = digital.chunks_to_symbols_bc((const), 1)
        self.blocks_throttle = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.blocks_add_xx = blocks.add_vcc(1)
        self.analog_random_source_x = blocks.vector_source_b(map(int, numpy.random.randint(0, M, 10000000)), True)
        self.analog_noise_source_x = analog.noise_source_c(analog.GR_GAUSSIAN, 1.0 / math.sqrt(2.0 * Bps * 10**(EbN0/10.)), 42)
        self.BER = BER.mi_bloque_embebido(Sym_max=MaxCount, Errors_max=MaxErrors)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.BER, 0), (self.qtgui_number_sink_0_0_0_0, 0))
        self.connect((self.BER, 1), (self.qtgui_number_sink_0_0_0_0, 1))
        self.connect((self.BER, 2), (self.qtgui_number_sink_0_0_0_0, 2))
        self.connect((self.analog_noise_source_x, 0), (self.blocks_add_xx, 1))
        self.connect((self.analog_random_source_x, 0), (self.blocks_throttle, 0))
        self.connect((self.blocks_add_xx, 0), (self.digital_constellation_decoder_cb_0, 0))
        self.connect((self.blocks_throttle, 0), (self.BER, 1))
        self.connect((self.blocks_throttle, 0), (self.digital_chunks_to_symbols_xx, 0))
        self.connect((self.digital_chunks_to_symbols_xx, 0), (self.blocks_add_xx, 0))
        self.connect((self.digital_constellation_decoder_cb_0, 0), (self.BER, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "ser_simulation")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_const(self):
        return self.const

    def set_const(self, const):
        self.const = const
        self.set_M(len(self.const))
        self.digital_chunks_to_symbols_xx.set_symbol_table((self.const))

    def get_M(self):
        return self.M

    def set_M(self, M):
        self.M = M
        self.set_Bps(int(math.log(self.M,2)))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle.set_sample_rate(self.samp_rate)

    def get_run_stop(self):
        return self.run_stop

    def set_run_stop(self, run_stop):
        self.run_stop = run_stop
        if self.run_stop: self.start()
        else: self.stop(); self.wait()
        self._run_stop_callback(self.run_stop)

    def get_MiconstellationObject(self):
        return self.MiconstellationObject

    def set_MiconstellationObject(self, MiconstellationObject):
        self.MiconstellationObject = MiconstellationObject

    def get_MaxErrors(self):
        return self.MaxErrors

    def set_MaxErrors(self, MaxErrors):
        self.MaxErrors = MaxErrors
        self.BER.Errors_max = self.MaxErrors

    def get_MaxCount(self):
        return self.MaxCount

    def set_MaxCount(self, MaxCount):
        self.MaxCount = MaxCount
        self.BER.Sym_max = self.MaxCount

    def get_EbN0(self):
        return self.EbN0

    def set_EbN0(self, EbN0):
        self.EbN0 = EbN0
        self.analog_noise_source_x.set_amplitude(1.0 / math.sqrt(2.0 * self.Bps * 10**(self.EbN0/10.)))

    def get_Bps(self):
        return self.Bps

    def set_Bps(self, Bps):
        self.Bps = Bps
        self.analog_noise_source_x.set_amplitude(1.0 / math.sqrt(2.0 * self.Bps * 10**(self.EbN0/10.)))


def main(top_block_cls=ser_simulation, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
