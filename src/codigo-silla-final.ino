int izqA = 5;
int derA = 11;
int izqB = 6;
int derB = 3;
int vel = 150; // Velocidad de los motores (0-255)
int led13 = 13;
int led12 = 12;
int val_atras = 1;
String cad;

int pos = 0, val_led1, val_led2, val_led3;
String cad1, cad2, cad3;

void setup()

{
  Serial.begin(9600);
  pinMode(derA, OUTPUT);
  pinMode(derB, OUTPUT);
  pinMode(izqA, OUTPUT);
  pinMode(izqB, OUTPUT);

  Serial.begin(9600);
  delay(30);
  pinMode(led13, OUTPUT);
  digitalWrite(led13, 0);

  Serial.begin(9600);
  delay(30);
  pinMode(led12, OUTPUT);
  digitalWrite(led12, 0);
}




void loop()
{
  if (Serial.available()) {
    cad = Serial.readString();
    pos = cad.indexOf(',');
    cad1 = cad.substring(0, pos);
    cad2 = cad.substring(pos + 1);
  

    if (val_led1 != cad1.toInt())
    {
      val_led1 = cad1.toInt();
      //digitalWrite(led13, val_led1);

    }

    if (val_led2 != cad2.toInt())

    {
      val_led2 = cad2.toInt();
      //digitalWrite(led12, val_led2);

    }


    //adelante
    if (val_led1 == 1)
    {
      if (val_led2 == 1)
      {
        //Serial.print("Entro_adelante_derecha");
        analogWrite(derA, vel);
        digitalWrite(led13, 1);
        //delay(2000);
        //Serial.print("Entro_adelante_izquierda");
        analogWrite(izqA, vel);
        digitalWrite(led12, 1);
        //delay(2000);
      }
    }


    // izquierda
    if (val_led1 == 1)
    {
      if (val_led2 == 0)
      {
        //Serial.print("Entro_adelante_derecha");
        analogWrite(derA, 0);
        digitalWrite(led13, 1);
        //delay(2000);
        //Serial.print("Entro_adelante_izquierda");
        analogWrite(izqA, vel);
        digitalWrite(led12, 0);
        //delay(2000);
      }
    }

    // derecha
    if (val_led1 == 0)
    {
      if (val_led2 == 1)
      {
        //Serial.print("Entro_adelante_derecha");
        analogWrite(derA, vel);
        digitalWrite(led13, 0);
        //delay(2000);
        //Serial.print("Entro_adelante_izquierda");
        analogWrite(izqA, 1);
        digitalWrite(led12, 1);
        //delay(2000);
      }
    }

    // atras
    if (val_led1 == 2 && val_led2 == 2 )
    {
      analogWrite(derB, vel);
      analogWrite(izqB, vel);
      
      digitalWrite(led13, 1);
      digitalWrite(led12, 1);
      delay(500);
      digitalWrite(led13, 0);
      digitalWrite(led12, 0);
      delay(500);
      digitalWrite(led13, 1);
      digitalWrite(led12, 1);
      delay(500);
      digitalWrite(led13, 0);
      digitalWrite(led12, 0);
    }

    //detente
    if (val_led1 == 0 && val_led2 == 0)
    {
      digitalWrite(led13, 1);
      digitalWrite(led12, 1);
      delay(500);
      digitalWrite(led13, 0);
      digitalWrite(led12, 0);
      delay(500);
      digitalWrite(led13, 1);
      digitalWrite(led12, 1);
      delay(500);
      digitalWrite(led13, 0);
      digitalWrite(led12, 0);
      delay(500);
      digitalWrite(led13, 1);
      digitalWrite(led12, 1);
      delay(500);
      digitalWrite(led13, 0);
      digitalWrite(led12, 0);
      delay(500);
      digitalWrite(led13, 1);
      digitalWrite(led12, 1);
      delay(500);
      digitalWrite(led13, 0);
      digitalWrite(led12, 0);
    }












    cad = cad + "-Dato procesado";
    Serial.print(cad1);
    Serial.print(cad2);
    Serial.print(cad3);

  }
  delay(2500);
  digitalWrite(led12, LOW);
  digitalWrite(led13, LOW);
  analogWrite(derA, 0);    // Detiene los Motores
  analogWrite(izqA, 0);
  analogWrite(derB, 0);    // Detiene los Motores
  analogWrite(izqB, 0);

}
