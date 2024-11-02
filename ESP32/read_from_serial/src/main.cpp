#include <Arduino.h>

// put function declarations here:
int myFunction(int, int);

// 從串列埠讀取資料

void setup() {
  // put your setup code here, to run once:
  // int result = myFunction(2, 3);
  // 初始化串列埠
  Serial.begin(9600);
  pinMode(2, OUTPUT);  // 設定腳位2為輸出(內建LED)
  pinMode(17, OUTPUT);  // 設定腳位17為輸出
}

void loop() 
{
  //判斷串列埠是否有資料
  if(Serial.available() > 0)
  {
    //讀取串列埠資料
    char data = Serial.read();
    
    if (data == '1')
    {
      digitalWrite(2, HIGH); // 設定腳位2為高電位
    } 
    else if (data == '2') 
    {
      digitalWrite(2, LOW); // 設定腳位2為低電位
    } 
    else if (data == '3') 
    {
      for (int i=0 ; i < 10 ; i++); 
      {
        digitalWrite(17, HIGH); // 設定腳位17為高電位
        delay(2000); // 延遲500ms
        digitalWrite(17, LOW); // 設定腳位17為低電位
        delay(2000); // 延遲500ms
      }
    //   digitalWrite(17, HIGH); // 設定腳位17為高電位
    // }
    // else if (data == '4') 
    // {
    //   digitalWrite(17, LOW); // 設定腳位17為低電位
    }
  }
}

// put function definitions here:
int myFunction(int x, int y) {
  return x + y;
}