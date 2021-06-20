from thinkdsp import TriangleSignal
from thinkdsp import decorate
from IPython.display import Audio
from thinkdsp import SquareSignal
from thinkdsp import SawtoothSignal
from matplotlib import pyplot

signal1=TriangleSignal(200)
duration1=signal1.period*3
segment1=signal1.make_wave(duration1,framerate=10000)
segment1.plot()
wave1=signal1.make_wave(duration=0.5,framerate=10000)
wave1.apodize()

wave1.make_audio()
spectrum1=wave1.make_spectrum()
pyplot.subplot(141)
pyplot.xlabel('triangle')
spectrum1.plot()



signal2=SquareSignal(200)  
duration2=signal2.period*3
segment2=signal2.make_wave(duration2,framerate=10000)
segment2.plot()
wave2=signal2.make_wave(duration=0.5,framerate=10000)
wave2.apodize()

wave2.make_audio()
spectrum2=wave2.make_spectrum()
pyplot.subplot(142)
pyplot.xlabel('square')
spectrum2.plot()



signal3=SawtoothSignal(200)
duration3=signal3.period*3
segment3=signal3.make_wave(duration3,framerate=10000)
segment3.plot()
wave3=signal3.make_wave(duration=0.5,framerate=10000)
wave3.apodize()

wave3.make_audio()
spectrum3=wave3.make_spectrum()
pyplot.subplot(143)
pyplot.xlabel('sawtooth')
spectrum3.plot()


pyplot.show()