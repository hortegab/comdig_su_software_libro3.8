#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Lab Total
# Generated: Tue Mar  3 18:25:50 2020
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
from b_Canal_simple_cc import b_Canal_simple_cc  # grc-generated hier_block
from b_quantizer_fb import b_quantizer_fb  # grc-generated hier_block
from gnuradio import audio
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import cmath
import coding  # embedded python module
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

        self.MiconstellationObject = MiconstellationObject = digital.constellation_calcdist((digital.constellation_8psk().points()), (), 4, 1).base()

        self.Constelacion = Constelacion = MiconstellationObject.points()
        self.samp_rate_audio = samp_rate_audio = 11000
        self.NbpS = NbpS = 8
        self.M = M = len(Constelacion)
        self.Rb = Rb = NbpS*samp_rate_audio
        self.Bps = Bps = int(math.log(M,2))
        self.Sps = Sps = 2
        self.Rs = Rs = Rb/Bps
        self.samp_rate_usrp_tx = samp_rate_usrp_tx = 400e6
        self.samp_rate_usrp_rx = samp_rate_usrp_rx = 100e6
        self.samp_rate_d = samp_rate_d = Rs*Sps
        self.Ki_d = Ki_d = samp_rate_usrp_tx/samp_rate_d
        self.Kd_d = Kd_d = samp_rate_usrp_rx/samp_rate_d
        self.m1 = m1 = math.floor(math.log(Kd_d,2))
        self.m = m = math.floor(math.log(Ki_d,2))
        self.Ki = Ki = math.pow(2,m)
        self.Kd = Kd = math.pow(2,m1)
        self.samp_rate_tx = samp_rate_tx = int(samp_rate_usrp_tx/Ki)
        self.samp_rate = samp_rate = int(samp_rate_usrp_rx/Kd)
        self.run_stop = run_stop = True
        self.mapinverse = mapinverse = coding.inverse_map(Constelacion)
        self.mapdirect = mapdirect = coding.direct_map(Constelacion)
        self.Vp = Vp = 1.
        self.Tmax_scope = Tmax_scope = 16./Rs
        self.SymbTune = SymbTune = 0
        self.Path_Loss_dB = Path_Loss_dB = 0.
        self.NodB = NodB = -60.
        self.NnivelesQ = NnivelesQ = math.pow(2,NbpS)
        self.Fc = Fc = 80e6
        self.F_offset = F_offset = 0
        self.Ch_Fluct_percent = Ch_Fluct_percent = 10.
        self.Ajuste_phi = Ajuste_phi = 0.

        ##################################################
        # Blocks
        ##################################################
        self.controls = Qt.QTabWidget()
        self.controls_widget_0 = Qt.QWidget()
        self.controls_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.controls_widget_0)
        self.controls_grid_layout_0 = Qt.QGridLayout()
        self.controls_layout_0.addLayout(self.controls_grid_layout_0)
        self.controls.addTab(self.controls_widget_0, 'Manipulacion parametros del Canal')
        self.controls_widget_1 = Qt.QWidget()
        self.controls_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.controls_widget_1)
        self.controls_grid_layout_1 = Qt.QGridLayout()
        self.controls_layout_1.addLayout(self.controls_grid_layout_1)
        self.controls.addTab(self.controls_widget_1, 'Sintonizar parametros de otros bloques')
        self.top_grid_layout.addWidget(self.controls, 1, 0, 1, 2)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.canal = Qt.QTabWidget()
        self.canal_widget_0 = Qt.QWidget()
        self.canal_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.canal_widget_0)
        self.canal_grid_layout_0 = Qt.QGridLayout()
        self.canal_layout_0.addLayout(self.canal_grid_layout_0)
        self.canal.addTab(self.canal_widget_0, 'Constelaciones')
        self.canal_widget_1 = Qt.QWidget()
        self.canal_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.canal_widget_1)
        self.canal_grid_layout_1 = Qt.QGridLayout()
        self.canal_layout_1.addLayout(self.canal_grid_layout_1)
        self.canal.addTab(self.canal_widget_1, 'Tiempo')
        self.top_grid_layout.addWidget(self.canal, 2, 0, 1, 1)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._SymbTune_range = Range(0, 1000, 1, 0, 200)
        self._SymbTune_win = RangeWidget(self._SymbTune_range, self.set_SymbTune, 'SymbTunning', "counter", int)
        self.controls_grid_layout_1.addWidget(self._SymbTune_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.controls_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 1):
            self.controls_grid_layout_1.setColumnStretch(c, 1)
        self._Path_Loss_dB_range = Range(-100, 100, 1, 0., 200)
        self._Path_Loss_dB_win = RangeWidget(self._Path_Loss_dB_range, self.set_Path_Loss_dB, 'Ch_Path_Loss_dB', "counter", float)
        self.controls_grid_layout_0.addWidget(self._Path_Loss_dB_win, 0, 4, 1, 1)
        for r in range(0, 1):
            self.controls_grid_layout_0.setRowStretch(r, 1)
        for c in range(4, 5):
            self.controls_grid_layout_0.setColumnStretch(c, 1)
        self._NodB_range = Range(-100, 100, 1, -60., 200)
        self._NodB_win = RangeWidget(self._NodB_range, self.set_NodB, 'Ch Noise dB', "counter", float)
        self.controls_grid_layout_0.addWidget(self._NodB_win, 0, 3, 1, 1)
        for r in range(0, 1):
            self.controls_grid_layout_0.setRowStretch(r, 1)
        for c in range(3, 4):
            self.controls_grid_layout_0.setColumnStretch(c, 1)
        self._F_offset_range = Range(-100, 100, 0.01, 0, 200)
        self._F_offset_win = RangeWidget(self._F_offset_range, self.set_F_offset, 'Ch_Frec_offset (Hz)', "counter", float)
        self.controls_grid_layout_0.addWidget(self._F_offset_win, 0, 1, 1, 1)
        for r in range(0, 1):
            self.controls_grid_layout_0.setRowStretch(r, 1)
        for c in range(1, 2):
            self.controls_grid_layout_0.setColumnStretch(c, 1)
        self._Ajuste_phi_range = Range(-2.*math.pi, 2.*math.pi, 4*math.pi/200., 0., 200)
        self._Ajuste_phi_win = RangeWidget(self._Ajuste_phi_range, self.set_Ajuste_phi, 'Ch_Desajuste_phi (Rad)', "counter", float)
        self.controls_grid_layout_0.addWidget(self._Ajuste_phi_win, 0, 2, 1, 1)
        for r in range(0, 1):
            self.controls_grid_layout_0.setRowStretch(r, 1)
        for c in range(2, 3):
            self.controls_grid_layout_0.setColumnStretch(c, 1)
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
        self.qtgui_const_sink_x_0_2_0_0 = qtgui.const_sink_c(
        	1024, #size
        	'', #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0_2_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_2_0_0.set_y_axis(-1.5, 1.5)
        self.qtgui_const_sink_x_0_2_0_0.set_x_axis(-2.0, 2.0)
        self.qtgui_const_sink_x_0_2_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_2_0_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0_2_0_0.enable_grid(False)
        self.qtgui_const_sink_x_0_2_0_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0_2_0_0.disable_legend()

        labels = ["Salida del canal                                                                         ", 'Tx.Modulador-salida', "Salida del canal", '', '',
                  '', '', '', '', '']
        widths = [1, 6, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["green", "red", "magenta", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_2_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_2_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_2_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_2_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_2_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_2_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_2_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_2_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_2_0_0.pyqwidget(), Qt.QWidget)
        self.canal_grid_layout_0.addWidget(self._qtgui_const_sink_x_0_2_0_0_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.canal_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.canal_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_const_sink_x_0_2_0 = qtgui.const_sink_c(
        	1024, #size
        	'', #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0_2_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_2_0.set_y_axis(-1.5, 1.5)
        self.qtgui_const_sink_x_0_2_0.set_x_axis(-2.0, 2.0)
        self.qtgui_const_sink_x_0_2_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_2_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0_2_0.enable_grid(False)
        self.qtgui_const_sink_x_0_2_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0_2_0.disable_legend()

        labels = ["Tx.Modulador-salida                                                             ", 'Tx.Modulador-salida', "Salida del canal", '', '',
                  '', '', '', '', '']
        widths = [4, 6, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["red", "red", "magenta", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_2_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_2_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_2_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_2_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_2_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_2_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_2_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_2_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_2_0.pyqwidget(), Qt.QWidget)
        self.canal_grid_layout_0.addWidget(self._qtgui_const_sink_x_0_2_0_win, 2, 0, 1, 1)
        for r in range(2, 3):
            self.canal_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.canal_grid_layout_0.setColumnStretch(c, 1)
        self.digital_map_bb_0_0 = digital.map_bb((mapinverse))
        self.digital_map_bb_0 = digital.map_bb((mapdirect))
        self.digital_diff_encoder_bb_0 = digital.diff_encoder_bb(M)
        self.digital_diff_decoder_bb_0 = digital.diff_decoder_bb(M)
        self.digital_constellation_decoder_cb_0 = digital.constellation_decoder_cb(MiconstellationObject)
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc((Constelacion), 1)
        self.blocks_wavfile_source_0 = blocks.wavfile_source('/home/uis-e3t/MisGits/comdig_pract_M_PSK/bush-clinton_debate_waffle.wav', True)
        self.blocks_unpacked_to_packed_xx_0 = blocks.unpacked_to_packed_bb(Bps, gr.GR_LSB_FIRST)
        self.blocks_packed_to_unpacked_xx_0 = blocks.packed_to_unpacked_bb(Bps, gr.GR_LSB_FIRST)
        self.blocks_multiply_const_vxx_0_0_0 = blocks.multiply_const_vff((Vp/(NnivelesQ/2), ))
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, SymbTune)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)
        self.b_quantizer_fb_0 = b_quantizer_fb(
            NivelesQ=NnivelesQ,
            Vmax=Vp,
        )
        self.b_Canal_simple_cc_0 = b_Canal_simple_cc(
            Ch_Loss_dB=Path_Loss_dB,
            Ch_NodB=NodB,
            Ch_Phoffset=Ajuste_phi,
            Ch_Toffset=0,
            Fluctuacion=Ch_Fluct_percent,
            Foffset=F_offset,
            T_fluct=M*1024,
            samp_rate=Rs,
        )
        self.audio_sink_0 = audio.sink(samp_rate_audio, '', True)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.b_Canal_simple_cc_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.b_Canal_simple_cc_0, 0), (self.qtgui_const_sink_x_0_2_0_0, 0))
        self.connect((self.b_quantizer_fb_0, 0), (self.blocks_packed_to_unpacked_xx_0, 0))
        self.connect((self.blocks_char_to_float_0, 0), (self.blocks_multiply_const_vxx_0_0_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.digital_constellation_decoder_cb_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0_0, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_packed_to_unpacked_xx_0, 0), (self.digital_diff_encoder_bb_0, 0))
        self.connect((self.blocks_unpacked_to_packed_xx_0, 0), (self.blocks_char_to_float_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.b_quantizer_fb_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.b_Canal_simple_cc_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.qtgui_const_sink_x_0_2_0, 0))
        self.connect((self.digital_constellation_decoder_cb_0, 0), (self.digital_map_bb_0_0, 0))
        self.connect((self.digital_diff_decoder_bb_0, 0), (self.blocks_unpacked_to_packed_xx_0, 0))
        self.connect((self.digital_diff_encoder_bb_0, 0), (self.digital_map_bb_0, 0))
        self.connect((self.digital_map_bb_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))
        self.connect((self.digital_map_bb_0_0, 0), (self.digital_diff_decoder_bb_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "Lab_total")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_MiconstellationObject(self):
        return self.MiconstellationObject

    def set_MiconstellationObject(self, MiconstellationObject):
        self.MiconstellationObject = MiconstellationObject

    def get_Constelacion(self):
        return self.Constelacion

    def set_Constelacion(self, Constelacion):
        self.Constelacion = Constelacion
        self.set_mapinverse(coding.inverse_map(self.Constelacion))
        self.set_mapdirect(coding.direct_map(self.Constelacion))
        self.set_M(len(self.Constelacion))
        self.digital_chunks_to_symbols_xx_0.set_symbol_table((self.Constelacion))

    def get_samp_rate_audio(self):
        return self.samp_rate_audio

    def set_samp_rate_audio(self, samp_rate_audio):
        self.samp_rate_audio = samp_rate_audio
        self.set_Rb(self.NbpS*self.samp_rate_audio)

    def get_NbpS(self):
        return self.NbpS

    def set_NbpS(self, NbpS):
        self.NbpS = NbpS
        self.set_NnivelesQ(math.pow(2,self.NbpS))
        self.set_Rb(self.NbpS*self.samp_rate_audio)

    def get_M(self):
        return self.M

    def set_M(self, M):
        self.M = M
        self.set_Bps(int(math.log(self.M,2)))
        self.b_Canal_simple_cc_0.set_T_fluct(self.M*1024)

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

    def get_Sps(self):
        return self.Sps

    def set_Sps(self, Sps):
        self.Sps = Sps
        self.set_samp_rate_d(self.Rs*self.Sps)

    def get_Rs(self):
        return self.Rs

    def set_Rs(self, Rs):
        self.Rs = Rs
        self.set_samp_rate_d(self.Rs*self.Sps)
        self.b_Canal_simple_cc_0.set_samp_rate(self.Rs)
        self.set_Tmax_scope(16./self.Rs)

    def get_samp_rate_usrp_tx(self):
        return self.samp_rate_usrp_tx

    def set_samp_rate_usrp_tx(self, samp_rate_usrp_tx):
        self.samp_rate_usrp_tx = samp_rate_usrp_tx
        self.set_samp_rate_tx(int(self.samp_rate_usrp_tx/self.Ki))
        self.set_Ki_d(self.samp_rate_usrp_tx/self.samp_rate_d)

    def get_samp_rate_usrp_rx(self):
        return self.samp_rate_usrp_rx

    def set_samp_rate_usrp_rx(self, samp_rate_usrp_rx):
        self.samp_rate_usrp_rx = samp_rate_usrp_rx
        self.set_samp_rate(int(self.samp_rate_usrp_rx/self.Kd))
        self.set_Kd_d(self.samp_rate_usrp_rx/self.samp_rate_d)

    def get_samp_rate_d(self):
        return self.samp_rate_d

    def set_samp_rate_d(self, samp_rate_d):
        self.samp_rate_d = samp_rate_d
        self.set_Ki_d(self.samp_rate_usrp_tx/self.samp_rate_d)
        self.set_Kd_d(self.samp_rate_usrp_rx/self.samp_rate_d)

    def get_Ki_d(self):
        return self.Ki_d

    def set_Ki_d(self, Ki_d):
        self.Ki_d = Ki_d
        self.set_m(math.floor(math.log(self.Ki_d,2)))

    def get_Kd_d(self):
        return self.Kd_d

    def set_Kd_d(self, Kd_d):
        self.Kd_d = Kd_d
        self.set_m1(math.floor(math.log(self.Kd_d,2)))

    def get_m1(self):
        return self.m1

    def set_m1(self, m1):
        self.m1 = m1
        self.set_Kd(math.pow(2,self.m1))

    def get_m(self):
        return self.m

    def set_m(self, m):
        self.m = m
        self.set_Ki(math.pow(2,self.m))

    def get_Ki(self):
        return self.Ki

    def set_Ki(self, Ki):
        self.Ki = Ki
        self.set_samp_rate_tx(int(self.samp_rate_usrp_tx/self.Ki))

    def get_Kd(self):
        return self.Kd

    def set_Kd(self, Kd):
        self.Kd = Kd
        self.set_samp_rate(int(self.samp_rate_usrp_rx/self.Kd))

    def get_samp_rate_tx(self):
        return self.samp_rate_tx

    def set_samp_rate_tx(self, samp_rate_tx):
        self.samp_rate_tx = samp_rate_tx

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_run_stop(self):
        return self.run_stop

    def set_run_stop(self, run_stop):
        self.run_stop = run_stop
        self._run_stop_callback(self.run_stop)
        if self.run_stop: self.start()
        else: self.stop(); self.wait()

    def get_mapinverse(self):
        return self.mapinverse

    def set_mapinverse(self, mapinverse):
        self.mapinverse = mapinverse

    def get_mapdirect(self):
        return self.mapdirect

    def set_mapdirect(self, mapdirect):
        self.mapdirect = mapdirect

    def get_Vp(self):
        return self.Vp

    def set_Vp(self, Vp):
        self.Vp = Vp
        self.blocks_multiply_const_vxx_0_0_0.set_k((self.Vp/(self.NnivelesQ/2), ))
        self.b_quantizer_fb_0.set_Vmax(self.Vp)

    def get_Tmax_scope(self):
        return self.Tmax_scope

    def set_Tmax_scope(self, Tmax_scope):
        self.Tmax_scope = Tmax_scope

    def get_SymbTune(self):
        return self.SymbTune

    def set_SymbTune(self, SymbTune):
        self.SymbTune = SymbTune
        self.blocks_delay_0.set_dly(self.SymbTune)

    def get_Path_Loss_dB(self):
        return self.Path_Loss_dB

    def set_Path_Loss_dB(self, Path_Loss_dB):
        self.Path_Loss_dB = Path_Loss_dB
        self.b_Canal_simple_cc_0.set_Ch_Loss_dB(self.Path_Loss_dB)

    def get_NodB(self):
        return self.NodB

    def set_NodB(self, NodB):
        self.NodB = NodB
        self.b_Canal_simple_cc_0.set_Ch_NodB(self.NodB)

    def get_NnivelesQ(self):
        return self.NnivelesQ

    def set_NnivelesQ(self, NnivelesQ):
        self.NnivelesQ = NnivelesQ
        self.blocks_multiply_const_vxx_0_0_0.set_k((self.Vp/(self.NnivelesQ/2), ))
        self.b_quantizer_fb_0.set_NivelesQ(self.NnivelesQ)

    def get_Fc(self):
        return self.Fc

    def set_Fc(self, Fc):
        self.Fc = Fc

    def get_F_offset(self):
        return self.F_offset

    def set_F_offset(self, F_offset):
        self.F_offset = F_offset
        self.b_Canal_simple_cc_0.set_Foffset(self.F_offset)

    def get_Ch_Fluct_percent(self):
        return self.Ch_Fluct_percent

    def set_Ch_Fluct_percent(self, Ch_Fluct_percent):
        self.Ch_Fluct_percent = Ch_Fluct_percent
        self.b_Canal_simple_cc_0.set_Fluctuacion(self.Ch_Fluct_percent)

    def get_Ajuste_phi(self):
        return self.Ajuste_phi

    def set_Ajuste_phi(self, Ajuste_phi):
        self.Ajuste_phi = Ajuste_phi
        self.b_Canal_simple_cc_0.set_Ch_Phoffset(self.Ajuste_phi)


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
