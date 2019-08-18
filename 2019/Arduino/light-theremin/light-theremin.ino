int sensVal;
int sensLow = 1023;
int sensHigh = 0;
const int ledPin = 13;
const int sensPin = A0;

void setup() {
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, HIGH);

  // 5 second calibration
  while (millis() < 5000) {
    sensVal = analogRead(sensPin);
    if (sensVal > sensHigh) {
      sensHigh = sensVal;
    }
    if (sensVal < sensLow) {
      sensLow = sensVal;
    }
  }

  digitalWrite(ledPin, LOW);
}

void loop() {
  sensVal = analogRead(sensPin);
  int pitch = map(sensVal, sensLow, sensHigh, 50, 4000);
  tone(8, pitch, 20);
  delay(10);
}
