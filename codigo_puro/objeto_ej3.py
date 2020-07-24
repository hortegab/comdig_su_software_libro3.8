#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Lo de arriba es para que los IDE conozcan en que esta escrito este codigo 
###########################################################
# Puedes encontrar este codigo como objeto_ej3.py en:    ##
# https://sites.google.com/saber.uis.edu.co/comdig/sw    ##
###########################################################
###########################################################
###           LA CLASE DE UN BLOQUE NUESTRO             ###
###########################################################
import numpy as np
from gnuradio import gr

# Se recomienda que el nombre de la clase finalice con una o dos letras especiales:
# nombre_ff: cuando en el bloque sus entradas y salidas son senales reales y de tipo flotante
# nombre_f: el bloque solo tiene una entrada o una salida y es una senal real de tipo flotante
# En vez de "f" puden usarse: c (compleja),  i (entero), b (binario), c (entero corto, de 8 bits)


class e_add_cc(gr.sync_block):  
    """Aqui debes explicar como funciona el bloque, los parametros usados.
    En este caso particular estamos definiendo nuestra propia version del bloque add"""

    # Dentro de la funcion __init__(), deben definirse los parametros de configuracion del bloque.
    # A cada parametro se le da un valor por defecto, por ejemplo  def __init__(self, amp=1.0):
    def __init__(self):
        # En la siguiente funcion debes recordar que usaras:
        # sync: cuando tu bloque sea un bloque de tipo sincrono (por cada muestra entrante habra una saliente)
        # decim: cuando es un bloque decimador (por cada muestra saliente hay un numero entero de muestras entrantes)
        # interp: cuando es un bloque interpolador (por cada muestra entrante hay un numero entero de muestras salientes)
        # basic: cuando no hay relacion entre el numero de muestras entrantes y las salientes
        # mas en: https://wiki.gnuradio.org/index.php/Guided_Tutorial_GNU_Radio_in_Python#3.3.1._Choosing_a_Block_Type
        gr.sync_block.__init__(
            self,
            # Lo siguiente es para definir el nombre que tendra nuestro bloque para usuarios de GRC
            name='e_dd_ff', 
            # A continuacion se definen los tipos de senales de entrada. Veamos algunos ejemplos:
            # [np.complex64]: cuando se tiene una entrada y es compleja
            # [np.float32]: cuando se tiene una entrada y es de tipo flotante
            # [np.float32, np.complex64]: cuando hay dos entradas, una de tipo flotante otra compleja
            # otros casos: int8 o byte (entero de 8 bits, que en C++ se conoce como char)
            # No hemos explorado mas casos, pero si que no es tan sencillo. Uno supondria que otros casos posibles son:
            # int16 (en C++ se conoce como short), int32, int64. Los dos primeros funcionan, pero int64 no.
            in_sig=[np.complex64,np.complex64],

            # aqui aplica lo mismo explicado anteriormente
            out_sig=[np.complex64]
        )
        # abajo se puede escribir lo que se le antoje al programador, por ejemplo:
        # self.coef=1.0: define la variable global acum y le asigna el valor cero
        # self significa que es una variable global, que se puede involcar directamente desde otras funciones
        # se pueden definir las funcines que se deseen
        # En todo caso, lo más usual es que esas variables y funciones sean usadas en work() 
        self.coef = 1.0

    # La funcion work() siempre debe estar presente en un bloque. Es alli donde estara la logica del bloque 
    
    def work(self, input_items, output_items):
        in0 = input_items[0]
        in1 = input_items[1]
        out0 = output_items[0]
        out0[:]=(in0+in1)*self.coef
        return len(out0)
        






        
