# Considering more than 1 frame transmitts at the same time 
# to observe collisio in different cases 

# define frame type 2 and 3
frame_type_2 = list(map(convert, '0000010001101'))
frame_type_3 = list(map(convert, '0001101011111'))

# define corr_result_2 and corr_result_3 based on frame type 2 and 3
corr_result_2 = [0] * (len(frame_type_2) + len(preamble) - 1)
for i in range(len(frame_type_2)):
    for j in range(len(preamble)):
        corr_result_2[i+j] += frame_type_2[i] * preamble[j]

corr_result_3 = [0] * (len(frame_type_3) + len(preamble) - 1)
for i in range(len(frame_type_3)):
    for j in range(len(preamble)):
        corr_result_3[i+j] += frame_type_3[i] * preamble[j]


# plot frame type 2 and 3 in the same graph
plt.plot(corr_result)
#plt.plot(corr_result_2)
plt.plot(corr_result_3)
plt.xlabel('Shift')
plt.ylabel('Correlation Result')
plt.title('Frame 1 and 3 Transmitting at the same time')

plt.show()


