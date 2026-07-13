const int soundPin = A0; 
const int relayPin = 8; 
int threshold = 300;
bool bulbState = false;
unsigned long lastClapTime = 0;
const unsigned long debounceDelay = 700; 

void setup() {
  pinMode(relayPin, OUTPUT); 
  
  digitalWrite(relayPin, LOW); 
}

void loop() {
  int soundValue = analogRead(soundPin);

  if (soundValue > threshold && (millis() - lastClapTime) > debounceDelay) {
    bulbState = !bulbState; 
    digitalWrite(relayPin, bulbState ? HIGH : LOW); 
    lastClapTime = millis(); 
  }
}
