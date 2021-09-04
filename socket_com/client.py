
# client 
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

dst_ip_addr = '127.0.0.1'
dst_port = 50000

if __name__ == '__main__':
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = xyz_data(1, 2, 3)
    msg = pickle.dumps(data)
    # data = np.ones(3,np.int32)
    # msg = data.tobytes()
    server.sendto(msg, (dst_ip_addr, dst_port))