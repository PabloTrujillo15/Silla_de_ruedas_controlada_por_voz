# Silla de ruedas controlado por la voz 

Este dispositivo es controlado por medio de la voz con cinco comandos básicos los cuales son: adelantes, reversa, derecha, izquierda y detente. Además se evalúa el desempeño del algoritmo previamente propuesto presentando la menor cantidad de errores posibles al momento de hacer la validación. Este algoritmo fue programado en lenguaje Python en el notebook de Jupyter, se seleccionó el clasificador **_BernoulliNB_**.

Este repositorio contiene:
-   Algoritmo fuente
-   Datos :
    -  Scripts de desarrollo (Python3 y Arduino)
      -   Base de datos
# Requisitos de hardware
  -  Computador
  -   Micrófono del computador
     -  Arduino 
    
# Requisitos de software
-   Python 3.8 :
    -  Reconocimiento de voz 
    - PyAudio
    - Pandas
    - Numpy
    - Sklearn
    - Enhebrar
    - Speech recognition 
    - Pyttsx3
    - Time
    - Serial 
## Instalación de librerías 
Como se muestra a continuación son las librerías que se utilizó para la elaboración del algoritmo

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
A continuación se mostrará como se hace la instalación de las librerías
### Instalar PyAudio

Primero, asegúrese de tener Python3.8, luego se ejecuta el comando:

    $ pip install PyAudio
  ### Instalar Pandas

Segundo, instalar la librería con el siguiente comando:

    $ pip install Pandas
### Instalar Numpy

Seguidamente, instalar la librería numpy con el siguiente comando:

    $ pip install numpy
Para las demás librerías se realiza el mismo proceso de instalación como lo son: 
     -Sklearn
    - Enhebrar
    - Speech recognition 
    - Pyttsx3
    - Time
    - Serial 

    $ pip install (librería a instalar)


### Configuración de la adquisición de voz
Se hace la adquisición por medio del micrófono del computador y esta en procesada en el algoritmo

    def listen():
    with sr.Microphone() as source:

        print("Estamos escuchando...")
        voice = listener.listen(source)
        rec = listener.recognize_google(voice, language='es-ES')
        rec = rec.lower()
        print(rec)
    return rec
   
  Es necesario usar un dispositivo arduino como esclavo y configurar el puerto de arduino con el código anterior
  

    ser = serial.Serial('COM3', 9600)
Ejemplo de comunicación serial sencilla con leds

    int led13 = 13;
    int led12 = 12;
    String cad;
    
    void setup()
    {    
      Serial.begin(9600);
      delay(30);
      pinMode(led13,OUTPUT);
      digitalWrite(led13,0);
     
      Serial.begin(9600);
      delay(30);
      pinMode(led12,OUTPUT);
      digitalWrite(led12,0);
     }
    int pos = 0,val_led1,val_led2;
    String cad1,cad2;
    
    void loop()  
    {
      if(Serial.available()){
        cad = Serial.readString();
        pos = cad.indexOf(',');
        cad1 = cad.substring(0,pos);
        cad2 = cad.substring(pos+1);
        
        if(val_led1 != cad1.toInt())
        {
          val_led1 = cad1.toInt();
          digitalWrite(led13,val_led1);
        }
        
        if(val_led2 != cad2.toInt())
        
        {
          val_led2 = cad2.toInt();
          digitalWrite(led12,val_led2);
        }
        cad = cad + "-Dato procesado";
        Serial.print(cad1);
        Serial.print(cad2);
        }
      delay(5000);
      digitalWrite(led12,LOW);
      digitalWrite(led13,LOW);
      }
      
### Autores:

**Universidad de Ibagué** - **Ingeniería Electrónica** **Inteligencia Artificial - Curso: 2021 / A**

-   [Harold F Murcia](http://haroldmurcia.com/) - _Tutor_
-   [Laura Valentina Ruiz Gonzalez](mailto:2420161037@estudiantesunibague.edu.co)
-   [Pablo German Trujillo Martinez](mailto:2420171041@estudiantesunibague.edu.co)




 
