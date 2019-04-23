import scipy.io.wavfile as wav
import numpy as np
from matplotlib import pyplot as plt
fs,data8k=wav.read('ooha.wav')
print(fs,len(data8k))
print(data8k)
plt.plot(data8k)
plt.show()