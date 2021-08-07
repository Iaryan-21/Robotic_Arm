
#include <Servo.h>

Servo servoA;
Servo servoB;
Servo servoC;
Servo servoD;
Servo servoE;

int servoPositions[5];
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
servoA.attach(3);
servoB.attach(5);
servoC.attach(6);
servoD.attach(9);
servoE.attach(10);
}

void loop() {
  // put your main code here, to run repeatedly:
while(Serial.available()){
  String input = Serial.readStringUntil('\n');
  servoPositions[0] = input.substring(0,3).toInt();
  servoPositions[1] = input.substring(3,6).toInt();
  servoPositions[2] = input.substring(6,9).toInt();
  servoPositions[3] = input.substring(9,12).toInt();
  servoPositions[4] = input.substring(12,15).toInt();
}
servoA.write(servoPositions[0]);
servoB.write(servoPositions[1]);
servoC.write(servoPositions[2]);
servoD.write(servoPositions[3]);
servoE.write(servoPositions[4]);

delay(500);
}
