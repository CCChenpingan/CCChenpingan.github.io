import numpy as np
from IPython.core.display import publish_display_data
from thinkdsp import TriangleSignal
from matplotlib import pyplot
import matplotlib.pyplot as plt

triangle = TriangleSignal(440).make_wave(duration=0.01)
spectrum = triangle.make_spectrum()
spectrum.hs[0] = 100
triangle.plot(color='gray')
spectrum.make_wave().plot()
pyplot.show()




