from time import time
  

  
def posRedundantBits(data, r): 

    j = 0
    k = 1
    m = len(data) 
    res = '' 

    for i in range(1, m + r+1): 
        if(i == 2**j): 
            res = res + '0'
            j += 1
        else: 
            res = res + data[-1 * k] 
            k += 1

    return res[::-1] 
  
  
def calcParityBits(arr, r): 
    n = len(arr) 

    for i in range(r): 
        val = 0
        for j in range(1, n + 1): 
 
            if(j & (2**i) == (2**i)): 
                val = val ^ int(arr[-1 * j]) 

        arr = arr[:n-(2**i)] + str(val) + arr[n-(2**i)+1:] 
    return arr 

def calcRedundantBits(data): 

    for i in range(data): 
        if(2**i >= data + i + 1): 
            return i 
  
  
def detectError(arr, nr): 
    n = len(arr) 
    res = 0
  

    for i in range(nr): 
        val = 0
        for j in range(1, n + 1): 
            if(j & (2**i) == (2**i)): 
                val = val ^ int(arr[-1 * j]) 
  
  
        res = res + val*(10**i) 
  

    return int(str(res), 2) 
  
  

def hamming (cadena_binaria):
    start_time = time()
    m = len(cadena_binaria) 
    r = calcRedundantBits(m) 
    arr = posRedundantBits(cadena_binaria, r) 
    arr = calcParityBits(arr, r) 

    end_time = time()-start_time

    archivo= open('tiempo_hammin.csv','a')

    with archivo:
        archivo.write(str(end_time) + "\n")

    arr = '11101110'
    correction = detectError(arr, r) 
    print ('hamming completo')
