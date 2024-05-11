base = {}
for i in range(32):
    if i < 10:
        base[str(i)] = '0' * (5-len(bin(i)[2:])) + bin(i)[2:]
    elif i < 17:
        base[chr(i+88)] = '0' * (5-len(bin(i)[2:])) + bin(i)[2:]
    elif i < 19:
        base[chr(i+89)] = '0' * (5-len(bin(i)[2:])) + bin(i)[2:]
    elif i < 21:
        base[chr(i+90)] = '0' * (5-len(bin(i)[2:])) + bin(i)[2:]
    else:
        base[chr(i+91)] = '0' * (5-len(bin(i)[2:])) + bin(i)[2:]

def hashtoarrayindex(hash):
    bi = ''
    for c in hash:
        bi += base[c]
    odd = '0b' # row
    even = '0b' # column
    for i in range(len(bi)//2):
        odd += bi[2*i+1]
        even += bi[2*i]
    return (int(odd, 2)-733067, int(even, 2)-900017) # based on pohang area
