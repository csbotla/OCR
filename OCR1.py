import cv2
import urllib.request
import pytesseract

#cap = cv2.VideoCapture('http://192.168.0.102:8080/video')#Camera source from android app
cap = cv2.VideoCapture(0)
cv2.namedWindow("test")
#cv2.resizeWindow("test",(20,20))

img_counter = 0

while True:
    ret, frame = cap.read()
    cv2.imshow("test", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        print("Frame captured!!")
        img_name = "opencv_frame.jpeg"
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1
        result = pytesseract.image_to_string(img_name)
        print(result)

        file=open('f1.txt','w',encoding='utf-8')
        print("Writing into File")
        file.write(result)
        file.close()

    '''i=1
    i=i + 1
    result = ''
    if i == 30:
        result = pytesseract.image_to_string(opencv_frame)
        print(result)
        str = re.sub('[^0-9a-zA-Z -]+', '', result)
        i=1

    if str!='':
        str_show = str
        prev_str = str
    else:
        str_show = prev_str

    #cv2.putText(frame,str_show, (230, 50), font, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
    #cv2.imshow('frame',frame)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break'''

cap.release()

cv2.destroyAllWindows()
