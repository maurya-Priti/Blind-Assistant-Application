from ultralytics.models.yolo.model import YOLO  
from gtts import gTTS
import os
from playsound import playsound
import cv2

import speech_recognition as sr  

# get audio from the microphone                                                                       
r = sr.Recognizer()   
                                                                               


#import os

model = YOLO("yolov8n.pt")  

def listen():
   voice_input=""
   while (voice_input !="stop"):
    
    # get audio from the microphone                                                                            
    
    r = sr.Recognizer()   
    with sr.Microphone() as source:                                                                       
        print("Speak:")                                                                                   
        audio = r.listen(source) 
        voice_input=r.recognize_google(audio)
        try:
            print("You said " + r.recognize_google(audio))
            voice_input=r.recognize_google(audio)
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        if voice_input=="describe environment" or voice_input=="describe":
            object()
       # elif voice_input=="stop":
            
        else:
            break
            #listen()
      
            
def object():
    cap=cv2.VideoCapture(0) 
    results = model.predict(imgsz=512, stream=True, source="0",show=True) # source already setup 
    print(results)
    for r in results:  
        print(r)       
        for c in r.boxes.cls:             
            language = 'en'
            mytext= str(model.names[int(c)])
            print(mytext)
            myobj = gTTS(text=mytext, lang=language, slow=False)
            myobj.save('output.mp3')
            playsound("output.mp3")
            os.remove('output.mp3')  
            # cap.release()
            #cv2.destroyAllWindows()
            

    
   
           

listen()
