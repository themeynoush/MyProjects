# Studying correlation computation between a FT and Received_Flow in Sigfox Network
# Author: Meynoush - github: @themeynoush


# create a function that converts 1 to -1 and 0 to 1
def convert(num):
    if num == '1':
        return -1
    else:
        return 1
    
# convert the Received_Flow and frame type to a list of 1s and -1s
frame_type_1 = list(map(convert, '0000001101011'))
frame_type_2 = list(map(convert, '0000010001101'))
frame_type_3 = list(map(convert, '0001101011111'))

# 8 bytes     0b0 0000001101011   0x006B   first
# 9 bytes     0b0 0000010001101  0x008D  first
# 12 bytes  0b0 0001101011111   0x035F   first

Received_Flow = list(map(convert, '10101010101010101010001101011111000000')) #Premable+ FT + 000000 is the payload
# Received_Flow_1 =  10101010101010101010000001101011000000
# Received_Flow_2 =  10101010101010101010000010001101000000
# Received_Flow_3 =  10101010101010101010001101011111000000

corr_result_1 = [0] * (len(Received_Flow) + len(frame_type_1) - 1)
for i in range(len(Received_Flow)):
    for j in range(min(len(frame_type_1), len(Received_Flow) - i)):
        corr_result_1[i] += frame_type_1[j] * Received_Flow[i+j]

# find the index of the peak correlation 0x006B
peak_index = corr_result_1.index(max(corr_result_1))
# find the index of the peak correlation 0x008D
peak_index = corr_result_2.index(max(corr_result_2))
# find the index of the peak correlation 0x035D
peak_index = corr_result_3.index(max(corr_result_3))

# plot the correlation result
import matplotlib.pyplot as plt
import numpy as np

# repeat the correlation between the Received_Flow and each frame type
corr_result_2 = [0] * (len(Received_Flow) + len(frame_type_2) - 1)
for i in range(len(Received_Flow)):
    for j in range(min(len(frame_type_2), len(Received_Flow) - i)):
        corr_result_2[i] += frame_type_2[j] * Received_Flow[i+j]

corr_result_3 = [0] * (len(Received_Flow) + len(frame_type_3) - 1)
for i in range(len(Received_Flow)):
    for j in range(min(len(frame_type_3), len(Received_Flow) - i)):
        corr_result_3[i] += frame_type_3[j] * Received_Flow[i+j]

# plot all the correlation results in one figure for comparison
plt.figure(figsize=(10, 5))
plt.plot(corr_result_1, label='0x006B', color='red')
plt.plot(corr_result_2, label='0x008D', color='green')
plt.plot(corr_result_3, label='0x035D', color='blue')
plt.xlabel('Shift')
plt.ylabel('Correlation Result')
plt.title('Correlation of the Third Received Flow and all Frame Types')
plt.grid()
plt.legend()
plt.show()  

# print the peak correlation
print(f'The peak correlation for 0x006B: {max(corr_result_1)}')
print(f'The peak correlation for 0x008D: {max(corr_result_2)}')
print(f'The peak correlation for 0x035D: {max(corr_result_3)}\n')

# # print the correlation result table
# print('Bit\tFrame Type\tReceived_Flow\tResult')
# for i in range(len(frame_type_1)):
#     for j in range(len(Received_Flow)):
#         result = frame_type_1[i] * Received_Flow[j]
#         print(f'{i+j}\t{frame_type_1[i]}\t\t{Received_Flow[j]}\t\t{result}')


