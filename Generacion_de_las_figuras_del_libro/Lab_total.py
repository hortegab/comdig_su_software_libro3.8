#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Lab Total
# Generated: Sat Mar 28 07:33:17 2020
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
from b_Eye_Diagram_simple_c import b_Eye_Diagram_simple_c  # grc-generated hier_block
from b_RRaised_cosine_cc import b_RRaised_cosine_cc  # grc-generated hier_block
from gnuradio import analog
from gnuradio import blocks
from gnuradio import channels
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
from scipy import fftpack
import cmath
import math
import numpy
import random
import sip
from gnuradio import qtgui


class Lab_total(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Lab Total")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Lab Total")
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

        self.settings = Qt.QSettings("GNU Radio", "Lab_total")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.samp_rate_audio = samp_rate_audio = 11000
        self.NbpS = NbpS = 8
        self.Constelacion = Constelacion = [1.+0.j,   0.+1.j,   -1.+0.j,  0.-1.j ]
        self.Rbi = Rbi = NbpS*samp_rate_audio
        self.M = M = len(Constelacion)
        self.Sps = Sps = 8
        self.Rb = Rb = Rbi
        self.Bps = Bps = int(math.log(M,2))
        self.tap7 = tap7 = 1
        self.tap6 = tap6 = 1
        self.tap5 = tap5 = 1
        self.tap4 = tap4 = 0.25
        self.tap3 = tap3 = 1
        self.tap2 = tap2 = 1
        self.tap1 = tap1 = 0.05
        self.tap0 = tap0 = 0.25
        self.rolloff = rolloff = 0.9
        self.ntaps = ntaps = Sps*16
        self.nfilts = nfilts = 32
        self.code1 = code1 = '010110011011101100010101011111101001001110001011010001101010001'
        self.Rs = Rs = Rb/Bps
        self.samp_rate = samp_rate = Rs*Sps
        self.run_stop = run_stop = True
        self.rrc_taps_rx = rrc_taps_rx = firdes.root_raised_cosine(nfilts, nfilts, 1.0/float(Sps), rolloff, ntaps*nfilts)
        self.payload = payload = 128
        self.eq_gain = eq_gain = 0.01
        self.W = W = Rs/2
        self.Vp = Vp = 1.
        self.Tmax_scope = Tmax_scope = 64./Rs
        self.SymbTune = SymbTune = 2
        self.Sps_o = Sps_o = Sps
        self.NodB = NodB = -80
        self.NnivelesQ = NnivelesQ = math.pow(2,NbpS)
        self.NbpCode = NbpCode = len(code1)+10.

        self.MiconstellationObject = MiconstellationObject = digital.constellation_calcdist((Constelacion), (), 4, 1).base()

        self.Fc = Fc = 80e6
        self.Ch_taps = Ch_taps = fftpack.ifftshift(fftpack.ifft([tap0, tap1, tap2, tap3, tap4, tap5, tap6, tap7]))
        self.Ch_Jitter = Ch_Jitter = 0
        self.Ch_Frec_offset = Ch_Frec_offset = 0
        self.Ch_Delay = Ch_Delay = 0
        self.Am = Am = .8

        ##################################################
        # Blocks
        ##################################################
        self.controls = Qt.QTabWidget()
        self.controls_widget_0 = Qt.QWidget()
        self.controls_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.controls_widget_0)
        self.controls_grid_layout_0 = Qt.QGridLayout()
        self.controls_layout_0.addLayout(self.controls_grid_layout_0)
        self.controls.addTab(self.controls_widget_0, 'Ch_Offsets')
        self.controls_widget_1 = Qt.QWidget()
        self.controls_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.controls_widget_1)
        self.controls_grid_layout_1 = Qt.QGridLayout()
        self.controls_layout_1.addLayout(self.controls_grid_layout_1)
        self.controls.addTab(self.controls_widget_1, 'Ch_Taps')
        self.controls_widget_2 = Qt.QWidget()
        self.controls_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.controls_widget_2)
        self.controls_grid_layout_2 = Qt.QGridLayout()
        self.controls_layout_2.addLayout(self.controls_grid_layout_2)
        self.controls.addTab(self.controls_widget_2, 'Tuning')
        self.top_grid_layout.addWidget(self.controls, 0, 1, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.Instrumentos = Qt.QTabWidget()
        self.Instrumentos_widget_0 = Qt.QWidget()
        self.Instrumentos_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Instrumentos_widget_0)
        self.Instrumentos_grid_layout_0 = Qt.QGridLayout()
        self.Instrumentos_layout_0.addLayout(self.Instrumentos_grid_layout_0)
        self.Instrumentos.addTab(self.Instrumentos_widget_0, 'Capa0.Canal y precanal')
        self.Instrumentos_widget_1 = Qt.QWidget()
        self.Instrumentos_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Instrumentos_widget_1)
        self.Instrumentos_grid_layout_1 = Qt.QGridLayout()
        self.Instrumentos_layout_1.addLayout(self.Instrumentos_grid_layout_1)
        self.Instrumentos.addTab(self.Instrumentos_widget_1, 'Capas.Pre-modulacion')
        self.Instrumentos_widget_2 = Qt.QWidget()
        self.Instrumentos_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Instrumentos_widget_2)
        self.Instrumentos_grid_layout_2 = Qt.QGridLayout()
        self.Instrumentos_layout_2.addLayout(self.Instrumentos_grid_layout_2)
        self.Instrumentos.addTab(self.Instrumentos_widget_2, 'Capa1. Modulacion')
        self.Instrumentos_widget_3 = Qt.QWidget()
        self.Instrumentos_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Instrumentos_widget_3)
        self.Instrumentos_grid_layout_3 = Qt.QGridLayout()
        self.Instrumentos_layout_3.addLayout(self.Instrumentos_grid_layout_3)
        self.Instrumentos.addTab(self.Instrumentos_widget_3, 'Capa2. CodificacionDeSimbolos')
        self.top_grid_layout.addWidget(self.Instrumentos, 1, 0, 1, 2)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.canal = Qt.QTabWidget()
        self.canal_widget_0 = Qt.QWidget()
        self.canal_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.canal_widget_0)
        self.canal_grid_layout_0 = Qt.QGridLayout()
        self.canal_layout_0.addLayout(self.canal_grid_layout_0)
        self.canal.addTab(self.canal_widget_0, 'H(f) y Espectro')
        self.canal_widget_1 = Qt.QWidget()
        self.canal_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.canal_widget_1)
        self.canal_grid_layout_1 = Qt.QGridLayout()
        self.canal_layout_1.addLayout(self.canal_grid_layout_1)
        self.canal.addTab(self.canal_widget_1, 'Diagrama de ojo canal')
        self.canal_widget_2 = Qt.QWidget()
        self.canal_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.canal_widget_2)
        self.canal_grid_layout_2 = Qt.QGridLayout()
        self.canal_layout_2.addLayout(self.canal_grid_layout_2)
        self.canal.addTab(self.canal_widget_2, 'Diagrama de ojo ecualizador')
        self.canal_widget_3 = Qt.QWidget()
        self.canal_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.canal_widget_3)
        self.canal_grid_layout_3 = Qt.QGridLayout()
        self.canal_layout_3.addLayout(self.canal_grid_layout_3)
        self.canal.addTab(self.canal_widget_3, 'Constelacion')
        self.canal_widget_4 = Qt.QWidget()
        self.canal_layout_4 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.canal_widget_4)
        self.canal_grid_layout_4 = Qt.QGridLayout()
        self.canal_layout_4.addLayout(self.canal_grid_layout_4)
        self.canal.addTab(self.canal_widget_4, 'La Ecualizacion')
        self.Instrumentos_grid_layout_0.addWidget(self.canal, 1, 0, 1, 1)
        for r in range(1, 2):
            self.Instrumentos_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.Instrumentos_grid_layout_0.setColumnStretch(c, 1)
        self._NodB_range = Range(-140., 0., 1., -80, 200)
        self._NodB_win = RangeWidget(self._NodB_range, self.set_NodB, 'Ch_No(dB)', "counter", float)
        self.controls_grid_layout_0.addWidget(self._NodB_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.controls_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.controls_grid_layout_0.setColumnStretch(c, 1)
        self._Ch_Jitter_range = Range(-.001, .001, 0.0001, 0, 200)
        self._Ch_Jitter_win = RangeWidget(self._Ch_Jitter_range, self.set_Ch_Jitter, 'Ch_Jitter', "counter", float)
        self.controls_grid_layout_0.addWidget(self._Ch_Jitter_win, 0, 2, 1, 1)
        for r in range(0, 1):
            self.controls_grid_layout_0.setRowStretch(r, 1)
        for c in range(2, 3):
            self.controls_grid_layout_0.setColumnStretch(c, 1)
        self._Ch_Frec_offset_range = Range(0, 100, 0.0001, 0, 200)
        self._Ch_Frec_offset_win = RangeWidget(self._Ch_Frec_offset_range, self.set_Ch_Frec_offset, 'Ch_Frec_offset (Hz)', "counter", float)
        self.controls_grid_layout_0.addWidget(self._Ch_Frec_offset_win, 0, 1, 1, 1)
        for r in range(0, 1):
            self.controls_grid_layout_0.setRowStretch(r, 1)
        for c in range(1, 2):
            self.controls_grid_layout_0.setColumnStretch(c, 1)
        self._Ch_Delay_range = Range(0, 1000, 1, 0, 200)
        self._Ch_Delay_win = RangeWidget(self._Ch_Delay_range, self.set_Ch_Delay, 'Ch_Delay', "counter", int)
        self.controls_grid_layout_0.addWidget(self._Ch_Delay_win, 0, 3, 1, 1)
        for r in range(0, 1):
            self.controls_grid_layout_0.setRowStretch(r, 1)
        for c in range(3, 4):
            self.controls_grid_layout_0.setColumnStretch(c, 1)
        self._tap7_range = Range(0, 1, 0.01, 1, 200)
        self._tap7_win = RangeWidget(self._tap7_range, self.set_tap7, "tap7", "slider", float)
        self.controls_grid_layout_1.addWidget(self._tap7_win, 1, 3, 1, 1)
        for r in range(1, 2):
            self.controls_grid_layout_1.setRowStretch(r, 1)
        for c in range(3, 4):
            self.controls_grid_layout_1.setColumnStretch(c, 1)
        self._tap6_range = Range(0.25, 1, 0.01, 1, 200)
        self._tap6_win = RangeWidget(self._tap6_range, self.set_tap6, "tap6", "slider", float)
        self.controls_grid_layout_1.addWidget(self._tap6_win, 1, 2, 1, 1)
        for r in range(1, 2):
            self.controls_grid_layout_1.setRowStretch(r, 1)
        for c in range(2, 3):
            self.controls_grid_layout_1.setColumnStretch(c, 1)
        self._tap5_range = Range(0, 1, 0.01, 1, 200)
        self._tap5_win = RangeWidget(self._tap5_range, self.set_tap5, "tap5", "slider", float)
        self.controls_grid_layout_1.addWidget(self._tap5_win, 1, 1, 1, 1)
        for r in range(1, 2):
            self.controls_grid_layout_1.setRowStretch(r, 1)
        for c in range(1, 2):
            self.controls_grid_layout_1.setColumnStretch(c, 1)
        self._tap4_range = Range(0, 1, 0.01, 0.25, 200)
        self._tap4_win = RangeWidget(self._tap4_range, self.set_tap4, "tap4", "slider", float)
        self.controls_grid_layout_1.addWidget(self._tap4_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.controls_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 1):
            self.controls_grid_layout_1.setColumnStretch(c, 1)
        self._tap3_range = Range(0, 1, 0.01, 1, 200)
        self._tap3_win = RangeWidget(self._tap3_range, self.set_tap3, "tap3", "slider", float)
        self.controls_grid_layout_1.addWidget(self._tap3_win, 0, 3, 1, 1)
        for r in range(0, 1):
            self.controls_grid_layout_1.setRowStretch(r, 1)
        for c in range(3, 4):
            self.controls_grid_layout_1.setColumnStretch(c, 1)
        self._tap2_range = Range(0.25, 1, 0.01, 1, 200)
        self._tap2_win = RangeWidget(self._tap2_range, self.set_tap2, "tap2", "slider", float)
        self.controls_grid_layout_1.addWidget(self._tap2_win, 0, 2, 1, 1)
        for r in range(0, 1):
            self.controls_grid_layout_1.setRowStretch(r, 1)
        for c in range(2, 3):
            self.controls_grid_layout_1.setColumnStretch(c, 1)
        self._tap1_range = Range(0, 1, 0.01, 0.05, 200)
        self._tap1_win = RangeWidget(self._tap1_range, self.set_tap1, "tap1", "slider", float)
        self.controls_grid_layout_1.addWidget(self._tap1_win, 0, 1, 1, 1)
        for r in range(0, 1):
            self.controls_grid_layout_1.setRowStretch(r, 1)
        for c in range(1, 2):
            self.controls_grid_layout_1.setColumnStretch(c, 1)
        self._tap0_range = Range(0, 1, 0.01, 0.25, 200)
        self._tap0_win = RangeWidget(self._tap0_range, self.set_tap0, "tap0", "slider", float)
        self.controls_grid_layout_1.addWidget(self._tap0_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.controls_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 1):
            self.controls_grid_layout_1.setColumnStretch(c, 1)
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
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	Rs, #bw
        	"", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0.enable_axis_labels(True)

        if not True:
          self.qtgui_waterfall_sink_x_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0.set_intensity_range(-50, -30)

        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.canal_grid_layout_0.addWidget(self._qtgui_waterfall_sink_x_0_win, 1, 1, 1, 1)
        for r in range(1, 2):
            self.canal_grid_layout_0.setRowStretch(r, 1)
        for c in range(1, 2):
            self.canal_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0_1_0_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	Rs, #bw
        	'', #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_1_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_1_0_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_1_0_0.set_y_label('H(f)', 'dB')
        self.qtgui_freq_sink_x_0_1_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_1_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_1_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_1_0_0.set_fft_average(0.05)
        self.qtgui_freq_sink_x_0_1_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_1_0_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0_1_0_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_1_0_0.set_plot_pos_half(not True)

        labels = ['Equalizer output', 'salida del canal', '', '', '',
                  '', '', '', '', '']
        widths = [2, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_1_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_1_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_1_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_1_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_1_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_1_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_1_0_0.pyqwidget(), Qt.QWidget)
        self.canal_grid_layout_4.addWidget(self._qtgui_freq_sink_x_0_1_0_0_win, 1, 1, 1, 1)
        for r in range(1, 2):
            self.canal_grid_layout_4.setRowStretch(r, 1)
        for c in range(1, 2):
            self.canal_grid_layout_4.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0_1_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	Rs*Sps_o, #bw
        	'', #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_1_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_1_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_1_0.set_y_label('H(f)', 'dB')
        self.qtgui_freq_sink_x_0_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_1_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_1_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_1_0.set_fft_average(0.05)
        self.qtgui_freq_sink_x_0_1_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_1_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0_1_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_1_0.set_plot_pos_half(not True)

        labels = ['Equalizer input', 'salida del canal', '', '', '',
                  '', '', '', '', '']
        widths = [2, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_1_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_1_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_1_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_1_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_1_0.pyqwidget(), Qt.QWidget)
        self.canal_grid_layout_4.addWidget(self._qtgui_freq_sink_x_0_1_0_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.canal_grid_layout_4.setRowStretch(r, 1)
        for c in range(0, 1):
            self.canal_grid_layout_4.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0_1 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	Rs, #bw
        	'', #name
        	2 #number of inputs
        )
        self.qtgui_freq_sink_x_0_1.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_1.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_1.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_1.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_1.enable_grid(False)
        self.qtgui_freq_sink_x_0_1.set_fft_average(0.05)
        self.qtgui_freq_sink_x_0_1.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_1.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0_1.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_1.set_plot_pos_half(not True)

        labels = ['Entrada del canal', 'salida del canal', '', '', '',
                  '', '', '', '', '']
        widths = [2, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_1.pyqwidget(), Qt.QWidget)
        self.canal_grid_layout_0.addWidget(self._qtgui_freq_sink_x_0_1_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.canal_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.canal_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_const_sink_x_0_1_1_0_0_0 = qtgui.const_sink_c(
        	1024, #size
        	'', #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0_1_1_0_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_1_1_0_0_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0_1_1_0_0_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0_1_1_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_1_1_0_0_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0_1_1_0_0_0.enable_grid(False)
        self.qtgui_const_sink_x_0_1_1_0_0_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0_1_1_0_0_0.disable_legend()

        labels = ['Equalizer output', 'Salida del Ecualizador', '', 'Filtro RRC y MPSK Timing Recovery', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "blue", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_1_1_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_1_1_0_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_1_1_0_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_1_1_0_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_1_1_0_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_1_1_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_1_1_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_1_1_0_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_1_1_0_0_0.pyqwidget(), Qt.QWidget)
        self.canal_grid_layout_4.addWidget(self._qtgui_const_sink_x_0_1_1_0_0_0_win, 0, 1, 1, 1)
        for r in range(0, 1):
            self.canal_grid_layout_4.setRowStretch(r, 1)
        for c in range(1, 2):
            self.canal_grid_layout_4.setColumnStretch(c, 1)
        self.qtgui_const_sink_x_0_1_1_0_0 = qtgui.const_sink_c(
        	1024, #size
        	'', #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0_1_1_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_1_1_0_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0_1_1_0_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0_1_1_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_1_1_0_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0_1_1_0_0.enable_grid(False)
        self.qtgui_const_sink_x_0_1_1_0_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0_1_1_0_0.disable_legend()

        labels = ['Equalizer input', 'Salida del Ecualizador', '', 'Filtro RRC y MPSK Timing Recovery', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "blue", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_1_1_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_1_1_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_1_1_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_1_1_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_1_1_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_1_1_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_1_1_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_1_1_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_1_1_0_0.pyqwidget(), Qt.QWidget)
        self.canal_grid_layout_4.addWidget(self._qtgui_const_sink_x_0_1_1_0_0_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.canal_grid_layout_4.setRowStretch(r, 1)
        for c in range(0, 1):
            self.canal_grid_layout_4.setColumnStretch(c, 1)
        self.qtgui_const_sink_x_0_1_1_0 = qtgui.const_sink_c(
        	1024, #size
        	'', #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0_1_1_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_1_1_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0_1_1_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0_1_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_1_1_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0_1_1_0.enable_grid(False)
        self.qtgui_const_sink_x_0_1_1_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0_1_1_0.disable_legend()

        labels = ['Salida del Ecualizador', 'Salida del Ecualizador', '', 'Filtro RRC y MPSK Timing Recovery', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "blue", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_1_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_1_1_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_1_1_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_1_1_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_1_1_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_1_1_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_1_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_1_1_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_1_1_0.pyqwidget(), Qt.QWidget)
        self.canal_grid_layout_3.addWidget(self._qtgui_const_sink_x_0_1_1_0_win, 1, 1, 1, 1)
        for r in range(1, 2):
            self.canal_grid_layout_3.setRowStretch(r, 1)
        for c in range(1, 2):
            self.canal_grid_layout_3.setColumnStretch(c, 1)
        self.qtgui_const_sink_x_0_1_1 = qtgui.const_sink_c(
        	1024, #size
        	'', #name
        	2 #number of inputs
        )
        self.qtgui_const_sink_x_0_1_1.set_update_time(0.10)
        self.qtgui_const_sink_x_0_1_1.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0_1_1.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0_1_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_1_1.enable_autoscale(False)
        self.qtgui_const_sink_x_0_1_1.enable_grid(False)
        self.qtgui_const_sink_x_0_1_1.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0_1_1.disable_legend()

        labels = ['Entrada de canal', 'Salida del Canal', '', 'Filtro RRC y MPSK Timing Recovery', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "blue", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_1_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_1_1.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_1_1.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_1_1.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_1_1.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_1_1.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_1_1.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_1_1_win = sip.wrapinstance(self.qtgui_const_sink_x_0_1_1.pyqwidget(), Qt.QWidget)
        self.canal_grid_layout_3.addWidget(self._qtgui_const_sink_x_0_1_1_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.canal_grid_layout_3.setRowStretch(r, 1)
        for c in range(0, 1):
            self.canal_grid_layout_3.setColumnStretch(c, 1)
        self.digital_pfb_clock_sync_xxx_0_0 = digital.pfb_clock_sync_ccf(Sps, 2*math.pi/100.0, (rrc_taps_rx), nfilts, nfilts/2, 1.5, 1)
        self.digital_pfb_clock_sync_xxx_0 = digital.pfb_clock_sync_ccf(Sps, 2*math.pi/100.0, (rrc_taps_rx), nfilts, nfilts/2, 1.5, Sps_o)
        self.digital_lms_dd_equalizer_cc_0 = digital.lms_dd_equalizer_cc(11, eq_gain, Sps_o, MiconstellationObject)
        self.digital_constellation_decoder_cb_0_0 = digital.constellation_decoder_cb(MiconstellationObject)
        self.digital_constellation_decoder_cb_0 = digital.constellation_decoder_cb(MiconstellationObject)
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc((Constelacion), 1)
        self.channels_channel_model_0 = channels.channel_model(
        	noise_voltage=math.pow(10.,(NodB)/20.),
        	frequency_offset=Ch_Frec_offset,
        	epsilon=Ch_Jitter+1.,
        	taps=(Ch_taps),
        	noise_seed=13,
        	block_tags=False
        )
        self.blocks_null_sink_1_0 = blocks.null_sink(gr.sizeof_char*1)
        self.blocks_null_sink_1 = blocks.null_sink(gr.sizeof_char*1)
        self.blocks_delay_0_0 = blocks.delay(gr.sizeof_gr_complex*1, Ch_Delay*Sps)
        self.b_RRaised_cosine_cc_0 = b_RRaised_cosine_cc(
            Ganancia=1.,
            Interpolation=Sps,
            ntaps=ntaps*Sps,
            rolloff=rolloff,
            sps=Sps,
        )
        self.b_Eye_Diagram_simple_c_0_0 = b_Eye_Diagram_simple_c(
            AlphaLineas=0.5,
            Delay_i=0,
            GrosorLineas=20,
            Kint=1,
            N_eyes=2,
            Samprate1=samp_rate,
            Sps1=Sps,
            Title="Entrada del ecualizador",
            Ymax=2,
            Ymin=-2,
        )
        self.canal_grid_layout_2.addWidget(self.b_Eye_Diagram_simple_c_0_0, 1, 0, 1, 1)
        for r in range(1, 2):
            self.canal_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 1):
            self.canal_grid_layout_2.setColumnStretch(c, 1)
        self.b_Eye_Diagram_simple_c_0 = b_Eye_Diagram_simple_c(
            AlphaLineas=0.5,
            Delay_i=0,
            GrosorLineas=20,
            Kint=1,
            N_eyes=2,
            Samprate1=samp_rate,
            Sps1=Sps,
            Title="salida del canal",
            Ymax=2,
            Ymin=-2,
        )
        self.canal_grid_layout_1.addWidget(self.b_Eye_Diagram_simple_c_0, 1, 0, 1, 1)
        for r in range(1, 2):
            self.canal_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 1):
            self.canal_grid_layout_1.setColumnStretch(c, 1)
        self.analog_random_source_x_0 = blocks.vector_source_b(map(int, numpy.random.randint(0, M, 1000000)), True)
        self.analog_agc2_xx_0 = analog.agc2_cc(1e-1, 1e-2, 1.0, 1.0)
        self.analog_agc2_xx_0.set_max_gain(65536)
        self._SymbTune_range = Range(0, 1000, 1, 2, 200)
        self._SymbTune_win = RangeWidget(self._SymbTune_range, self.set_SymbTune, 'SymbTunning', "counter", int)
        self.controls_grid_layout_2.addWidget(self._SymbTune_win, 0, 1, 1, 1)
        for r in range(0, 1):
            self.controls_grid_layout_2.setRowStretch(r, 1)
        for c in range(1, 2):
            self.controls_grid_layout_2.setColumnStretch(c, 1)
        self.Pre_modulacion = Qt.QTabWidget()
        self.Pre_modulacion_widget_0 = Qt.QWidget()
        self.Pre_modulacion_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Pre_modulacion_widget_0)
        self.Pre_modulacion_grid_layout_0 = Qt.QGridLayout()
        self.Pre_modulacion_layout_0.addLayout(self.Pre_modulacion_grid_layout_0)
        self.Pre_modulacion.addTab(self.Pre_modulacion_widget_0, 'Capa8.Mensaje continuo')
        self.Pre_modulacion_widget_1 = Qt.QWidget()
        self.Pre_modulacion_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Pre_modulacion_widget_1)
        self.Pre_modulacion_grid_layout_1 = Qt.QGridLayout()
        self.Pre_modulacion_layout_1.addLayout(self.Pre_modulacion_grid_layout_1)
        self.Pre_modulacion.addTab(self.Pre_modulacion_widget_1, 'Capa7.Cuantificacion')
        self.Pre_modulacion_widget_2 = Qt.QWidget()
        self.Pre_modulacion_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Pre_modulacion_widget_2)
        self.Pre_modulacion_grid_layout_2 = Qt.QGridLayout()
        self.Pre_modulacion_layout_2.addLayout(self.Pre_modulacion_grid_layout_2)
        self.Pre_modulacion.addTab(self.Pre_modulacion_widget_2, 'Capa6.PCM')
        self.Pre_modulacion_widget_3 = Qt.QWidget()
        self.Pre_modulacion_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Pre_modulacion_widget_3)
        self.Pre_modulacion_grid_layout_3 = Qt.QGridLayout()
        self.Pre_modulacion_layout_3.addLayout(self.Pre_modulacion_grid_layout_3)
        self.Pre_modulacion.addTab(self.Pre_modulacion_widget_3, 'Capa5.Otrastecnicas')
        self.Pre_modulacion_widget_4 = Qt.QWidget()
        self.Pre_modulacion_layout_4 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Pre_modulacion_widget_4)
        self.Pre_modulacion_grid_layout_4 = Qt.QGridLayout()
        self.Pre_modulacion_layout_4.addLayout(self.Pre_modulacion_grid_layout_4)
        self.Pre_modulacion.addTab(self.Pre_modulacion_widget_4, 'Capa4.CodificacionBinaria')
        self.Pre_modulacion_widget_5 = Qt.QWidget()
        self.Pre_modulacion_layout_5 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Pre_modulacion_widget_5)
        self.Pre_modulacion_grid_layout_5 = Qt.QGridLayout()
        self.Pre_modulacion_layout_5.addLayout(self.Pre_modulacion_grid_layout_5)
        self.Pre_modulacion.addTab(self.Pre_modulacion_widget_5, 'Capa3.M-PAM')
        self.Instrumentos_grid_layout_1.addWidget(self.Pre_modulacion, 1, 0, 1, 1)
        for r in range(1, 2):
            self.Instrumentos_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 1):
            self.Instrumentos_grid_layout_1.setColumnStretch(c, 1)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_agc2_xx_0, 0), (self.b_Eye_Diagram_simple_c_0, 0))
        self.connect((self.analog_agc2_xx_0, 0), (self.digital_pfb_clock_sync_xxx_0, 0))
        self.connect((self.analog_agc2_xx_0, 0), (self.digital_pfb_clock_sync_xxx_0_0, 0))
        self.connect((self.analog_random_source_x_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))
        self.connect((self.b_RRaised_cosine_cc_0, 0), (self.channels_channel_model_0, 0))
        self.connect((self.blocks_delay_0_0, 0), (self.analog_agc2_xx_0, 0))
        self.connect((self.channels_channel_model_0, 0), (self.blocks_delay_0_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.b_RRaised_cosine_cc_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.qtgui_const_sink_x_0_1_1, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.qtgui_freq_sink_x_0_1, 0))
        self.connect((self.digital_constellation_decoder_cb_0, 0), (self.blocks_null_sink_1, 0))
        self.connect((self.digital_constellation_decoder_cb_0_0, 0), (self.blocks_null_sink_1_0, 0))
        self.connect((self.digital_lms_dd_equalizer_cc_0, 0), (self.digital_constellation_decoder_cb_0, 0))
        self.connect((self.digital_lms_dd_equalizer_cc_0, 0), (self.qtgui_const_sink_x_0_1_1_0, 0))
        self.connect((self.digital_lms_dd_equalizer_cc_0, 0), (self.qtgui_const_sink_x_0_1_1_0_0_0, 0))
        self.connect((self.digital_lms_dd_equalizer_cc_0, 0), (self.qtgui_freq_sink_x_0_1_0_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.b_Eye_Diagram_simple_c_0_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.digital_lms_dd_equalizer_cc_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.qtgui_const_sink_x_0_1_1_0_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.qtgui_freq_sink_x_0_1_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0_0, 0), (self.digital_constellation_decoder_cb_0_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0_0, 0), (self.qtgui_const_sink_x_0_1_1, 1))
        self.connect((self.digital_pfb_clock_sync_xxx_0_0, 0), (self.qtgui_freq_sink_x_0_1, 1))
        self.connect((self.digital_pfb_clock_sync_xxx_0_0, 0), (self.qtgui_waterfall_sink_x_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "Lab_total")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate_audio(self):
        return self.samp_rate_audio

    def set_samp_rate_audio(self, samp_rate_audio):
        self.samp_rate_audio = samp_rate_audio
        self.set_Rbi(self.NbpS*self.samp_rate_audio)

    def get_NbpS(self):
        return self.NbpS

    def set_NbpS(self, NbpS):
        self.NbpS = NbpS
        self.set_Rbi(self.NbpS*self.samp_rate_audio)
        self.set_NnivelesQ(math.pow(2,self.NbpS))

    def get_Constelacion(self):
        return self.Constelacion

    def set_Constelacion(self, Constelacion):
        self.Constelacion = Constelacion
        self.set_M(len(self.Constelacion))
        self.digital_chunks_to_symbols_xx_0.set_symbol_table((self.Constelacion))

    def get_Rbi(self):
        return self.Rbi

    def set_Rbi(self, Rbi):
        self.Rbi = Rbi
        self.set_Rb(self.Rbi)

    def get_M(self):
        return self.M

    def set_M(self, M):
        self.M = M
        self.set_Bps(int(math.log(self.M,2)))

    def get_Sps(self):
        return self.Sps

    def set_Sps(self, Sps):
        self.Sps = Sps
        self.set_samp_rate(self.Rs*self.Sps)
        self.set_rrc_taps_rx(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.Sps), self.rolloff, self.ntaps*self.nfilts))
        self.set_ntaps(self.Sps*16)
        self.set_Sps_o(self.Sps)
        self.blocks_delay_0_0.set_dly(self.Ch_Delay*self.Sps)
        self.b_RRaised_cosine_cc_0.set_Interpolation(self.Sps)
        self.b_RRaised_cosine_cc_0.set_ntaps(self.ntaps*self.Sps)
        self.b_RRaised_cosine_cc_0.set_sps(self.Sps)
        self.b_Eye_Diagram_simple_c_0_0.set_Sps1(self.Sps)
        self.b_Eye_Diagram_simple_c_0.set_Sps1(self.Sps)

    def get_Rb(self):
        return self.Rb

    def set_Rb(self, Rb):
        self.Rb = Rb
        self.set_Rs(self.Rb/self.Bps)

    def get_Bps(self):
        return self.Bps

    def set_Bps(self, Bps):
        self.Bps = Bps
        self.set_Rs(self.Rb/self.Bps)

    def get_tap7(self):
        return self.tap7

    def set_tap7(self, tap7):
        self.tap7 = tap7
        self.set_Ch_taps(fftpack.ifftshift(fftpack.ifft([self.tap0, self.tap1, self.tap2, self.tap3, self.tap4, self.tap5, self.tap6, self.tap7])))

    def get_tap6(self):
        return self.tap6

    def set_tap6(self, tap6):
        self.tap6 = tap6
        self.set_Ch_taps(fftpack.ifftshift(fftpack.ifft([self.tap0, self.tap1, self.tap2, self.tap3, self.tap4, self.tap5, self.tap6, self.tap7])))

    def get_tap5(self):
        return self.tap5

    def set_tap5(self, tap5):
        self.tap5 = tap5
        self.set_Ch_taps(fftpack.ifftshift(fftpack.ifft([self.tap0, self.tap1, self.tap2, self.tap3, self.tap4, self.tap5, self.tap6, self.tap7])))

    def get_tap4(self):
        return self.tap4

    def set_tap4(self, tap4):
        self.tap4 = tap4
        self.set_Ch_taps(fftpack.ifftshift(fftpack.ifft([self.tap0, self.tap1, self.tap2, self.tap3, self.tap4, self.tap5, self.tap6, self.tap7])))

    def get_tap3(self):
        return self.tap3

    def set_tap3(self, tap3):
        self.tap3 = tap3
        self.set_Ch_taps(fftpack.ifftshift(fftpack.ifft([self.tap0, self.tap1, self.tap2, self.tap3, self.tap4, self.tap5, self.tap6, self.tap7])))

    def get_tap2(self):
        return self.tap2

    def set_tap2(self, tap2):
        self.tap2 = tap2
        self.set_Ch_taps(fftpack.ifftshift(fftpack.ifft([self.tap0, self.tap1, self.tap2, self.tap3, self.tap4, self.tap5, self.tap6, self.tap7])))

    def get_tap1(self):
        return self.tap1

    def set_tap1(self, tap1):
        self.tap1 = tap1
        self.set_Ch_taps(fftpack.ifftshift(fftpack.ifft([self.tap0, self.tap1, self.tap2, self.tap3, self.tap4, self.tap5, self.tap6, self.tap7])))

    def get_tap0(self):
        return self.tap0

    def set_tap0(self, tap0):
        self.tap0 = tap0
        self.set_Ch_taps(fftpack.ifftshift(fftpack.ifft([self.tap0, self.tap1, self.tap2, self.tap3, self.tap4, self.tap5, self.tap6, self.tap7])))

    def get_rolloff(self):
        return self.rolloff

    def set_rolloff(self, rolloff):
        self.rolloff = rolloff
        self.set_rrc_taps_rx(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.Sps), self.rolloff, self.ntaps*self.nfilts))
        self.b_RRaised_cosine_cc_0.set_rolloff(self.rolloff)

    def get_ntaps(self):
        return self.ntaps

    def set_ntaps(self, ntaps):
        self.ntaps = ntaps
        self.set_rrc_taps_rx(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.Sps), self.rolloff, self.ntaps*self.nfilts))
        self.b_RRaised_cosine_cc_0.set_ntaps(self.ntaps*self.Sps)

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts
        self.set_rrc_taps_rx(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.Sps), self.rolloff, self.ntaps*self.nfilts))

    def get_code1(self):
        return self.code1

    def set_code1(self, code1):
        self.code1 = code1
        self.set_NbpCode(len(self.code1)+10.)

    def get_Rs(self):
        return self.Rs

    def set_Rs(self, Rs):
        self.Rs = Rs
        self.set_samp_rate(self.Rs*self.Sps)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.Rs)
        self.qtgui_freq_sink_x_0_1_0_0.set_frequency_range(0, self.Rs)
        self.qtgui_freq_sink_x_0_1_0.set_frequency_range(0, self.Rs*self.Sps_o)
        self.qtgui_freq_sink_x_0_1.set_frequency_range(0, self.Rs)
        self.set_W(self.Rs/2)
        self.set_Tmax_scope(64./self.Rs)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.b_Eye_Diagram_simple_c_0_0.set_Samprate1(self.samp_rate)
        self.b_Eye_Diagram_simple_c_0.set_Samprate1(self.samp_rate)

    def get_run_stop(self):
        return self.run_stop

    def set_run_stop(self, run_stop):
        self.run_stop = run_stop
        self._run_stop_callback(self.run_stop)
        if self.run_stop: self.start()
        else: self.stop(); self.wait()

    def get_rrc_taps_rx(self):
        return self.rrc_taps_rx

    def set_rrc_taps_rx(self, rrc_taps_rx):
        self.rrc_taps_rx = rrc_taps_rx
        self.digital_pfb_clock_sync_xxx_0_0.update_taps((self.rrc_taps_rx))
        self.digital_pfb_clock_sync_xxx_0.update_taps((self.rrc_taps_rx))

    def get_payload(self):
        return self.payload

    def set_payload(self, payload):
        self.payload = payload

    def get_eq_gain(self):
        return self.eq_gain

    def set_eq_gain(self, eq_gain):
        self.eq_gain = eq_gain
        self.digital_lms_dd_equalizer_cc_0.set_gain(self.eq_gain)

    def get_W(self):
        return self.W

    def set_W(self, W):
        self.W = W

    def get_Vp(self):
        return self.Vp

    def set_Vp(self, Vp):
        self.Vp = Vp

    def get_Tmax_scope(self):
        return self.Tmax_scope

    def set_Tmax_scope(self, Tmax_scope):
        self.Tmax_scope = Tmax_scope

    def get_SymbTune(self):
        return self.SymbTune

    def set_SymbTune(self, SymbTune):
        self.SymbTune = SymbTune

    def get_Sps_o(self):
        return self.Sps_o

    def set_Sps_o(self, Sps_o):
        self.Sps_o = Sps_o
        self.qtgui_freq_sink_x_0_1_0.set_frequency_range(0, self.Rs*self.Sps_o)

    def get_NodB(self):
        return self.NodB

    def set_NodB(self, NodB):
        self.NodB = NodB
        self.channels_channel_model_0.set_noise_voltage(math.pow(10.,(self.NodB)/20.))

    def get_NnivelesQ(self):
        return self.NnivelesQ

    def set_NnivelesQ(self, NnivelesQ):
        self.NnivelesQ = NnivelesQ

    def get_NbpCode(self):
        return self.NbpCode

    def set_NbpCode(self, NbpCode):
        self.NbpCode = NbpCode

    def get_MiconstellationObject(self):
        return self.MiconstellationObject

    def set_MiconstellationObject(self, MiconstellationObject):
        self.MiconstellationObject = MiconstellationObject

    def get_Fc(self):
        return self.Fc

    def set_Fc(self, Fc):
        self.Fc = Fc

    def get_Ch_taps(self):
        return self.Ch_taps

    def set_Ch_taps(self, Ch_taps):
        self.Ch_taps = Ch_taps
        self.channels_channel_model_0.set_taps((self.Ch_taps))

    def get_Ch_Jitter(self):
        return self.Ch_Jitter

    def set_Ch_Jitter(self, Ch_Jitter):
        self.Ch_Jitter = Ch_Jitter
        self.channels_channel_model_0.set_timing_offset(self.Ch_Jitter+1.)

    def get_Ch_Frec_offset(self):
        return self.Ch_Frec_offset

    def set_Ch_Frec_offset(self, Ch_Frec_offset):
        self.Ch_Frec_offset = Ch_Frec_offset
        self.channels_channel_model_0.set_frequency_offset(self.Ch_Frec_offset)

    def get_Ch_Delay(self):
        return self.Ch_Delay

    def set_Ch_Delay(self, Ch_Delay):
        self.Ch_Delay = Ch_Delay
        self.blocks_delay_0_0.set_dly(self.Ch_Delay*self.Sps)

    def get_Am(self):
        return self.Am

    def set_Am(self, Am):
        self.Am = Am


def main(top_block_cls=Lab_total, options=None):

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
