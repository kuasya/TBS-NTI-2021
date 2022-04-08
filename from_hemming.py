a = str(input())
l = len(a)

i = 0
kontr_bit = 0
kontr_bits = []
sum = 0
error = ''
while 2**i <= l:
    kontr_bit = 2**i
    kontr_bits += [kontr_bit-1]

    for j in range(l):
        if len(bin(j+1)) >= i+1:

            if bin(j+1)[-(i+1)] != 'b':
                if int(bin(j+1)[-(i+1)]) == 1:
                    sum += int(a[j])

    # if int(a[kontr_bit-1]) == sum % 2:
    if sum % 2 == 0:
        error = '0' + error
    else:
        error = '1' + error

    sum = 0
    i += 1
print(kontr_bits, kontr_bit)
bit_error = 0
for j in range(len(error)):
    bit_error += int(error[-j-1])*2**j

if bit_error > l:
    print('error not one:(')

new_bit = 0
if bit_error != 0 and bit_error-1 < l:
    print(bit_error, l)
    new_bit = (int(a[bit_error-1]) + 1) % 2

new_a = ''
for j in range(l):
    if j not in kontr_bits:
        if j != bit_error - 1:
            new_a += a[j]
        else:
            new_a += str(new_bit)

print(a)
print('error in', bit_error)
print(new_a)
