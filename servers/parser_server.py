from socket import AF_INET, SOCK_DGRAM, socket
from servers import PARSER_SERVER, BUF_SIZE
import jieba

if __name__ == '__main__':
    # specify jieba dictionary
    jieba.set_dictionary('res/dict.txt.big')
    jieba.initialize()
    
    # Custom keywords
    with open('res/keyword') as f:
        for word in f.read().split('\n'):
            jieba.add_word(word)

    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(PARSER_SERVER)
    while True:
        # Receive & decode
        print('Waiting...')
        recvdata addr = sock.recvfrom(BUF_SIZE)
        text = recvdata.decode()
        print('Received : {}'.format(text))
        
        # Process
        segged = jieba.lcut(text)
        joined = ' '.join(segged)

        # Send back result
        print('Sent : {}'.format(joined))
        senddata = joined.encode()
        sock.sendto(senddata, addr)