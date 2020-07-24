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
from SERcurvas2 import e_BER_tool
from SERcurvas2 import e_canal_BER
from gnuradio import digital
from gnuradio import blocks
from gnuradio import gr

class e_canal_SER(gr.hier_block2):
    """
    docstring for block e_canal_SER
    """
    def __init__(self, N=8, EbN0min=0, EbN0max=16,B=100,Rb=1):
        gr.hier_block2.__init__(self,
            "e_canal_SER",
	     gr.io_signature((2),(2),(gr.sizeof_char)),
             gr.io_signature((1),(1),gr.sizeof_float))
            #gr.io_signature(1,1,gr.sizeof_gr_complex),  # Input signature
	    #gr.io_signature(2,2,gr.sizeof_char),  # Input signature
	    #gr.io_signature(1,1,gr.sizeof_float),
            #gr.io_signature(1,1,gr.sizeof_gr_complex)) # Output signature

            # Define blocks and connect them
	B1=e_BER_tool(N=17)
	B2=e_canal_BER(N=8, EbN0min=0, EbN0max=16,B=100,Rb=1)
	#self.B3= digital.chunks_to_symbols_bc((const), 1)
	#self.B4 = blocks.float_to_complex(1)
	#self.null= blocks.null_source(gr.sizeof_float*1)
	self.connect((self,0),(B2,0))
	#self.connect((self,0),(self.B3,0))
	self.connect((self,1),(B1,1))
	self.connect((self,2),(B1,2))
	self.connect((B2,0),(self,0))
	self.connect((B2,1),(B1,0))
	self.connect((B1,0),(self,1))
	#self.connect((self.null,0),(self.B4,1))
	#self.connect((self.B4,0),(self,1))

