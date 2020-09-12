# -*- coding: utf-8 -*-

import speech_recognition as sr

from gtts import gTTS
import os

recognizer = sr.Recognizer()
microphone = sr.Microphone()

def speech_to_text():
    try:  
        with microphone as source:
            print('Say something')
            audio = recognizer.listen(source, phrase_time_limit=10) 
        return recognizer.recognize_google(audio, language='cmn-Hant-TW')
    except sr.UnknownValueError:  
        print("Could not understand audio")  
    except sr.RequestError as e:  
        print("Error; {0}".format(e))  
    except Exception as e:
        print(e)

def text_to_speech(text):
    tts = gTTS(text=text, lang='zh-tw')
    tts.save('res/tts')
    _ = os.system("mplayer res/tts > /dev/null")


def intersects(l1, l2):
    return len( set(l1).intersection(set(l2)) ) > 0

speech = [
    '你的腰最近還好嗎?',
    '還是要多注意喔',
    '那要不要去檢查',
    '要不要跟孩子說',
    '真的嗎? 但是這樣孩子們會擔心喔',
    '好! App提醒孩子',
    '好吧，那你要注意安全喔',
    '好吧，那我先幫你記下來'
]
choices = [
    ['很好 不錯 可以 還行','不好 不太好 不舒服'],
    ['好','不要'],
]
conversation = {
    speech[0]: {'choice': choices[0], 0: speech[2], 1: speech[1]},
    speech[2]: {'choice': choices[1], 0: speech[4], 1: speech[3]},
    speech[3]: {'choice': choices[1], 0: speech[6], 1: speech[5]},
    speech[4]: {'choice': choices[1], 0: speech[7], 1: speech[5]}
}

class Machine():
    state = speech[0]

    def __init__(self):
        self.state = speech[0]

    def action(self):
        state = self.state

        # text_to_speech(state)

        if state not in conversation:
            return False

        #     heard = speech_to_text()

        print(heard)
        # segged = jieba.lcut(heard)
        for x in segged:
            print(x, end=' ')
        print()

        decision = conversation[state]['choice']
        negatives = decision[1].split(' ')
        positives = decision[0].split(' ')

        if intersects(segged, positives):
            self.state = conversation[state][1]
        elif intersects(segged, negatives):
            self.state = conversation[state][0]

        return True

if __name__ == '__main__' :
    machine = Machine()
    while machine.action():
        pass
