""" 
librerias
"""
from bitarray import bitarray
import socket
import pickle

"""
cadena a enviar
"""
def cadena():
    data=input("Ingrese la palabra. \n")
    cadena_segura(data)
    pass

def cadena_segura(data):
    #print ("cadena normal:",data,'\n')
    cadena_binaria = ''.join(format(ord(x), 'b') for x in data)
    #print ("cadena binaria:", cadena_binaria,'\n')
    cadena_bitarray = bitarray(cadena_binaria,endian='big')
    print (cadena_bitarray)
    pickle_cadena = pickle.dumps(cadena_bitarray)
    cadena_enviada(pickle_cadena)

def cadena_enviada(cadena_bitarray):
    HOST = '127.0.0.1'  # The server's hostname or IP address
    PORT = 65432        # The port used by the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        #print ('cadena normal', cadena_bitarray)
        s.sendall(cadena_bitarray)
        data = s.recv(1024)

    #print('Received', data)

    



if "__main__" == "__main__":
    cadena()