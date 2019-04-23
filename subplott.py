import scipy.io.wavfile as wav
import numpy as np
from matplotlib import pyplot as plt
fs1,data8k=wav.read('oohafast.wav')
print(fs1,len(data8k))
print(data8k) #values of samples
t1=np.arange(0,len(data8k)/fs1,1.0/fs1) #time scale
plt.subplot(2,1,1)
plt.plot(data8k)
fs2,data81k=wav.read('oohaslow.wav')
print(fs2,len(data81k)
t2=np.arange(0,len(data81k)/fs2,1.0/fs2) #time scale
plt.subplot(2,1,2)
plt.plot(data81k)
plt.show()
