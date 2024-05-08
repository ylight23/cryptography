
def binarytodecimal(binary):
    string = int(binary,2)
    return string
ct='011001101110101011000100110110101101001011101000110011001101100011000010110011101110010011010010110011101101000011101000110111001101111011101110100110101010011010001010100001101111011011010010110101000110000011101010101111101101011011011100011000001110111010111110110100000110000011101110101111101110100001100000101111101110011011010000110101001100110011101000101111101101101001100110111110101100010011100100111010101111010011110100111101001111010011110100111100'
ct1='0000000000000000001000000101010001101000011001010010000001100110011011000110000101100111001000000110100101110011001000000100011001001100010000010100011101111011011010010111010000110101010111110011001101101110001100000111010100111001011010000101111101101010010101010011010101010100010111110111010001001111010111110111001101001000001100010110011001110100010111110100110100110011011111010010000000000000'
print("LENGTH: ", len(ct1))

str_data=' '
for i in range(0, len(ct1), 8):
    temp_data= ct1[i:i+7]
    decimal_data = binarytodecimal(temp_data)
    str_data = str_data + chr(decimal_data)

print("TEXT :", str_data)
print("FLAG: MSEC{ij0u_kn0w_h0w_t0_shjft_m3}")