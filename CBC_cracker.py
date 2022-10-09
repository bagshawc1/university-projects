k2 = {}
def key_constructor(iv, plaintext, ciphertext):
    split_plain = [*plaintext]
    split_ascii = [ord(x) for x in split_plain]
    for i in range(len(split_ascii)):
        if ciphertext[i-1]:
            iv = ciphertext[i-1]
        key = iv ^ split_ascii[i]
        k2[ciphertext[i]] = key


def cbc_decoder(iv, ciphertext):
    output = list()
    for i in range(len(ciphertext)):
        if ciphertext[i-1]:
            iv = ciphertext[i-1]
        ascii_code = iv ^ k2[ciphertext[i]]
        output.append(chr(ascii_code))
    return ''.join(output)


key_constructor(85, 'bank', [97, 127, 78, 47])
key_constructor(85, 'dress', [7, 135, 95, 254, 116])
key_constructor(85, 'paint', [47, 115, 15, 55, 67])
key_constructor(85, 'salt', [85, 201, 22, 186])
print(cbc_decoder(85, [85, 254, 116, 127, 15, 186]))