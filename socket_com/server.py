# server
import socket
import pickle
import numpy as np

class xyz_data:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def print_data(self):
        print(self.x,self.y,self.z)

src_ip_addr = '127.0.0.1'
src_port = 50000
buffer_size = 1024

if __name__ == '__main__':
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((src_ip_addr,src_port))
    while True:
        msg, addr = server.recvfrom(buffer_size)
        # data = np.ndarray((3),np.int32,msg)
        data = pickle.loads(msg)
        print(msg)
        print(data)
        print(addr)
        data.print_data()

        
