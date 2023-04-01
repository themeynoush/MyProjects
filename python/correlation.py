import numpy as np
import matplotlib.pyplot as plt

# Define the preamble
preamble = np.array([1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1])

# Define the three frame types
frame1 = np.array([0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1])
frame2 = np.array([0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1])
frame3 = np.array([0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1])

# Compute the correlation results for each frame
corr1 = np.correlate(frame1, preamble, mode='full')
corr2 = np.correlate(frame2, preamble, mode='full')
corr3 = np.correlate(frame3, preamble, mode='full')

# Plot the correlation results
plt.plot(corr1, label='Frame 1')
plt.plot(corr2, label='Frame 2')
plt.plot(corr3, label='Frame 3')
plt.legend()
plt.xlabel('Sample Index')
plt.ylabel('Correlation Value')
plt.show()

