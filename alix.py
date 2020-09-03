import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
print('it work')

r = sr.Recognizer()
def record_audio(ask=False):
 with sr.Microphone() as source:
    if ask:
       print(ask)
    audio = r.listen(source)
    voice_data=''
    try:
         voice_data = r.recognize_google(audio)
         
    except sr.UnknownValueError:
        print("sorry, I did not get that")
    except sr.RequestError:
        print("speech is dwon today")   
    return voice_data

def alix_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1,1000000)
    audio_file= 'audio-' + str(r) +'.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
   if 'name' == voice_data:
       alix_speak("My name is alix")
   if 'search' in voice_data:
       search = record_audio('what do you want to search?') 
       url = 'https://google.com/search?q='+ search
       webbrowser.get().open(url)
       alix_speak('here is what I found for ' + search)
   if 'exit' in voice_data:
       exit()


time.sleep(1)
alix_speak("how can i help you")
while 1:        
   voice_data = record_audio()
   print("me:" + voice_data)
   respond(voice_data)

