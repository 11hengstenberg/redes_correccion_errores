from bitarray import bitarray

def readn(fin, n):
    s = 0
    for ti in fin.read(n):
        s = s * 256 + ord(ti)
    return s
     
def fletcher(fin, k):
    if  k not in (16, 32, 64):
        raise ValueError("Valid choices of k are 16, 32 and 64")
    nbytes = k // 16
    mod = 2 ** (8 * nbytes) - 1
    s = s2 = 0
    t = readn(fin, nbytes)
    while t:
        s += t
        s2 += s 
        t = readn(fin, nbytes)
    return s % mod + (mod + 1) * (s2 % mod)