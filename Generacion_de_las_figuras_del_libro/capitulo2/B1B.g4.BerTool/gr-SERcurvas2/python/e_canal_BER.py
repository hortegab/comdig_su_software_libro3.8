#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2018 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy
import numpy as np
import random
import math
from gnuradio import gr

class e_canal_BER(gr.sync_block):
    """
Es un canal AWGN (Additive Whaite Gaussian Noise, en banda base). 
Solo pide el Eb/N0 y  partir de la Rata de transmisión de bits y del ancho de banda de la señal
 Internamente mide la potencia de la senal entrante
despejar la potencia del ruido que cumpla con la SNR 
SNR-Db: es la relacion senal a ruido en dB
    """
    def __init__(self, N=8, EsN0min=0, EsN0max=16,B=100,Rs=1):  # only default arguments here
        gr.sync_block.__init__(
            self,
            name='e_canal_BER',
            in_sig=[np.complex64],
            out_sig=[np.complex64, np.int32]
        )
        self.N = N
	self.B=B
	self.Rs=Rs

	self.EsN0dB=np.linspace(EsN0min,EsN0max,N)
        self.k=0  # recuerda cual es el valor de SNR actual
     
    def work(self, input_items, output_items):
        L=len(input_items[0])
	Rs=self.Rs
	B1=self.B
        # calculo de la varianza (potencia promedio normalizada) de la senal entrante
        Pin=np.mean(np.absolute(input_items[0])**2)
        ###############################################################  
        ##  Esta es donde esta el mehoyo y se puede optimizar mejor
        ###############################################################
        for i in range(0,L): 
            output_items[0][i] = input_items[0][i]+noise_c(self.EsN0dB[self.k], Pin,Rs,B1)
            output_items[1][i] = self.k
            if self.k < self.N-1:
                self.k += 1
            else:
                self.k=0
        return len(output_items[0])

#############################################################################
## calculo de una muestra de ruido
## Rb: Rata de bit
## B: 
## N: es el numero de elementos en el vector
## P_s: es la varianza (potencia promedio) de la senal entrante. 
## SNR_dB: es la relacion senal a ruido en dB del ruido respecto a P_signal
#############################################################################

def noise_c(EsN0_dB,P_s,Rs,B):
    EsN0=pow(10.,EsN0_dB/10.) 
    SNR=EsN0*Rs/B
    P_n = P_s/SNR  # la potencia del ruido
    sigma = math.sqrt(P_n) # es porque la funcion random.normal() pide la desviacion standard
    n=np.random.normal(0.,sigma)+np.random.normal(0.,sigma)*1.j
    
    return n
