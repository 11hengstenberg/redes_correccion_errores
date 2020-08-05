import socket
import pickle

def decodificar(pickle_cadena):
    cadena_bits = ''.join([ '1' if x else '0' for x in picke_cadena ])
    print (cadena_bits)

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

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


