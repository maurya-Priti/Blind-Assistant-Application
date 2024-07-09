import pytesseract
from gtts import gTTS
import os
from playsound import playsound

# Set the path to the Tesseract executable (if necessary)
pytesseract.pytesseract.tesseract_cmd = r'your Tesseract path'

# Set the TESSDATA_PREFIX environment variable
os.environ['TESSDATA_PREFIX'] = r'C://Program Files//Tesseract-OCR//tessdata'
import cv2


cap = cv2.VideoCapture(0)
frame_count = 0
#start = time.time()
first = True
frames = []


while cap.isOpened():
  frame_count +=1
  success, image = cap.read()
  if not success:
    print("Ignoring empty camera frame.")
    continue
  if frame_count == 100:
    break
  if success:
      imgH, imgW, _ = image.shape
      x1,y1,w1,h1=0,0,imgH,imgW
      
      results = pytesseract.image_to_string(image)
      print(results)
      if len(results)>1:
        mytext= results
    
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save('output.mp3')
        playsound("output.mp3")
        os.remove('output.mp3')
      
  boxes= pytesseract.image_to_boxes(image)
  for box in boxes.splitlines():
    box=box.split(' ')
    x,y,w,h=int(box[1]),int(box[2]),int(box[3]),int(box[4])
    cv2.rectangle(image,(x,imgH-y),(w,imgH-h),(0,0,255),3)
    
    
  cv2.putText(image, '%s' % (results), (0,20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (455,255,255), 2)
  cv2.imshow('Text detection', image)

#cap.release()
#cv2.destroyAllWindows()   
