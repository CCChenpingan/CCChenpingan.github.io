from thinkdsp import TriangleSignal
from thinkdsp import decorate
import matplotlib.pyplot as plt 
triangle = TriangleSignal().make_wave(duration=0.01)
spectrum = triangle.make_spectrum()
print(spectrum.hs[0])