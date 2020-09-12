from socket import socket, AF_INET, SOCK_DGRAM

class Machine():
    state = None

    __init__(self):
        pass

if __name__ == '__main__'
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(CONTROL_SERVER)
    while True:
        print ('waiting...')
        data, addr = sock.recvfrom(BUF_SIZE)
        print ('received : {}'.format(data.decode()))

        # buf = 'got it'
        # sock.sendto(buf.encode(), addr)