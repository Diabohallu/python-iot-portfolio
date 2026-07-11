#include <Servo.h>
Servo myservo;
#include <LiquidCrystal_I2C.h> 
LiquidCrystal_I2C lcd(0x27,16,2);

int val = 0;
int pos = 0;
int pir = 7; 

const int redLed = 8;
const int greenLed = 9;

void setup() {

  Serial.begin(9600);
  pinMode(7,INPUT); 
  myservo.attach(6); 
  myservo.write(0);

  pinMode(8,OUTPUT);
  pinMode(9,OUTPUT); 

  lcd.init();
  lcd.backlight();
  lcd.setCursor(0,0);
  lcd.print("Door is Closed");

}

void loop() {

  val = digitalRead(7); 
  Serial.println(val); 
  delay(100); 

  if (val == 1 && pos == 0){
      digitalWrite(8,LOW);
      digitalWrite(9,HIGH); 
      lcd.setCursor(0,0);
      lcd.print("Door is Opening");

    for (pos = 0; pos <= 120; pos++) 
    {
      myservo.write(pos); 
      delay(10);
    }
    delay(3000);
  }

  else if (val == 0 && pos == 120){
      digitalWrite(8,HIGH); 
      digitalWrite(9,LOW); 
      lcd.setCursor(0,0);
      lcd.print("Door is Closing");
   
    for (pos = 120; pos >= 0; pos--) 
    {
      myservo.write(pos); 
      delay(10);
    }
    
  }
}
