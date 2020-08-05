import socket
import pickle
from time import time
import csv

def decodificar(pickle_cadena):
    start_time = time()
    cadena_bits = ''.join([ '1' if x else '0' for x in picke_cadena ])
    end_time = time()-start_time
    print (cadena_bits)



    archivo= open('tiempo_correccion.csv','a')

    with archivo:
        archivo.write(str(end_time) + "\n")
        print ('tiempo de ejecucion',end_time)
    

HOST = '127.0.0.1'  
PORT = 65432        


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break 
            conn.sendall(data)
            picke_cadena = pickle.loads(data)
            decodificar(picke_cadena)
            #print(picke_cadena)


