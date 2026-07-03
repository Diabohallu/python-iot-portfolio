#include <LiquidCrystal_I2C.h>

int sensorPin = A0; //Soil Moisture Sensor

int relayPin = 10; //Relay Controlling Water Pump

int buzzerPin = 9; //Buzzer
int red_led = 8; // Red LED
int green_led = 7; // Gree LED

LiquidCrystal_I2C lcd(0*21,16,2);
int threshold = 500; //Moisture

void setup() {

  pinMode(10, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(7, OUTPUT);

  lcd.init();
  lcd.backlight();
  lcd.setCursor(0,0);
  lcd.print("System is Ready");
  delay(3000);
  lcd.clear();

  digitalWrite(10, HIGH);
  digitalWrite(9, LOW);

  Serial.begin(9600);

}

void loop() {

  int moisture = analogRead(A0);

  Serial.print("Soil Moisture: ");
  Serial.println(moisture);

  if(moisture < threshold) {

    digitalWrite(10, HIGH); // Relay controlling Water Pump
    digitalWrite(9, HIGH);  // Buzzer
    digitalWrite(8, HIGH);  // Red LED
    digitalWrite(7, LOW);   // Green LED

    lcd.setCursor(0,0);
    lcd.print("Low Moisture");
    lcd.setCursor(0,1);
    lcd.print("Pumping Water");

    Serial.println("Pump ON - Buzzer ON");

  }
  else {

    digitalWrite(10, LOW);
    digitalWrite(9, LOW);
    digitalWrite(8, LOW);
    digitalWrite(7, HIGH);

    lcd.setCursor(0,0);
    lcd.print("Sufficient Water");
    lcd.setCursor(0,1);
    lcd.print("Pump is OFF");

    Serial.println("Pump ON - Buzzer ON");

  }
  delay(1000);

}



















































