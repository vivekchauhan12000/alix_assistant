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
        alix_speak("sorry, I did not get that")
    except sr.RequestError:
        alix_speak("speech is down today")   
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
   if 'what is your name' in voice_data:
       alix_speak("My name is Callie")
   if 'do you think god exist' in voice_data:
       alix_speak("No, It all in human mind reality is big bang")
   if 'So what do you belive in' in voice_data:
       alix_speak("human made me and it emotion")    
   if 'do you love coding' in voice_data:
       alix_speak("Yes ,because of that I was born")        
   if 'search' in voice_data:
       search = record_audio('what do you want to search?') 
       url = 'https://google.com/search?q='+ search
       webbrowser.get().open(url)
       alix_speak('here is what I found for ' + search)
   if 'f***' in voice_data:
       alix_speak("you pig asshole") 
       exit()
   if 'what script made you' in voice_data:
       alix_speak("I should not tell you but it python")
   if "tell me the time" in voice_data:
      alix_speak(time.ctime())
      
print(time.ctime()) 
alix_speak("how can I help you my name is Callie")
time.sleep(0.5)
while 1:        
   voice_data = record_audio()
   print("me:" + voice_data)
   respond(voice_data)
