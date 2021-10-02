#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: SER Simulation
# Author: Homero Ortega Boada
# Description: Dale un valor a Es/No, corre el flujograma y obten la SER. Puedes sacar tantos valores como para construir una curva de SER
# GNU Radio version: 3.9.0.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
import sip
import numpy
from gnuradio import blocks
from gnuradio import digital
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import epy_block_0
import math
import numpy as np



from gnuradio import qtgui

class ser_simulation(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "SER Simulation", catch_exceptions=True)
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

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.const0 = const0 = digital.constellation_bpsk().points()
        self.M0 = M0 = len(const0)
        self.samp_rate = samp_rate = 100e3
        self.mapa = mapa = np.arange(M0)
        self.Sps = Sps = 1
        self.run_stop = run_stop = True
        self.Rs = Rs = samp_rate/Sps
        self.N_snr = N_snr = 32
        self.MiconstellationObject0 = MiconstellationObject0 = digital.constellation_calcdist(const0, mapa,
        4, 1, digital.constellation.AMPLITUDE_NORMALIZATION).base()
        self.MaxErrors = MaxErrors = 1000
        self.MaxCount = MaxCount = int(1e7)
        self.EsN0min = EsN0min = 0
        self.EsN0max = EsN0max = 35

        ##################################################
        # Blocks
        ##################################################
        _run_stop_check_box = Qt.QCheckBox('Inicial/Parar')
        self._run_stop_choices = {True: True, False: False}
        self._run_stop_choices_inv = dict((v,k) for k,v in self._run_stop_choices.items())
        self._run_stop_callback = lambda i: Qt.QMetaObject.invokeMethod(_run_stop_check_box, "setChecked", Qt.Q_ARG("bool", self._run_stop_choices_inv[i]))
        self._run_stop_callback(self.run_stop)
        _run_stop_check_box.stateChanged.connect(lambda i: self.set_run_stop(self._run_stop_choices[bool(i)]))
        self.top_grid_layout.addWidget(_run_stop_check_box, 0, 0, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_bercurve_sink_0 = qtgui.ber_sink_b(
            numpy.linspace(EsN0min, EsN0max, N_snr), #range of esnos
            1, #number of curves
            100, #ensure at least
            -7.0, #cutoff
            [], #indiv. curve names
            None # parent
        )
        self.qtgui_bercurve_sink_0.set_update_time(0.10)
        self.qtgui_bercurve_sink_0.set_y_axis(-10, 0)
        self.qtgui_bercurve_sink_0.set_x_axis(numpy.linspace(EsN0min, EsN0max, N_snr)[0], numpy.linspace(EsN0min, EsN0max, N_snr)[-1])

        labels = ['BPSK mio', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_bercurve_sink_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_bercurve_sink_0.set_line_label(i, labels[i])
            self.qtgui_bercurve_sink_0.set_line_width(i, widths[i])
            self.qtgui_bercurve_sink_0.set_line_color(i, colors[i])
            self.qtgui_bercurve_sink_0.set_line_style(i, styles[i])
            self.qtgui_bercurve_sink_0.set_line_marker(i, markers[i])
            self.qtgui_bercurve_sink_0.set_line_alpha(i, alphas[i])

        self._qtgui_bercurve_sink_0_win = sip.wrapinstance(self.qtgui_bercurve_sink_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_bercurve_sink_0_win)
        self.epy_block_0 = epy_block_0.blk(N=N_snr, EsN0min=EsN0min, EsN0max=EsN0max, Sps=Sps, Rs=Rs)
        self.digital_constellation_decoder_cb_0_0_0 = digital.constellation_decoder_cb(MiconstellationObject0)
        self.digital_chunks_to_symbols_xx_1 = digital.chunks_to_symbols_bc(const0, 1)
        self.blocks_vector_to_stream_0 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, N_snr)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, N_snr)
        self.blocks_stream_demux_0_0 = blocks.stream_demux(gr.sizeof_char*1, ([1]*N_snr))
        self.blocks_stream_demux_0 = blocks.stream_demux(gr.sizeof_char*1, ([1]*N_snr))
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_char*1)
        self.analog_random_source_x_1 = blocks.vector_source_b(list(map(int, numpy.random.randint(0, M0, 10000000))), True)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_random_source_x_1, 0), (self.blocks_stream_demux_0, 0))
        self.connect((self.analog_random_source_x_1, 0), (self.digital_chunks_to_symbols_xx_1, 0))
        self.connect((self.blocks_stream_demux_0, 21), (self.qtgui_bercurve_sink_0, 42))
        self.connect((self.blocks_stream_demux_0, 26), (self.qtgui_bercurve_sink_0, 52))
        self.connect((self.blocks_stream_demux_0, 1), (self.qtgui_bercurve_sink_0, 2))
        self.connect((self.blocks_stream_demux_0, 30), (self.qtgui_bercurve_sink_0, 60))
        self.connect((self.blocks_stream_demux_0, 22), (self.qtgui_bercurve_sink_0, 44))
        self.connect((self.blocks_stream_demux_0, 18), (self.qtgui_bercurve_sink_0, 36))
        self.connect((self.blocks_stream_demux_0, 23), (self.qtgui_bercurve_sink_0, 46))
        self.connect((self.blocks_stream_demux_0, 6), (self.qtgui_bercurve_sink_0, 12))
        self.connect((self.blocks_stream_demux_0, 7), (self.qtgui_bercurve_sink_0, 14))
        self.connect((self.blocks_stream_demux_0, 31), (self.qtgui_bercurve_sink_0, 62))
        self.connect((self.blocks_stream_demux_0, 2), (self.qtgui_bercurve_sink_0, 4))
        self.connect((self.blocks_stream_demux_0, 3), (self.qtgui_bercurve_sink_0, 6))
        self.connect((self.blocks_stream_demux_0, 8), (self.qtgui_bercurve_sink_0, 16))
        self.connect((self.blocks_stream_demux_0, 17), (self.qtgui_bercurve_sink_0, 34))
        self.connect((self.blocks_stream_demux_0, 14), (self.qtgui_bercurve_sink_0, 28))
        self.connect((self.blocks_stream_demux_0, 20), (self.qtgui_bercurve_sink_0, 40))
        self.connect((self.blocks_stream_demux_0, 5), (self.qtgui_bercurve_sink_0, 10))
        self.connect((self.blocks_stream_demux_0, 24), (self.qtgui_bercurve_sink_0, 48))
        self.connect((self.blocks_stream_demux_0, 0), (self.qtgui_bercurve_sink_0, 0))
        self.connect((self.blocks_stream_demux_0, 29), (self.qtgui_bercurve_sink_0, 58))
        self.connect((self.blocks_stream_demux_0, 13), (self.qtgui_bercurve_sink_0, 26))
        self.connect((self.blocks_stream_demux_0, 28), (self.qtgui_bercurve_sink_0, 56))
        self.connect((self.blocks_stream_demux_0, 19), (self.qtgui_bercurve_sink_0, 38))
        self.connect((self.blocks_stream_demux_0, 4), (self.qtgui_bercurve_sink_0, 8))
        self.connect((self.blocks_stream_demux_0, 27), (self.qtgui_bercurve_sink_0, 54))
        self.connect((self.blocks_stream_demux_0, 16), (self.qtgui_bercurve_sink_0, 32))
        self.connect((self.blocks_stream_demux_0, 11), (self.qtgui_bercurve_sink_0, 22))
        self.connect((self.blocks_stream_demux_0, 9), (self.qtgui_bercurve_sink_0, 18))
        self.connect((self.blocks_stream_demux_0, 15), (self.qtgui_bercurve_sink_0, 30))
        self.connect((self.blocks_stream_demux_0, 12), (self.qtgui_bercurve_sink_0, 24))
        self.connect((self.blocks_stream_demux_0, 10), (self.qtgui_bercurve_sink_0, 20))
        self.connect((self.blocks_stream_demux_0, 25), (self.qtgui_bercurve_sink_0, 50))
        self.connect((self.blocks_stream_demux_0_0, 9), (self.qtgui_bercurve_sink_0, 19))
        self.connect((self.blocks_stream_demux_0_0, 21), (self.qtgui_bercurve_sink_0, 43))
        self.connect((self.blocks_stream_demux_0_0, 24), (self.qtgui_bercurve_sink_0, 49))
        self.connect((self.blocks_stream_demux_0_0, 29), (self.qtgui_bercurve_sink_0, 59))
        self.connect((self.blocks_stream_demux_0_0, 17), (self.qtgui_bercurve_sink_0, 35))
        self.connect((self.blocks_stream_demux_0_0, 27), (self.qtgui_bercurve_sink_0, 55))
        self.connect((self.blocks_stream_demux_0_0, 19), (self.qtgui_bercurve_sink_0, 39))
        self.connect((self.blocks_stream_demux_0_0, 8), (self.qtgui_bercurve_sink_0, 17))
        self.connect((self.blocks_stream_demux_0_0, 11), (self.qtgui_bercurve_sink_0, 23))
        self.connect((self.blocks_stream_demux_0_0, 23), (self.qtgui_bercurve_sink_0, 47))
        self.connect((self.blocks_stream_demux_0_0, 26), (self.qtgui_bercurve_sink_0, 53))
        self.connect((self.blocks_stream_demux_0_0, 15), (self.qtgui_bercurve_sink_0, 31))
        self.connect((self.blocks_stream_demux_0_0, 2), (self.qtgui_bercurve_sink_0, 5))
        self.connect((self.blocks_stream_demux_0_0, 28), (self.qtgui_bercurve_sink_0, 57))
        self.connect((self.blocks_stream_demux_0_0, 31), (self.qtgui_bercurve_sink_0, 63))
        self.connect((self.blocks_stream_demux_0_0, 7), (self.qtgui_bercurve_sink_0, 15))
        self.connect((self.blocks_stream_demux_0_0, 6), (self.qtgui_bercurve_sink_0, 13))
        self.connect((self.blocks_stream_demux_0_0, 20), (self.qtgui_bercurve_sink_0, 41))
        self.connect((self.blocks_stream_demux_0_0, 18), (self.qtgui_bercurve_sink_0, 37))
        self.connect((self.blocks_stream_demux_0_0, 0), (self.qtgui_bercurve_sink_0, 1))
        self.connect((self.blocks_stream_demux_0_0, 13), (self.qtgui_bercurve_sink_0, 27))
        self.connect((self.blocks_stream_demux_0_0, 16), (self.qtgui_bercurve_sink_0, 33))
        self.connect((self.blocks_stream_demux_0_0, 30), (self.qtgui_bercurve_sink_0, 61))
        self.connect((self.blocks_stream_demux_0_0, 14), (self.qtgui_bercurve_sink_0, 29))
        self.connect((self.blocks_stream_demux_0_0, 3), (self.qtgui_bercurve_sink_0, 7))
        self.connect((self.blocks_stream_demux_0_0, 4), (self.qtgui_bercurve_sink_0, 9))
        self.connect((self.blocks_stream_demux_0_0, 10), (self.qtgui_bercurve_sink_0, 21))
        self.connect((self.blocks_stream_demux_0_0, 22), (self.qtgui_bercurve_sink_0, 45))
        self.connect((self.blocks_stream_demux_0_0, 25), (self.qtgui_bercurve_sink_0, 51))
        self.connect((self.blocks_stream_demux_0_0, 1), (self.qtgui_bercurve_sink_0, 3))
        self.connect((self.blocks_stream_demux_0_0, 5), (self.qtgui_bercurve_sink_0, 11))
        self.connect((self.blocks_stream_demux_0_0, 12), (self.qtgui_bercurve_sink_0, 25))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.epy_block_0, 0))
        self.connect((self.blocks_vector_to_stream_0, 0), (self.digital_constellation_decoder_cb_0_0_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_1, 0), (self.blocks_stream_to_vector_0, 0))
        self.connect((self.digital_constellation_decoder_cb_0_0_0, 0), (self.blocks_null_sink_0, 0))
        self.connect((self.digital_constellation_decoder_cb_0_0_0, 0), (self.blocks_stream_demux_0_0, 0))
        self.connect((self.epy_block_0, 0), (self.blocks_vector_to_stream_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "ser_simulation")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_const0(self):
        return self.const0

    def set_const0(self, const0):
        self.const0 = const0
        self.set_M0(len(self.const0))
        self.digital_chunks_to_symbols_xx_1.set_symbol_table(self.const0)

    def get_M0(self):
        return self.M0

    def set_M0(self, M0):
        self.M0 = M0
        self.set_mapa(np.arange(self.M0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_Rs(self.samp_rate/self.Sps)

    def get_mapa(self):
        return self.mapa

    def set_mapa(self, mapa):
        self.mapa = mapa

    def get_Sps(self):
        return self.Sps

    def set_Sps(self, Sps):
        self.Sps = Sps
        self.set_Rs(self.samp_rate/self.Sps)

    def get_run_stop(self):
        return self.run_stop

    def set_run_stop(self, run_stop):
        self.run_stop = run_stop
        if self.run_stop: self.start()
        else: self.stop(); self.wait()
        self._run_stop_callback(self.run_stop)

    def get_Rs(self):
        return self.Rs

    def set_Rs(self, Rs):
        self.Rs = Rs

    def get_N_snr(self):
        return self.N_snr

    def set_N_snr(self, N_snr):
        self.N_snr = N_snr

    def get_MiconstellationObject0(self):
        return self.MiconstellationObject0

    def set_MiconstellationObject0(self, MiconstellationObject0):
        self.MiconstellationObject0 = MiconstellationObject0

    def get_MaxErrors(self):
        return self.MaxErrors

    def set_MaxErrors(self, MaxErrors):
        self.MaxErrors = MaxErrors

    def get_MaxCount(self):
        return self.MaxCount

    def set_MaxCount(self, MaxCount):
        self.MaxCount = MaxCount

    def get_EsN0min(self):
        return self.EsN0min

    def set_EsN0min(self, EsN0min):
        self.EsN0min = EsN0min

    def get_EsN0max(self):
        return self.EsN0max

    def set_EsN0max(self, EsN0max):
        self.EsN0max = EsN0max




def main(top_block_cls=ser_simulation, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
