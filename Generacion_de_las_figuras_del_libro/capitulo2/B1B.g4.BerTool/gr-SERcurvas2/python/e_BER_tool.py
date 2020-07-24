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
import numpy as np
import random
import math
import numpy
from gnuradio import gr

class e_BER_tool(gr.sync_block):

    """
Calcula la curva de BER o SER dependiendo de que la entranda sean bits o simbolos. La curva
se actualiza cada N muestras y puede ser vista con un scope configurado para mostrar N muestras
o bien con un vector scope precedido por "Stream to Vector" para armar vector de N muestras.

Pero este bloque funciona solo acompanado del bloque e_Canal_BER y ambos estan hechos
de manera embebida, usando "python block". Por eso, no son bloque que aparecen en las librerias
instaladas en grc.


El principio de funcionamiento es asi:
* Este bloque del bloque e_Canal_BER y ambos estan hechos de manera embebida, usando 
  "python block". Por eso, no son bloque que aparecen en las librerias instaladas en grc.
* e_Canal_BER varia la SNR para que la senal que entra al canal se vea afectada por el ruido
* Por una de sus salidas, el canal indica a que punto de la SER corresponde la SNR actual
  Esa informacion es recibida por nuestro bloque por la entrada In0
* Nuestro bloque, recibe por los puertos In1 e In2, recibe los bits o simbolos transmitidos y los 
  recuperados respectivamente. Por In0 reconoce a que punto de la curva de SER corresponden esos
  valores, para recalcular la SER del punto dado
"""

    ############################################################################################
    ##  Constructor del bloque                                                                ##
    ############################################################################################

    def __init__(self, N=17):  
        gr.sync_block.__init__(
            self,
            name='e_BER_tool',
            in_sig=[np.int32, np.int8, np.int8],
            out_sig=[np.float32]
        )

        self.N=N # es el numero de puntos de la curva de SER a calcular
        self.errores = np.zeros(self.N)
        # count: cuenta el numero de muestras que ya han sido procesadas para cada punto de la BER
        self.count=0. 
        # SER: es la memoria de la ultima curva calculada
        self.SER=np.ones(self.N) 

    ############################################################################################
    ##  Lo de arriba es solo el constructor del bloque). Aqui comienza el verdadero cdigo     ##
    ############################################################################################

    def work(self, input_items, output_items):
        in0=input_items[1]
        in1=input_items[2]
        
        # L: es el tamano del vector de entrada. 
        L=len(in0) 
        
        # Barrido de los datos recibidos
        for i in range(0,L):
            k=input_items[0][i]
            self.count += np.sign(k)^1 

            # incremento el contador de errores
            self.errores[k] += int(in0[i]<>in1[i])

            # calculo la SER
            self.SER[k]=self.errores[k]/self.count
            output_items[0][i]=self.SER[k]

        return len(output_items[0])

