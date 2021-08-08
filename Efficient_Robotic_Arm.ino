
#include <Servo.h>

Servo servo0;
Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;

int servoPositions[5];
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
servo0.attach(3);
servo1.attach(5);
servo2.attach(6);
servo3.attach(9);
servo4.attach(10);
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
servo0.write(servoPositions[0]);
servo1.write(servoPositions[1]);
servo2.write(servoPositions[2]);
servo3.write(servoPositions[3]);
servo4.write(servoPositions[4]);

delay(500);
}
