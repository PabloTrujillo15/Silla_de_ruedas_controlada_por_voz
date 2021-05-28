%matplotlib inline
import numpy as np
import pandas as pd 
import sklearn
import matplotlib.pyplot as plt 
from sklearn.naive_bayes import GaussianNB,BernoulliNB,MultinomialNB 
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.feature_extraction.text import TfidfVectorizer
import speech_recognition as sr
import pyttsx3
import time
import pywhatkit
import serial
from sklearn.ensemble import RandomForestClassifier

listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)


ser = serial.Serial('COM3', 9600)

print('Los comandos validos para el control de la silla son:')
print('"Adelante,Avanza"\n"Reversa"\n"Derecha,Diestra,Giro derecha"\n"izquierda,Zurda, Giro izquierda"\n"Detente,Para,Alto"') 


def listen():
    with sr.Microphone() as source:

        print("Estamos escuchando...")
        voice = listener.listen(source)
        rec = listener.recognize_google(voice, language='es-ES')
        rec = rec.lower()
        print(rec)
    return rec 



def IA():
    data = pd.read_csv("data2.csv")
    data.head(5)
    data.comando[2]
    x1 = data.comando
    y = data.tipo
    vector = TfidfVectorizer()
    x = vector.fit_transform(x1)
    features_names = vector.get_feature_names()
    features_names[20:30]
    
    x = x.toarray()
    
    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.3, random_state = 10)
    #x_train, x_test, y_train, y_test = train_test_split(x,y, random_state = 42)
    
    #model = RandomForestClassifier(n_estimators = 45) #50%
    model = BernoulliNB(alpha = 0.01) #75%
    #model = GaussianNB() #75%
    model.fit(x_train,y_train)
    y_predict = model.predict(x_test)

    print('Con un nivel de confianza del: 75%' )
    print(accuracy_score(y_test,y_predict))
    print(classification_report(y_test,y_predict))
    pd.crosstab(y_test,y_predict)
    
    print('Analisis...')
    
    rec = listen()
    nueva_frase = pd.Series([rec])
    nueva_frase_transformed = vector.transform(nueva_frase)
    
    prediccion = model.predict(nueva_frase_transformed)
    print(prediccion)
    
    if prediccion == 'adelante':
        if not ser.isOpen():
            ser.open()
            print('com3 is open', ser.isOpen())
        print('Usted indico: adelante')
        #Metodo 1 (archivo: python a arduino)
        #led1 = ('1')
        #led2 = ('1')

        #ser.write(led1.encode())
        #val1=led1.encode('utf-8', 'ignore')
        #val1=led1.encode('ascii', 'ignore')
        #print(type(val1))

        #metodo 2 (archivo: Pruebas de comunicacion)
        led1 = 1
        led2 = 1

        cad = str(led1) + "," + str(led2)
        ser.write(cad.encode('ascii'))
        print(type(cad))
        print(cad)

        #metodo 3 (archivo: comunicacion andrea)
        #var = "9".enconde('utf-8')
        #ser.write(var) 
        
    elif prediccion == 'atras':
        print('Usted indico: atras')
        if not ser.isOpen():
            ser.open()
            print('com3 is open', ser.isOpen())
        print('Usted indico: adelante')
        
        #metodo 2 (archivo: Pruebas de comunicacion)
        led1 = 2
        led2 = 2

        cad = str(led1) + "," + str(led2)
        ser.write(cad.encode('ascii'))
        print(type(cad))
        print(cad)
        
    elif prediccion == 'izquierda':
        print('Usted indico: izquierda')
        
        if not ser.isOpen():
            ser.open()
            print('com3 is open', ser.isOpen())
        print('Usted indico: adelante')
        
        #metodo 2 (archivo: Pruebas de comunicacion)
        led1 = 1 #motor derecha
        led2 = 0 #motor izquierda

        cad = str(led1) + "," + str(led2)
        ser.write(cad.encode('ascii'))
        print(type(cad))
        print(cad)
        
    elif prediccion == 'derecha':
        print('Usted indico: derecha')
        
        if not ser.isOpen():
            ser.open()
            print('com3 is open', ser.isOpen())
        print('Usted indico: adelante')
        
        #metodo 2 (archivo: Pruebas de comunicacion)
        led1 = 0 #motor derecha
        led2 = 1 #motor izquierda

        cad = str(led1) + "," + str(led2)
        ser.write(cad.encode('ascii'))
        print(type(cad))
        print(cad)
        
    elif prediccion == 'detente':
        print('Usted indico: detente')
        print('Usted indico: derecha')
        
        if not ser.isOpen():
            ser.open()
            print('com3 is open', ser.isOpen())
        print('Usted indico: adelante')
        
        #metodo 2 (archivo: Pruebas de comunicacion)
        led1 = 0 #motor derecha
        led2 = 0 #motor izquierda

        cad = str(led1) + "," + str(led2)
        ser.write(cad.encode('ascii'))
        print(type(cad))
        print(cad)
        
    else: 
        print('No es un comando valido')
   


#while True:
IA()