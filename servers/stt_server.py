from socket import AF_INET, SOCK_DGRAM, socket
from servers import STT_SERVER, BUF_SIZE
import speech_recognition as sr

recognizer = sr.Recognizer()
microphone = sr.Microphone()

def speech_to_text():
    text = None
    while text is None:
        try:  
            with microphone as source:
                audio = recognizer.listen(source, phrase_time_limit=10) 
            text = recognizer.recognize_google(audio, language='cmn-Hant-TW')
        except sr.UnknownValueError:  
            print("Could not understand audio")  
        except sr.RequestError as e:  
            print("Error; {0}".format(e))  
        except Exception as e:
            print(e)
    return text

if __name__ == '__main__':
    with microphone as source :
        print('Wait...')
        recognizer.adjust_for_ambient_noise(source, duration=3)
        print('Ready')
       
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(STT_SERVER)
    while True:
        print('Waiting...')
        recvdata, addr = sock.recvfrom(BUF_SIZE)

        print('Say something')
        text = speech_to_text()
            

        print('Sent : {}'.format(text))
        sock.sendto(text.encode(), addr)

