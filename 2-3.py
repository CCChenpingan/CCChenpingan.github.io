from thinkdsp import SquareSignal
from matplotlib import pyplot

signal2=SquareSignal(1100)  
duration2=signal2.period*3
segment2=signal2.make_wave(duration2,framerate=10000)
wave2=signal2.make_wave(duration=0.5,framerate=10000)
wave2.apodize()
spectrum2=wave2.make_spectrum()
pyplot.xlabel('square disorder')
spectrum2.plot()
pyplot.show()