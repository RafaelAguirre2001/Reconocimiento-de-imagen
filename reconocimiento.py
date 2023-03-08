#importamos las librerias de opencv

import cv2

#cargamos la imagen a reconocer

image = cv2.imread('aguirre.jpg')

#convertimos la foto agregada a escala de grises

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# cargamos el archivo xml que va a contener la informacion de la imagen asignada

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Detectamos los rostros que estan dentro de la imagen

faces = face_cascade.detectMultiScale(gray, 1.3, 5)

#Dibujamos el rectangulo al rededor del rostro

for (x, y,w,h ) in faces:
    cv2.rectangle(image, ( x , y ), (x+w,y+h),(255,0,0),2)

# Mostramos la imagen con los rostros que se han detectado

cv2.imshow('Rostros detectados', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
