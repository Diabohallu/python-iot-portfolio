#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27,16,2);
int smoke = 10;

void setup() {

  pinMode(10,INPUT);

  lcd.init();
  lcd.backlight();
  lcd.setCursor(0,0);
  lcd.print("Smoke sensor is");
  lcd.setCursor(0,1);
  lcd.print("Ready");
  delay(3000);
  lcd.clear();

}

void loop() {

  int smoke = digitalRead(10);

  if (smoke == HIGH){
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Smoke Detected");
    lcd.setCursor(0,1);
    lcd.print("Alert!!!");
    delay(500);
  }
  else {
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("No Smoke");
    lcd.setCursor(0,1);
    lcd.print("Detected");
    delay(500);
  }

}
