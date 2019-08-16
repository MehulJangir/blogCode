// output pins for 4-pin RGB LED
const int greenLEDPin = 9;
const int redLEDPin = 10;
const int blueLEDPin = 11;

// inputs from each phototransistor
const int redSensPin = A0;
const int greenSensPin = A1;
const int blueSensPin = A2;

// rgb value for each component (LED)
int redVal = 0;
int greenVal = 0;
int blueVal = 0;

// incoming rgb values from phototransistors
int redSensVal = 0;
int greenSensVal = 0;
int blueSensVal = 0;

void setup() {
  Serial.begin(9600);
  pinMode(greenLEDPin, OUTPUT);
  pinMode(redLEDPin, OUTPUT);
  pinMode(blueLEDPin, OUTPUT);
}

void loop() {
  redSensVal = analogRead(redSensPin);
  delay(5);
  greenSensVal = analogRead(greenSensPin);
  delay(5);
  blueSensVal = analogRead(blueSensPin);

  Serial.print("sensor values -> R: ");
  Serial.print(redSensVal);
  Serial.print(", G: ");
  Serial.print(greenSensVal);
  Serial.print(", B: ");
  Serial.println(blueSensVal);

  redVal = redSensVal/4;
  greenVal = greenSensVal/4;
  blueVal = blueSensVal/4;

  analogWrite(redLEDPin, redVal);
  analogWrite(blueLEDPin, blueVal);
  analogWrite(greenLEDPin, greenVal);
}
