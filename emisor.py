""" 
librerias
"""
from bitarray import bitarray
import socket

"""
cadena a enviar
"""
def cadena():
    data=input("Ingrese la palabra. \n")
    cadena_segura(data)
    pass

def cadena_segura(data):
    #print ("cadena normal:",data,'\n')
    cadena_binaria = ''.join(format(ord(i), 'b') for i in data)
    #print ("cadena binaria:", cadena_binaria,'\n')
    cadena_bitarray = bitarray(cadena_binaria,endian='big')
    #print ('cadena bitarray', cadena_bitarray,'\n') 
    #print ('cadena binaria', cadena_bitarray.decode())
    cadena_enviada(cadena_bitarray)


def cadena_enviada(cadena_bitarray):
    HOST = '127.0.0.1'  # The server's hostname or IP address
    PORT = 65432        # The port used by the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print ('cadena normal', cadena_bitarray)
        s.sendall(b'porquenofunciona')
        data = s.recv(1024)

    print('Received', repr(data))

    



if "__main__" == "__main__":
    cadena()