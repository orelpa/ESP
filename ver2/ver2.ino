#include "GyverButton.h"
#include <ETH.h>

char* host = "10.33.1.147"; //адрес сервера 10.33.2.10
uint16_t port = 5837; //порт сервера


const int chConverterPin = 15; //пин частотника
GButton btn1(14); // пин реле коробок
GButton btn2(12); // пин реле картона
GButton  btn3(15); // пин частотника
int converterState = 0;

void setup() {

  Serial.begin(115200); // отладка в порт
  ETH.begin(); // запуск библ ETH
  pinMode(chConverterPin, INPUT);
}

void loop() {
  
  btn1.tick();
  btn2.tick();
  btn3.tick();

  converterState = digitalRead(chConverterPin);

  // put your main code here, to run repeatedly:
      if (btn3.isHold()){
        if (btn1.isRelease()) {
        count_box(host, port);
        Serial.println("box");
      }
      if (btn2.isRelease()) {
        count_paper(host, port);
        Serial.println("paper");
      }
        
      }
      
      
    
  
}

void count_box(char* host, uint16_t port){
  WiFiClient client;
  if (!client.connect(host, port)){
    delay(1000);
  }
  
  if (client.connected()){
    String str = "box";
    client.print(str);
    client.stop();
  }
}

void count_paper(char* host, uint16_t port){
  WiFiClient client;
  if (!client.connect(host, port)){
    delay(1000);
  }
  
  if (client.connected()){
    String str = "paperboard";
    client.print(str);
    client.stop();
  }
}


