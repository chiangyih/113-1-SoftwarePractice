#include <Arduino.h>

int led = 2; // GPIO2

void setup()
{
  pinMode(led, OUTPUT);
  Serial.begin(9600);
  Serial.println("Type '1' to turn the LED on and '2' to turn it off");
}

void loop() 
{
  if (Serial.available() > 0) 
  {
    String cmd = Serial.readStringUntil('\n');
    if (cmd == "1") 
    {
      digitalWrite(led, HIGH);
      Serial.println("LED is on");
    } 
    else if (cmd == "2") 
    {
      digitalWrite(led, LOW);
      Serial.println("LED is off");
    } 
    else if (cmd == "3")
    {
      Serial.println("LED is blinking"); //閃爍5次
      for (int i = 0; i < 5; i++)
      {
        digitalWrite(led, HIGH);
        delay(200);
        digitalWrite(led, LOW);
        delay(200);
      }
    }
    else 
    {
      Serial.println("Invalid command");
    }
  }
}
