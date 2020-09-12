import socket
from socket import socket, AF_INET, SOCK_DGRAM

CONTROL_SERVER = ('localhost', 8001)
PARSER_SERVER = ('localhost', 8002)
STT_SERVER = ('localhost', 8003)
TTS_SERVER = ('localhost', 8004)
BOT_SERVER = ('localhost', 8005)

BUF_SIZE = 4096

def send_command(addr, command):
    with socket(AF_INET, SOCK_DGRAM) as sock:
        sock.sendto(command.encode(), addr)

def send_request(addr, text):
    with socket(AF_INET, SOCK_DGRAM) as sock:
        sock.sendto(text.encode(), addr)
        recvdata, recvaddr = sock.recvfrom(BUF_SIZE)
    return recvdata.decode()

if __name__ == '__main__':
    pass