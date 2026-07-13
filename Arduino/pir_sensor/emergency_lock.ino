#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0*21, 16, 2);
int pir = 10;
int led = 9;
int alarm = 8; 
int emergency_lock = 7; 

void setup() {

  pinMode(pir,INPUT);
  pinMode(led,OUTPUT);
  pinMode(alarm,OUTPUT); 
  pinMode(emergency_lock,OUTPUT);

  lcd.init();
  lcd.backlight();
  lcd.setCursor(0,0);
  lcd.print("System Ready");
  delay(3000);
  lcd.clear();

}

void loop(){

  int motion = digitalRead(pir);

  if (motion == HIGH){

    digitalWrite(led,HIGH);
    digitalWrite(alarm,HIGH);
    digitalWrite(emergency_lock,HIGH);

    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Motion Detected");
    lcd.setCursor(0,1);
    lcd.print("Alarm!");
    lcd.clear();
  }

  else{

    digitalWrite(led,LOW);
    digitalWrite(alarm,LOW);
    digitalWrite(emergency_lock,LOW);

    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("No Motion");
    lcd.setCursor(0,1);
    lcd.print("Detected");
    lcd.clear();

  }

}
