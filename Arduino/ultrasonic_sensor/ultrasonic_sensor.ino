#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0*21,16,2);
int trigPin = 8;
int echoPin = 9;

int distance;
long duration;

void setup() {

  pinMode(8,OUTPUT);
  pinMode(9,INPUT);

  lcd.init();
  lcd.backlight();
  lcd.setCursor(0,0);
  lcd.print("Ultrasonic sensor");
  lcd.setCursor(0,1);
  lcd.print("is ready");
  delay(3000);
  lcd.clear();

}

void loop() {

  digitalWrite(8,LOW);
  delayMicroseconds(2);
  digitalWrite(8,HIGH);
  delayMicroseconds(10);
  digitalWrite(8,LOW);

  duration = pulseIn(9,HIGH);
  distance = duration*0.031/2;
  
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("Distance is");
  lcd.setCursor(0,1);
  lcd.print(distance);
  delay(500);

}
