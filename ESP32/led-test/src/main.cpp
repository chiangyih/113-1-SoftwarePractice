// 使內建 LED 閃爍
// 內建接腳為gpio2，也可用builtin_led代替
#include <Arduino.h>
void setup() 
{
  pinMode(2, OUTPUT);
}
void loop() 
{
  digitalWrite(2, HIGH);
  delay(500);
  digitalWrite(2, LOW);
  delay(500);
}