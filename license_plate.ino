/*
  Ultrasonic Sensor HC-SR04 and Arduino Tutorial

  by Dejan Nedelkovski,
  www.HowToMechatronics.com
*/

#include <stdlib.h>
#include <unistd.h>
#include <stdio.h> 
#include <Servo.h>
 int incomming;
 int a;

Servo myservo;
char command[20];
// defines pins numbers
const int trigPin = 11;
const int echoPin = 12;
// defines variables
long duration;
int distance;
void setup() {
  pinMode(7, OUTPUT);
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPin, INPUT); // Sets the echoPin as an Input
  Serial.begin(9600); // Starts the serial communication
  a=0;
  myservo.attach(9);
  myservo.write(0);
}
void loop() {
  // Clears the trigPin
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  // Sets the trigPin on HIGH state for 10 micro seconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin, HIGH);
  // Calculating the distance
  distance = duration * 0.034 / 2;
  // Prints the distance on the Serial Monitor
  if(Serial.available()>0)
  {
    incomming=Serial.read();
    myservo.write(90);
    delay(10000);
    myservo.write(0);
  }
  else if (distance < 10 && distance >0) {
      Serial.println(distance);
      delay(2000);
      
  }
  delay(2000);
 /* }
  if(a==1)
  {
  incomming=Serial.read();
  digitalWrite(7, LOW);
  if(incomming==0){
      digitalWrite(7, HIGH);
  }
  }*/
  delay(1000);
}
