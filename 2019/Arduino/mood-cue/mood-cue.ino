#include <Servo.h>
Servo myServo;

const int potPin = A0;
int potVal;
int angle;

void setup() {
  myServo.attach(9); // link with pin 9
  Serial.begin(9600);
}

void loop() {
  potVal = analogRead(potPin); // take in potentiometer input
  Serial.print("pot val: ");
  Serial.print(potVal);
  
  angle = map(potVal, 0, 1023, 0, 179); // map changes values as per specs
  Serial.print(", angle: ");
  Serial.println(angle);
  
  myServo.write(angle); 
  delay(15); // delay to ensure that the servo motor spins properly
}
