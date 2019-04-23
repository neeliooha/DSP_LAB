import scipy.io.wavfile as wav
import numpy as np
from matplotlib import pyplot as plt
fs,data8k=wav.read('ooha.wav')
print(fs,len(data8k))
print(data8k) #values of samples
t=np.arange(0,len(data8k)/fs,1.0/fs) #time scale
plt.plot(data8k)
plt.show()
wav.write('oohaslow.wav',fs*0.5,data8k)
#wav.write('oohafast.wav',fs*2,data8k)