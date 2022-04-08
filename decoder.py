#!/usr/bin/python3
def decoder(filein, fileout, filelog):

    blocksize = 38
    while True:

        s = filein.read(blocksize)

        if not s:
            break
        a = ''
        a = s.decode('utf-8')
        l = len(a)

        i = 0
        kontr_bit = 0
        kontr_bits = []
        sum = 0
        error = ''
        while 2 ** i <= l:
            kontr_bit = 2 ** i
            kontr_bits += [kontr_bit - 1]

            for j in range(l):
                if len(bin(j + 1)) >= i + 1:

                    if bin(j + 1)[-(i + 1)] != 'b':
                        if int(bin(j + 1)[-(i + 1)]) == 1:
                            sum += int(a[j])

            if sum % 2 == 0:
                error += '0'
            else:
                error += '1'

            sum = 0
            i += 1

        bit_error = 0
        for j in range(len(error)):
            bit_error += int(error[-j - 1]) * 2 ** j

        new_bit = 0
        if bit_error != 0 and bit_error - 1 < l:

            new_bit = (int(a[bit_error - 1]) + 1) % 2

        new_a = ''
        for j in range(l):
            if j not in kontr_bits:
                if j != bit_error - 1:
                    new_a += a[j]
                else:
                    new_a += str(new_bit)
        i = 0
        while i < len(new_a):

            if i == 0:
                y = (int('0b' + new_a[i + 7:i:-1] + new_a[0], 2))
                # print(new_a[i + 7:i:-1] + new_a[0], y, end=' ')
            else:
                y = (int('0b'+new_a[i+7:i-1:-1], 2))
                # print(new_a[i+7:i-1:-1], y, end=' ')

            fileout.write(chr(y).encode())
            i += 8
            # print(chr(y).encode())

#
# with open('file_cod', 'rb') as filein:
#     with open('file_decod_itog', 'wb') as fileout:
#         decoder(filein, fileout, fileout)
