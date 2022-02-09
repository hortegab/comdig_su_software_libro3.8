#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Lab Total
# GNU Radio version: 3.9.5.0

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

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from b_PSD_VRMS_2ways import b_PSD_VRMS_2ways  # grc-generated hier_block
from b_bipolar_to_unipolar_ff import b_bipolar_to_unipolar_ff  # grc-generated hier_block
from b_quantizer_fb import b_quantizer_fb  # grc-generated hier_block
from b_scrambling_ff import b_scrambling_ff  # grc-generated hier_block
from gnuradio import analog
from gnuradio import blocks
from gnuradio import gr
from gnuradio.fft import window
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import E3TRadio
import cmath
import math
import numpy
import random



from gnuradio import qtgui

class Lab_total(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Lab Total", catch_exceptions=True)
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
        self.samp_rate_audio = samp_rate_audio = 11000
        self.NbpS = NbpS = 8
        self.Rb = Rb = NbpS*samp_rate_audio
        self.run_stop = run_stop = True
        self.Vp = Vp = 0.6
        self.Tmax_scope = Tmax_scope = 16./samp_rate_audio
        self.Sps = Sps = 16
        self.Rs = Rs = Rb
        self.NnivelesQ = NnivelesQ = int(math.pow(2,NbpS))
        self.N = N = 1024
        self.Fc = Fc = 80e6
        self.Ensayos = Ensayos = 1000000

        ##################################################
        # Blocks
        ##################################################
        self.menu = Qt.QTabWidget()
        self.menu_widget_0 = Qt.QWidget()
        self.menu_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.menu_widget_0)
        self.menu_grid_layout_0 = Qt.QGridLayout()
        self.menu_layout_0.addLayout(self.menu_grid_layout_0)
        self.menu.addTab(self.menu_widget_0, 'Tab 0')
        self.top_layout.addWidget(self.menu)
        _run_stop_check_box = Qt.QCheckBox("Inicial/Parar")
        self._run_stop_choices = {True: True, False: False}
        self._run_stop_choices_inv = dict((v,k) for k,v in self._run_stop_choices.items())
        self._run_stop_callback = lambda i: Qt.QMetaObject.invokeMethod(_run_stop_check_box, "setChecked", Qt.Q_ARG("bool", self._run_stop_choices_inv[i]))
        self._run_stop_callback(self.run_stop)
        _run_stop_check_box.stateChanged.connect(lambda i: self.set_run_stop(self._run_stop_choices[bool(i)]))
        self.menu_grid_layout_0.addWidget(_run_stop_check_box, 0, 0, 1, 2)
        for r in range(0, 1):
            self.menu_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 2):
            self.menu_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_f(
            16*Sps, #size
            Rb*Sps, #samp_rate
            "", #name
            3, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0.set_y_axis(-1.5, 1.5)

        self.qtgui_time_sink_x_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0.enable_tags(True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0.enable_stem_plot(False)


        labels = ['b(t)', 'c(t)', 'bs(t)', '', '',
            '', '', '', '', '']
        widths = [4, 4, 4, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(3):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.qwidget(), Qt.QWidget)
        self.menu_grid_layout_0.addWidget(self._qtgui_time_sink_x_0_0_win, 3, 0, 1, 1)
        for r in range(3, 4):
            self.menu_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.menu_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
            16, #size
            Rb, #samp_rate
            "", #name
            3, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1.5, 1.5)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)


        labels = ["PCM ", 'Codigo', 'Con Scrambling', '', '',
            '', '', '', '', '']
        widths = [4, 4, 4, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 0, 3, 1, 1,
            1, 1, 1, 1, 1]
        markers = [0, 0, 0, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(3):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.qwidget(), Qt.QWidget)
        self.menu_grid_layout_0.addWidget(self._qtgui_time_sink_x_0_win, 2, 0, 1, 1)
        for r in range(2, 3):
            self.menu_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.menu_grid_layout_0.setColumnStretch(c, 1)
        self.blocks_wavfile_source_0 = blocks.wavfile_source('/home/labcom/MisGits/comdig_su_software_libro3.8/Generacion_de_las_figuras_del_libro/bush-clinton_debate_waffle.wav', True)
        self.blocks_unpack_k_bits_bb_0_1 = blocks.unpack_k_bits_bb(NbpS)
        self.blocks_pack_k_bits_bb_0 = blocks.pack_k_bits_bb(NbpS)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_multiply_const_vxx_0_1 = blocks.multiply_const_ff(1.2)
        self.blocks_multiply_const_vxx_0_0_1 = blocks.multiply_const_ff(1.4)
        self.blocks_multiply_const_vxx_0_0_0 = blocks.multiply_const_ff(Vp/(NnivelesQ/2))
        self.blocks_float_to_char_0 = blocks.float_to_char(1, 1)
        self.blocks_char_to_float_0_0_0 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_0_0 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)
        self.b_scrambling_ff_0_0 = b_scrambling_ff(
            retardo=0,
            semilla=42,
        )
        self.b_scrambling_ff_0 = b_scrambling_ff(
            retardo=0,
            semilla=42,
        )
        self.b_quantizer_fb_0 = b_quantizer_fb(
            NivelesQ=NnivelesQ,
            Vmax=Vp,
        )
        self.b_bipolar_to_unipolar_ff_0 = b_bipolar_to_unipolar_ff()
        self.b_PSD_VRMS_2ways_0_0_0 = b_PSD_VRMS_2ways(
            Amp=100,
            Ensayos=1000000,
            N=1024,
            samp_rate_audio=Rb,
        )

        self.menu_grid_layout_0.addWidget(self.b_PSD_VRMS_2ways_0_0_0, 1, 0, 1, 1)
        for r in range(1, 2):
            self.menu_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.menu_grid_layout_0.setColumnStretch(c, 1)
        self.analog_random_uniform_source_x_0 = analog.random_uniform_source_b(0, 2, 42)
        self.E3TRadio_unipolar_to_bipolar_ff_0_0 = E3TRadio.unipolar_to_bipolar_ff(1.)
        self.E3TRadio_unipolar_to_bipolar_ff_0 = E3TRadio.unipolar_to_bipolar_ff(1.)
        self.E3TRadio_Zero_Order_Hold_0_0_0 = E3TRadio.Zero_Order_Hold(Sps)
        self.E3TRadio_Zero_Order_Hold_0_0 = E3TRadio.Zero_Order_Hold(Sps)
        self.E3TRadio_Zero_Order_Hold_0 = E3TRadio.Zero_Order_Hold(Sps)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.E3TRadio_Zero_Order_Hold_0, 0), (self.qtgui_time_sink_x_0_0, 0))
        self.connect((self.E3TRadio_Zero_Order_Hold_0_0, 0), (self.qtgui_time_sink_x_0_0, 1))
        self.connect((self.E3TRadio_Zero_Order_Hold_0_0_0, 0), (self.qtgui_time_sink_x_0_0, 2))
        self.connect((self.E3TRadio_unipolar_to_bipolar_ff_0, 0), (self.E3TRadio_Zero_Order_Hold_0, 0))
        self.connect((self.E3TRadio_unipolar_to_bipolar_ff_0, 0), (self.b_PSD_VRMS_2ways_0_0_0, 0))
        self.connect((self.E3TRadio_unipolar_to_bipolar_ff_0, 0), (self.b_scrambling_ff_0, 0))
        self.connect((self.E3TRadio_unipolar_to_bipolar_ff_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.E3TRadio_unipolar_to_bipolar_ff_0_0, 0), (self.blocks_multiply_const_vxx_0_1, 0))
        self.connect((self.analog_random_uniform_source_x_0, 0), (self.blocks_char_to_float_0_0_0, 0))
        self.connect((self.b_bipolar_to_unipolar_ff_0, 0), (self.blocks_float_to_char_0, 0))
        self.connect((self.b_quantizer_fb_0, 0), (self.blocks_unpack_k_bits_bb_0_1, 0))
        self.connect((self.b_scrambling_ff_0, 0), (self.b_PSD_VRMS_2ways_0_0_0, 1))
        self.connect((self.b_scrambling_ff_0, 0), (self.b_scrambling_ff_0_0, 0))
        self.connect((self.b_scrambling_ff_0, 0), (self.blocks_multiply_const_vxx_0_0_1, 0))
        self.connect((self.b_scrambling_ff_0_0, 0), (self.b_bipolar_to_unipolar_ff_0, 0))
        self.connect((self.blocks_char_to_float_0, 0), (self.blocks_multiply_const_vxx_0_0_0, 0))
        self.connect((self.blocks_char_to_float_0_0, 0), (self.E3TRadio_unipolar_to_bipolar_ff_0, 0))
        self.connect((self.blocks_char_to_float_0_0_0, 0), (self.E3TRadio_unipolar_to_bipolar_ff_0_0, 0))
        self.connect((self.blocks_float_to_char_0, 0), (self.blocks_pack_k_bits_bb_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0_0, 0), (self.blocks_null_sink_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0_1, 0), (self.E3TRadio_Zero_Order_Hold_0_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0_1, 0), (self.qtgui_time_sink_x_0, 2))
        self.connect((self.blocks_multiply_const_vxx_0_1, 0), (self.E3TRadio_Zero_Order_Hold_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_1, 0), (self.qtgui_time_sink_x_0, 1))
        self.connect((self.blocks_pack_k_bits_bb_0, 0), (self.blocks_char_to_float_0, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0_1, 0), (self.blocks_char_to_float_0_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.b_quantizer_fb_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "Lab_total")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate_audio(self):
        return self.samp_rate_audio

    def set_samp_rate_audio(self, samp_rate_audio):
        self.samp_rate_audio = samp_rate_audio
        self.set_Rb(self.NbpS*self.samp_rate_audio)
        self.set_Tmax_scope(16./self.samp_rate_audio)

    def get_NbpS(self):
        return self.NbpS

    def set_NbpS(self, NbpS):
        self.NbpS = NbpS
        self.set_NnivelesQ(int(math.pow(2,self.NbpS)))
        self.set_Rb(self.NbpS*self.samp_rate_audio)

    def get_Rb(self):
        return self.Rb

    def set_Rb(self, Rb):
        self.Rb = Rb
        self.set_Rs(self.Rb)
        self.b_PSD_VRMS_2ways_0_0_0.set_samp_rate_audio(self.Rb)
        self.qtgui_time_sink_x_0.set_samp_rate(self.Rb)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.Rb*self.Sps)

    def get_run_stop(self):
        return self.run_stop

    def set_run_stop(self, run_stop):
        self.run_stop = run_stop
        if self.run_stop: self.start()
        else: self.stop(); self.wait()
        self._run_stop_callback(self.run_stop)

    def get_Vp(self):
        return self.Vp

    def set_Vp(self, Vp):
        self.Vp = Vp
        self.b_quantizer_fb_0.set_Vmax(self.Vp)
        self.blocks_multiply_const_vxx_0_0_0.set_k(self.Vp/(self.NnivelesQ/2))

    def get_Tmax_scope(self):
        return self.Tmax_scope

    def set_Tmax_scope(self, Tmax_scope):
        self.Tmax_scope = Tmax_scope

    def get_Sps(self):
        return self.Sps

    def set_Sps(self, Sps):
        self.Sps = Sps
        self.E3TRadio_Zero_Order_Hold_0.set_retardo(self.Sps)
        self.E3TRadio_Zero_Order_Hold_0_0.set_retardo(self.Sps)
        self.E3TRadio_Zero_Order_Hold_0_0_0.set_retardo(self.Sps)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.Rb*self.Sps)

    def get_Rs(self):
        return self.Rs

    def set_Rs(self, Rs):
        self.Rs = Rs

    def get_NnivelesQ(self):
        return self.NnivelesQ

    def set_NnivelesQ(self, NnivelesQ):
        self.NnivelesQ = NnivelesQ
        self.b_quantizer_fb_0.set_NivelesQ(self.NnivelesQ)
        self.blocks_multiply_const_vxx_0_0_0.set_k(self.Vp/(self.NnivelesQ/2))

    def get_N(self):
        return self.N

    def set_N(self, N):
        self.N = N

    def get_Fc(self):
        return self.Fc

    def set_Fc(self, Fc):
        self.Fc = Fc

    def get_Ensayos(self):
        return self.Ensayos

    def set_Ensayos(self, Ensayos):
        self.Ensayos = Ensayos




def main(top_block_cls=Lab_total, options=None):

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
