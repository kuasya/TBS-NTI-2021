#!/usr/bin/python3
def encoder(filein, fileout):

    blocksize = 4
    while True:
        bytestring = filein.read(blocksize)
        if not bytestring:
            break
        a = ''
        # s = ''
        for j in range(len(bytestring)):

            byte = bytestring[j]
            # s += str(byte)
            for i in range(8):
                a += str((byte >> i) & 1)

        l_a = len(a)

        kontr_bit = 0
        # kontr_bits = []

        sum = 0
        kontr_values = {}
        kontr_bits = []
        i = 0
        while 2 ** i <= l_a:
            kontr_bit = 2 ** i
            kontr_bits += [kontr_bit]
            i += 1

        b = ''
        j = 0
        parameter = 0
        l = l_a + len(kontr_bits)

        while j <= l:
            if j + 1 in kontr_bits:
                b += '0'
                parameter += 1

            else:
                if j - parameter < l_a:
                    b += a[j - parameter]

            j += 1

        i = 0
        parameter = 0
        while i <= l:
            if i + 1 in kontr_bits:
                kontr_values[i + 1] = ''

                for j in range(l):

                    if len(bin(j + 1)) >= parameter + 1:
                        if bin(j + 1)[-(parameter + 1)] != 'b':
                            if int(bin(j + 1)[-(parameter + 1)]) == 1:
                                sum += int(b[j])
                parameter += 1

                kontr_values[i + 1] += str(sum % 2)
                sum = 0

            i += 1

        new_b = ''
        j = 0

        while j <= l:
            if j + 1 in kontr_values:
                new_b += kontr_values[j + 1]

            else:
                if j < l:
                    new_b += b[j]

            j += 1

        fileout.write(new_b.encode('utf-8'))

#
# with open('result1.dat', 'rb') as filein:
#     with open('file_cod', 'wb') as fileout:
#         encoder(filein, fileout)
