""" 
librerias
"""
from bitarray import bitarray
import socket
import pickle
from random import randint as rm

ruido_bit = 100


def cadena():
    data=input("Ingrese la palabra. \n")
    cadena_segura(data)
    pass

def cadena_segura(data):
    #print ("cadena normal:",data,'\n')
    cadena_binaria = ''.join(format(ord(x), 'b') for x in data)
    #print ("cadena binaria:", cadena_binaria,'\n')
    cadena_bitarray = bitarray(cadena_binaria,endian='big')
    cadena_binaria = ruido(cadena_bitarray)
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

def ruido (cadena_binaria):
    ruido = round(len(cadena_binaria)/ruido_bit)
    for i in range (ruido if ruido else 1):
        posicion=rm(0, len (cadena_binaria) -1)
        print('cadema sin ruido:', cadena_binaria)
        cadena_binaria[posicion]= not cadena_binaria[posicion]
        print ('cadena con ruido:', cadena_binaria)
    



if "__main__" == "__main__":
    cadena()