# Studying correlation computation between a FT and Preamble in Sigfox Network
# Author: Meynoush - github: @themeynoush


# create a function that converts 1 to -1 and 0 to 1
def convert(num):
    if num == '1':
        return -1
    else:
        return 1
    
# convert the preamble and frame type to a list of 1s and -1s
frame_type = list(map(convert, '0b0001101011111'))
# frame_type_2 = 0b0000010001101
# frame_type_3 = 0b0001101011111
preamble = list(map(convert, '1010101010101010101'))

# correlate the preamble with the frame type
corr_result = [0] * (len(frame_type) + len(preamble) - 1)
for i in range(len(frame_type)):
    for j in range(len(preamble)):
        corr_result[i+j] += frame_type[i] * preamble[j]

# find the index of the peak correlation
peak_index = corr_result.index(max(corr_result))

# plot the correlation result
import matplotlib.pyplot as plt
import numpy as np

plt.plot(corr_result)
plt.xlabel('Shift')
plt.ylabel('Correlation Result')
plt.title('Correlation of the 3rd Frame Type and Preamble')
plt.annotate('Peak correlation', xy=(peak_index, max(corr_result)), xytext=(peak_index, max(corr_result)+1),
                arrowprops=dict(facecolor='red', shrink=0.05))
plt.show()

# print the peak correlation
print(f'The peak correlation value is: {max(corr_result)} at shift number: {peak_index}')


# print the correlation result table
print('Bit\tFrame Type\tPreamble\tResult')
for i in range(len(frame_type)):
    for j in range(len(preamble)):
        result = frame_type[i] * preamble[j]
        print(f'{i+j}\t{frame_type[i]}\t\t{preamble[j]}\t\t{result}')



