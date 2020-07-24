import numpy as np
import pdb


class SimPLL(object):
    def __init__(self, lf_bandwidth):
        self.phase_out = 0.0
        self.freq_out = 0.0
        self.vco = np.exp(1j*self.phase_out)
        self.phase_difference = 0.0
        self.bw = lf_bandwidth
        self.beta = np.sqrt(lf_bandwidth)
        self.memory = [self.vco, 0]
        self.timming = 0

    def update_phase_estimate(self):
        self.vco = np.exp(1j*self.phase_out)

    def update_phase_difference(self, in_sig):
        self.phase_difference = np.angle(in_sig*np.conj(self.vco))

    def step(self, in_sig):
        # Takes an instantaneous sample of a signal and updates the PLL's inner state
        self.update_phase_difference(in_sig)
        self.freq_out += self.bw * self.phase_difference
        self.phase_out += self.beta * self.phase_difference + self.freq_out
        self.update_phase_estimate()
        self.update_sample()

    def update_sample(self):
    	self.memory[1] = self.vco
    	if self.memory[0] < self.memory[1]:
    		self.timming = 1
    	elif self.memory[0] > self.memory[1]:
    		self.timming = -1
    	else:
    		self.timming = 0
    	self.memory[0] = self.memory[1]


"""
    	elif self.memory[self.count - 1] > self.memory[self.count]:

    		self.timming = -1
"""


def main():
    import matplotlib.pyplot as plt
    pll = SimPLL(1)
    num_samples = 10000
    phi = 3
    frequency_offset = -0.2
    ref = []
    out = []
    diff = []
    timming = []

    for i in range(0, num_samples - 1):
        in_sig = np.exp(1j*phi)
        phi += frequency_offset
        pll.step(in_sig)
        ref.append(in_sig)
        out.append(pll.vco)
        timming.append(pll.timming)
        diff.append(pll.phase_difference)

    #print timming
    plt.stem(timming[9700:10000])
    plt.plot(ref[9700:10000])
    plt.plot(out[9700:10000])
    plt.plot(diff[9700:10000])
    plt.show()



main()
