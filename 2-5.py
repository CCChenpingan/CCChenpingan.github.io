from IPython.core.display import publish_display_data
from thinkdsp import TriangleSignal
from matplotlib import pyplot
import matplotlib.pyplot as plt
def filter_spectrum(spectrum):
    """Divides the spectrum through by the fs.
    
    spectrum: Spectrum object
    """
    spectrum.hs[1:] /= spectrum.fs[1:]
    spectrum.hs[0] = 0

wave1 = TriangleSignal(freq=440).make_wave(duration=0.5)
spectrum = wave1.make_spectrum()
spectrum.plot(high=10000, color='gray')
filter_spectrum(spectrum)
spectrum.scale(440)
spectrum.plot(high=10000)
pyplot.show()