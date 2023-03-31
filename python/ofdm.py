#Understanding Orthogonal Frequency Division Multiplexing (OFDM)
# March 2023
# Radio networks 4G and LTE

import numpy as np
import matplotlib.pyplot as plt

# Define the sinc function
def sinc(x):
    if x == 0:
        return 1
    else:
        return np.sin(x) / x

# Generate x values
t = np.linspace(-30, 30, 1000)

# Caluculate three sinc signals
x1 = np.array([sinc(xi- 6.7) for xi in t])
x2 = np.array([sinc(xi) for xi in t])
x3 = np.array([sinc(xi+ 6.7) for xi in t])


# Combine the signals using OFDM
N = 1024
X1 = np.fft.fft(x1, N)
X2 = np.fft.fft(x2, N)
X3 = np.fft.fft(x3, N)
X = np.zeros(3 * N, dtype=np.complex128)
X[::3] = X1
X[1::3] = X2
X[2::3] = X3
x = np.fft.ifft(X)

# Plot the OFDM chart
fig, ax = plt.subplots(figsize=(20, 8))
ax.plot(np.real(x), label='Combined signal')
ax.plot(np.real(x1), label='Signal 1')
ax.plot(np.real(x2), label='Signal 2')
ax.plot(np.real(x3), label='Signal 3')
ax.set_xlabel('Time (samples)')
ax.set_ylabel('Amplitude')
ax.set_title('OFDM Chart with 3 Signals')
ax.legend()

# Zoom on Orthogonal points
# ax.set_xlim([1000, 10])
# ax.set_ylim([-0.2, 0.3])

# Set grid
plt.grid(True, linewidth = 0.2)
plt.show()



