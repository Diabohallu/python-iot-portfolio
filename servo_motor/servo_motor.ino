#include <Servo.h>
Servo myservo;
#include <LiquidCrystal_I2C.h> //Added LCD
LiquidCrystal_I2C lcd(0x27,16,2);

int val = 0;
int pos = 0;
int pir = 7; //Added pir sensor connected to pin 7 for clarification

const int redLed = 8;
const int greenLed = 9;

void setup() {

  Serial.begin(9600);
  pinMode(7,INPUT); //pir sensor output pin connected
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

  val = digitalRead(7); //pir sensor output pin connected
  Serial.println(val); //see the value in serial monitor in Arduino IDE
  delay(100); 

  if (val == 1 && pos == 0){
      digitalWrite(8,LOW); //Made Red LED turn off while Door opens
      digitalWrite(9,HIGH); //Made Green LED glow while Door opens
      lcd.setCursor(0,0);
      lcd.print("Door is Opening");

    // Instead of Door opening when pos is at 0 and staying open at 120, Door opens when pos is less than 120 degrees too
    for (pos = 0; pos <= 120; pos++) // goes from 0 degrees to 120 degrees in steps of 1 degree
    {
      myservo.write(pos); // tells servo to go from position in variable "pos"
      delay(10); // wait 10 ms for the servo to reach the position 
    }
    delay(3000);
  }

  else if (val == 0 && pos == 120){
      digitalWrite(8,HIGH); //Made Red LED glow while Door closes
      digitalWrite(9,LOW); //Made Green LED turn off while Door closes
      lcd.setCursor(0,0);
      lcd.print("Door is Closing");

    // Instead of Door closing when pos is at 120 and staying closed at 0, Door closes when pos is greater than 0 degrees too
    for (pos = 120; pos >= 0; pos--) // goes from 120 degrees to 0 degrees
    {
      myservo.write(pos); 
      delay(10);
    }
    
  }
}
