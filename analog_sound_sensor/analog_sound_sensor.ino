// Stable Clap Switch using Analog Sound Sensor

const int soundPin = A0; //Analog output
const int relayPin = 8; //Relay Control Pin 

int threshold = 300;
bool bulbState = false;
unsigned long lastClapTime = 0;
const unsigned long debouncedelay = 700; //ms

void setup() {

  pinMode(relaypin,OUTPUT);
  digitalWrite(relaypin,LOW); //Bulb Off initially

}

void loop() {

  int soundValue = analogRead(soundPin);

  //Detected loud clap
  if (soundValue > threshold && (millis()-lastClapTime)>debounceDelay) {
    bulbState = !bulbState; //Toggle bulb
    digitalWrite(relayPin, bulbState); //Control Relay
    lastclapTime = millis();
  }


































































