/*
  Analog Input
 Demonstrates analog input by reading an analog sensor on analog pin 0 and
 turning on and off a light emitting diode(LED)  connected to digital pin 13.
 The amount of time the LED will be on and off depends on
 the value obtained by analogRead().

 The circuit:
 * Potentiometer attached to analog input 0
 * center pin of the potentiometer to the analog pin
 * one side pin (either one) to ground
 * the other side pin to +5V
 * LED anode (long leg) attached to digital output 13
 * LED cathode (short leg) attached to ground

 * Note: because most Arduinos have a built-in LED attached
 to pin 13 on the board, the LED is optional.


 Created by David Cuartielles
 modified 30 Aug 2011
 By Tom Igoe

 This example code is in the public domain.

 http://www.arduino.cc/en/Tutorial/AnalogInput

 */

int sensorPinSw = A0;
int sensorPinY = A1;
int sensorPinX = A2;// select the input pin for the potentiometer
int left = 13;      // select the pin for the LED
int right = 3;
int pressed = 8;
int up = 7;
int down = 6;
int pressed_down = 0;
int sensorValueSw = 0;
int sensorValueY = 0;
int sensorValueX = 0; // variable to store the value coming from the sensor
int sensitivity = 100;

void setup() {
  // declare the ledPin as an OUTPUT:
  Serial.begin(9600);
  pinMode(left, OUTPUT);
}

void loop() {
  // read the value from the sensor:
  sensorValueSw = analogRead(sensorPinSw);
  sensorValueY = analogRead(sensorPinY);
  sensorValueX = analogRead(sensorPinX);

  // pressed check
  if (sensorValueSw == 0)
  {
    pressed_down += 1;
    if (pressed_down > 5)
    {
      Serial.println("pressed");
      digitalWrite(pressed, HIGH);
      delay(sensitivity);
      digitalWrite(pressed, LOW);
    }
  }
  else
  {
    pressed_down = 0;
    digitalWrite(pressed, LOW);
  }

  // left check
  if (sensorValueX > 1020)
  {
    Serial.println("left");
    digitalWrite(left, HIGH);
    delay(sensitivity);
    digitalWrite(left, LOW);
  }
  else
  {
    digitalWrite(left, LOW);
  }

  // right check
  if (sensorValueX == 0)
  {
    Serial.println("right");
    digitalWrite(right, HIGH);
    delay(sensitivity);
    digitalWrite(right, LOW);
  }
  else
  {
    digitalWrite(right, LOW);
  }

  // up check
  if (sensorValueY > 1020)
  {
    Serial.println("up");
    digitalWrite(up, HIGH);
    delay(sensitivity);
    digitalWrite(up, LOW);
  }
  else
  {
    digitalWrite(up, LOW);
  }

  // down check
  if (sensorValueY == 0)
  {
    Serial.println("down");
    digitalWrite(down, HIGH);
    delay(sensitivity);
    digitalWrite(down, LOW);
  }
  else
  {
    digitalWrite(down, LOW);
  }

  
  delay(300);
  //Serial.println(sensorValueSw);
  //Serial.println(sensorValueY);
  //Serial.println(sensorValueX);

  

}
