import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read, write
class FFT():
    def removeSmallest(self, d):
        smallest = 0
        for i in range(1, len(d)):
            if abs(d[i]) < abs(d[smallest]):
                smallest = i

        return np.delete(d, smallest)

    def compress_audio(self, file_name, num_remove=5000, num_blocks=1000, plot_change=False):
        data = read('audio/' + file_name + '.wav')
        datafft = np.fft.fft(data[1])

        results = []
        block_size = len(data[1])//num_blocks + 1
        i = 0
        while i  < len(data[1]):
            datafft = np.fft.fft(data[1][i:i+ block_size])
            for y in range(0, num_remove // num_blocks):
                datafft = self.removeSmallest(datafft)
            dataifft = np.fft.ifft(datafft).real
            results = np.append(results, dataifft)
            i = i + block_size

        write(file_name + '_enc.wav',data[0], np.asarray(results, dtype='int16'))

        if plot_change:

            plt.plot(range(0, len(data[1])), data[1])
            plt.plot(range(0,len(results)), results)
            plt.show()

FFT().compress_audio(file_name='ceremony', plot_change=False)
