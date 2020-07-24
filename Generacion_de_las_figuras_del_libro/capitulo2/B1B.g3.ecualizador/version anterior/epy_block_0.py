"""
Embedded Python Blocks:

Each this file is saved, GRC will instantiate the first class it finds to get
ports and parameters of your block. The arguments to __init__  will be the
parameters. All of them are required to have default values!
"""
import numpy as np
from gnuradio import gr
class blk(gr.sync_block):

    def __init__(self,taps=5,gain=0.5,train=20):  # only default arguments here
        gr.sync_block.__init__(
            self,
            name='Ecualizador LMS Final',
            in_sig=[np.complex64,np.complex64],
            out_sig=[np.complex64]
        )
        #self.w=np.full((taps,1),0,dtype=np.complex64)
	self.w=np.zeros((taps,1),dtype=np.complex64)
	self.alpha=gain
	self.N=taps
	self.train=train
	self.count=0 

    def work(self, input_items, output_items,):
	
	x=input_items[0]
	d=input_items[1]
	if(self.count<=self.train):
		print 'Entrada entrenamiento'
		for i in range(self.N,len(x)):
			xt=x[(i-self.N):i]
			y=self.w.T.dot(xt)
			e=d[i-1]-self.w.T.dot(xt)
			e2=abs(e)
			print e2
			w1 = self.w.T + self.alpha*(e*(xt.conjugate()))
			self.w=w1.T
			#output_items[0][i]=y[0]	
	else:	
		for i in range(self.N,len(x)):
			print 'Entrada convolucion'
			xt=x[(i-self.N):i]
			y=self.w.T.dot(xt)
			#e=d[i-1]-y
			#self.w = self.w + self.alpha*(e*(xt.conjugate()))
			output_items[0][i]=y[0]
	print self.count
	self.count=self.count+1
        return len(output_items[0])
