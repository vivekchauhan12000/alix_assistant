import speech_recognition as sr
print('it work')

r = sr.Recognizer()
def record_audio():
 with sr.Microphone() as source:
    audio = r.listen(source)
    voice_data=''
    try:
         voice_data = r.recognize_google(audio)
         
    except sr.UnknownValueError:
        print("sorry, I did not get that")
    except sr.RequestError:
        print("speech is dwon today")   
    return voice_data

def respond(voice_data):
   if 'name' == voice_data:
      print("My name is alix")

print("how can i help you")        
voice_data = record_audio()
print("me:" + voice_data)
respond(voice_data)

