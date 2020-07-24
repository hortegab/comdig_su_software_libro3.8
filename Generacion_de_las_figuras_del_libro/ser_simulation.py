#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: SER Simulation
# Author: Homero Ortega Boada
# Description: Dale un valor a Es/No, corre el flujograma y obten la SER. Puedes sacar tantos valores como para construir una curva de SER
# Generated: Thu Aug 22 06:24:14 2019
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

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt4 import Qt
from b_BERTool import b_BERTool  # grc-generated hier_block
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import math
import numpy
import sip
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
        self.samp_rate = samp_rate = 100e3
        self.const3 = const3 = digital.qam_constellation(16).points()
        self.const2 = const2 = digital.constellation_8psk().points()
        self.const1 = const1 = digital.constellation_qpsk().points()
        self.const0 = const0 = digital.constellation_bpsk().points()
        self.Sps = Sps = 1
        self.run_stop = run_stop = True
        self.Rs = Rs = samp_rate/Sps
        self.N_snr = N_snr = 128

        self.MiconstellationObject3 = MiconstellationObject3 = digital.constellation_calcdist((const3), (), 4, 1).base()


        self.MiconstellationObject2 = MiconstellationObject2 = digital.constellation_calcdist((const2), (), 4, 1).base()


        self.MiconstellationObject1 = MiconstellationObject1 = digital.constellation_calcdist((const1), (), 4, 1).base()


        self.MiconstellationObject0 = MiconstellationObject0 = digital.constellation_calcdist((const0), (), 4, 1).base()

        self.MaxErrors = MaxErrors = 1000
        self.MaxCount = MaxCount = int(1e7)
        self.M3 = M3 = len(const3)
        self.M2 = M2 = len(const2)
        self.M1 = M1 = len(const1)
        self.M0 = M0 = len(const0)
        self.EsN0min = EsN0min = -5.
        self.EsN0max = EsN0max = 25.

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
        self.qtgui_vector_sink_f_0 = qtgui.vector_sink_f(
            N_snr,
            EsN0min,
            (EsN0max-EsN0min)/float(N_snr),
            "Es/N0 [dB]",
            "logPe",
            "Curva de SER",
            4 # Number of inputs
        )
        self.qtgui_vector_sink_f_0.set_update_time(0.10)
        self.qtgui_vector_sink_f_0.set_y_axis(-8, 0)
        self.qtgui_vector_sink_f_0.enable_autoscale(False)
        self.qtgui_vector_sink_f_0.enable_grid(False)
        self.qtgui_vector_sink_f_0.set_x_axis_units("dB")
        self.qtgui_vector_sink_f_0.set_y_axis_units("")
        self.qtgui_vector_sink_f_0.set_ref_level(0)

        labels = ["BPSK", "QPSK", '8PSK', "16QAM", '',
                  '', '', '', '', '']
        widths = [4, 4, 4, 4, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(4):
            if len(labels[i]) == 0:
                self.qtgui_vector_sink_f_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_vector_sink_f_0.set_line_label(i, labels[i])
            self.qtgui_vector_sink_f_0.set_line_width(i, widths[i])
            self.qtgui_vector_sink_f_0.set_line_color(i, colors[i])
            self.qtgui_vector_sink_f_0.set_line_alpha(i, alphas[i])

        self._qtgui_vector_sink_f_0_win = sip.wrapinstance(self.qtgui_vector_sink_f_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_vector_sink_f_0_win, 2, 0, 1, 1)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.digital_constellation_decoder_cb_0_1 = digital.constellation_decoder_cb(MiconstellationObject1)
        self.digital_constellation_decoder_cb_0_0_0 = digital.constellation_decoder_cb(MiconstellationObject0)
        self.digital_constellation_decoder_cb_0_0 = digital.constellation_decoder_cb(MiconstellationObject2)
        self.digital_constellation_decoder_cb_0 = digital.constellation_decoder_cb(MiconstellationObject3)
        self.digital_chunks_to_symbols_xx_1 = digital.chunks_to_symbols_bc((const0), 1)
        self.digital_chunks_to_symbols_xx_0_0 = digital.chunks_to_symbols_bc((const1), 1)
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc((const3), 1)
        self.digital_chunks_to_symbols_xx = digital.chunks_to_symbols_bc((const2), 1)
        self.b_BERTool_0_1 = b_BERTool(
            EsN0max=EsN0max,
            EsN0min=EsN0min,
            N_snr=N_snr,
            Rs=Rs,
        )
        self.b_BERTool_0_0_0 = b_BERTool(
            EsN0max=EsN0max,
            EsN0min=EsN0min,
            N_snr=N_snr,
            Rs=Rs,
        )
        self.b_BERTool_0_0 = b_BERTool(
            EsN0max=EsN0max,
            EsN0min=EsN0min,
            N_snr=N_snr,
            Rs=Rs,
        )
        self.b_BERTool_0 = b_BERTool(
            EsN0max=EsN0max,
            EsN0min=EsN0min,
            N_snr=N_snr,
            Rs=Rs,
        )
        self.analog_random_source_x_1 = blocks.vector_source_b(map(int, numpy.random.randint(0, M0, 10000000)), True)
        self.analog_random_source_x_0_0 = blocks.vector_source_b(map(int, numpy.random.randint(0, M1, 10000000)), True)
        self.analog_random_source_x_0 = blocks.vector_source_b(map(int, numpy.random.randint(0, M3, 10000000)), True)
        self.analog_random_source_x = blocks.vector_source_b(map(int, numpy.random.randint(0, M2, 10000000)), True)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_random_source_x, 0), (self.b_BERTool_0_0, 2))
        self.connect((self.analog_random_source_x, 0), (self.digital_chunks_to_symbols_xx, 0))
        self.connect((self.analog_random_source_x_0, 0), (self.b_BERTool_0, 1))
        self.connect((self.analog_random_source_x_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))
        self.connect((self.analog_random_source_x_0_0, 0), (self.b_BERTool_0_1, 2))
        self.connect((self.analog_random_source_x_0_0, 0), (self.digital_chunks_to_symbols_xx_0_0, 0))
        self.connect((self.analog_random_source_x_1, 0), (self.b_BERTool_0_0_0, 2))
        self.connect((self.analog_random_source_x_1, 0), (self.digital_chunks_to_symbols_xx_1, 0))
        self.connect((self.b_BERTool_0, 0), (self.digital_constellation_decoder_cb_0, 0))
        self.connect((self.b_BERTool_0, 1), (self.qtgui_vector_sink_f_0, 3))
        self.connect((self.b_BERTool_0_0, 0), (self.digital_constellation_decoder_cb_0_0, 0))
        self.connect((self.b_BERTool_0_0, 1), (self.qtgui_vector_sink_f_0, 2))
        self.connect((self.b_BERTool_0_0_0, 0), (self.digital_constellation_decoder_cb_0_0_0, 0))
        self.connect((self.b_BERTool_0_0_0, 1), (self.qtgui_vector_sink_f_0, 0))
        self.connect((self.b_BERTool_0_1, 0), (self.digital_constellation_decoder_cb_0_1, 0))
        self.connect((self.b_BERTool_0_1, 1), (self.qtgui_vector_sink_f_0, 1))
        self.connect((self.digital_chunks_to_symbols_xx, 0), (self.b_BERTool_0_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.b_BERTool_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0_0, 0), (self.b_BERTool_0_1, 0))
        self.connect((self.digital_chunks_to_symbols_xx_1, 0), (self.b_BERTool_0_0_0, 0))
        self.connect((self.digital_constellation_decoder_cb_0, 0), (self.b_BERTool_0, 2))
        self.connect((self.digital_constellation_decoder_cb_0_0, 0), (self.b_BERTool_0_0, 1))
        self.connect((self.digital_constellation_decoder_cb_0_0_0, 0), (self.b_BERTool_0_0_0, 1))
        self.connect((self.digital_constellation_decoder_cb_0_1, 0), (self.b_BERTool_0_1, 1))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "ser_simulation")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_Rs(self.samp_rate/self.Sps)

    def get_const3(self):
        return self.const3

    def set_const3(self, const3):
        self.const3 = const3
        self.set_M3(len(self.const3))
        self.digital_chunks_to_symbols_xx_0.set_symbol_table((self.const3))

    def get_const2(self):
        return self.const2

    def set_const2(self, const2):
        self.const2 = const2
        self.set_M2(len(self.const2))
        self.digital_chunks_to_symbols_xx.set_symbol_table((self.const2))

    def get_const1(self):
        return self.const1

    def set_const1(self, const1):
        self.const1 = const1
        self.set_M1(len(self.const1))
        self.digital_chunks_to_symbols_xx_0_0.set_symbol_table((self.const1))

    def get_const0(self):
        return self.const0

    def set_const0(self, const0):
        self.const0 = const0
        self.set_M0(len(self.const0))
        self.digital_chunks_to_symbols_xx_1.set_symbol_table((self.const0))

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
        self.b_BERTool_0_1.set_Rs(self.Rs)
        self.b_BERTool_0_0_0.set_Rs(self.Rs)
        self.b_BERTool_0_0.set_Rs(self.Rs)
        self.b_BERTool_0.set_Rs(self.Rs)

    def get_N_snr(self):
        return self.N_snr

    def set_N_snr(self, N_snr):
        self.N_snr = N_snr
        self.qtgui_vector_sink_f_0.set_x_axis(self.EsN0min, (self.EsN0max-self.EsN0min)/float(self.N_snr))
        self.b_BERTool_0_1.set_N_snr(self.N_snr)
        self.b_BERTool_0_0_0.set_N_snr(self.N_snr)
        self.b_BERTool_0_0.set_N_snr(self.N_snr)
        self.b_BERTool_0.set_N_snr(self.N_snr)

    def get_MiconstellationObject3(self):
        return self.MiconstellationObject3

    def set_MiconstellationObject3(self, MiconstellationObject3):
        self.MiconstellationObject3 = MiconstellationObject3

    def get_MiconstellationObject2(self):
        return self.MiconstellationObject2

    def set_MiconstellationObject2(self, MiconstellationObject2):
        self.MiconstellationObject2 = MiconstellationObject2

    def get_MiconstellationObject1(self):
        return self.MiconstellationObject1

    def set_MiconstellationObject1(self, MiconstellationObject1):
        self.MiconstellationObject1 = MiconstellationObject1

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

    def get_M3(self):
        return self.M3

    def set_M3(self, M3):
        self.M3 = M3

    def get_M2(self):
        return self.M2

    def set_M2(self, M2):
        self.M2 = M2

    def get_M1(self):
        return self.M1

    def set_M1(self, M1):
        self.M1 = M1

    def get_M0(self):
        return self.M0

    def set_M0(self, M0):
        self.M0 = M0

    def get_EsN0min(self):
        return self.EsN0min

    def set_EsN0min(self, EsN0min):
        self.EsN0min = EsN0min
        self.qtgui_vector_sink_f_0.set_x_axis(self.EsN0min, (self.EsN0max-self.EsN0min)/float(self.N_snr))
        self.b_BERTool_0_1.set_EsN0min(self.EsN0min)
        self.b_BERTool_0_0_0.set_EsN0min(self.EsN0min)
        self.b_BERTool_0_0.set_EsN0min(self.EsN0min)
        self.b_BERTool_0.set_EsN0min(self.EsN0min)

    def get_EsN0max(self):
        return self.EsN0max

    def set_EsN0max(self, EsN0max):
        self.EsN0max = EsN0max
        self.qtgui_vector_sink_f_0.set_x_axis(self.EsN0min, (self.EsN0max-self.EsN0min)/float(self.N_snr))
        self.b_BERTool_0_1.set_EsN0max(self.EsN0max)
        self.b_BERTool_0_0_0.set_EsN0max(self.EsN0max)
        self.b_BERTool_0_0.set_EsN0max(self.EsN0max)
        self.b_BERTool_0.set_EsN0max(self.EsN0max)


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
