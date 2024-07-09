import subprocess
from flask import Flask, jsonify, render_template, request, Response
import sys
import os
import time
import speech_recognition as sr  
import ultralytics
# get audio from the microphone                                                                       
r = sr.Recognizer() 





app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/start')
def start():
    global process
    command = "python detect_text.py"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    return render_template('index.html')
@app.route('/stop')
def stop():
    global process
    if process is not None:
        process.terminate()
        
        process.kill()
        return render_template('index.html')
        
    else:
        return render_template('index.html')

@app.route('/start_listen')
def listen():
   voice_input=""
   while (voice_input !="stop"):
                # get audio from the microphone                                                                       
               # r = sr.Recognizer()   
    
    r = sr.Recognizer()   
    with sr.Microphone() as source:                                                                       
        print("Speak:")                                                                                   
        audio = r.listen(source) 
      #  voice_input=r.recognize_google(audio)
        try:
            print("You said " + r.recognize_google(audio))
            voice_input=r.recognize_google(audio)
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        if voice_input=="describe environment":
            #command = "python real-time-audio.py"
            start_obj()
            listen()
        elif voice_input=="text":
            start()
            listen()
        elif voice_input=="stop":
            stop_obj()
            stop()
            
        else:
            listen()
      #  elif voice_input=="stop":
            

@app.route('/start_obj')
def start_obj():
    global process
    command = "python detect_object.py"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    return render_template('index.html')
@app.route('/stop_obj')
def stop_obj():
    global process
    if process is not None:
      #  time.sleep(12) # <-- sleep for 12''
        process.terminate()
        
        process.kill()
        return render_template('index.html')
        
    else:
        
        return render_template('index.html')




if __name__ == "__main__" :
    app.run(debug=True)