""" 
librerias
"""
from bitarray import bitarray

"""
cadena a enviar
"""
def cadena():
    data=input("Ingrese la palabra.")
    cadena_segura(data)

def cadena_segura(data):
    print ("cadena normal:",data)
    cadena_binaria = ''.join(format(ord(i), 'b') for i in data)
    print ("cadena binaria:", cadena_binaria) 





if "__main__" == "__main__":
    cadena()