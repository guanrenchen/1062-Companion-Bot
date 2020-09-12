from socket import AF_INET, SOCK_DGRAM, socket
from servers import TTS_SERVER, BUF_SIZE
from gtts import gTTS
import os

def text_to_speech(text):
    tts = gTTS(text=text, lang='zh-tw')
    tts.save('res/tts')
    _ = os.system("mplayer res/tts > /dev/null")

if __name__ == '__main__':
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(TTS_SERVER)
    while True:
        print('Waiting...')
        recvdata, addr = sock.recvfrom(BUF_SIZE)

        text = recvdata.decode()
        text_to_speech(text)

        print('Done')
        sock.sendto(b'', addr)
