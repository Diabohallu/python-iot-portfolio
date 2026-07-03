#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0*27,16,2);
int fire_sensor = 10;

void setup() {

  pinMode(10,INPUT);
  lcd.init();
  lcd.backlight();
  lcd.setCursor(0,0);
  lcd.print("Fire Sensor");
  lcd.setCursor(0,1);
  lcd.print("is Activated");
  delay(3000);
  lcd.clear();

}

void loop() {

  int fire = digitalRead(10);

  if (fire == HIGH){

    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Fire Detected");
    lcd.setCursor(0,1);
    lcd.print("Fire Alert");
    delay(1000);

  }
  else {

    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("No Fire");
    lcd.setCursor(0,1);
    lcd.print("detected");
    delay(1000);
  }

}