
#include <ETH.h>

char* host = "10.33.1.147"; //адрес сервера
uint16_t port = 5837; //порт сервера

const int box = 14; // пин реле коробок
const int paper = 12; // пин реле картона
int lastState_box = HIGH; // последнее сотояние пина коробок
int currentState_box; // текущее состояние пина коробок
unsigned long last_press_box; // время последнего изменения состояния пина коробок милисек
int lastState_paper = HIGH; // последнее состояние пина картона
int currentState_paper; // текущее стостояни пина картона
unsigned long last_press_paper; // время последнего изменения стостояния пина картона в милисек


void setup() {
  pinMode(box, INPUT_PULLUP); // режим работы пина + встроенный подтягивающий резистор
  pinMode(paper, INPUT_PULLUP);//
  Serial.begin(115200); // отладка в порт
  ETH.begin(); // запуск библ ETH
}

void loop() {
  currentState_box = digitalRead(box); // считываем состояние пинов
  currentState_paper = digitalRead(paper);
  if (lastState_box == LOW && currentState_box == HIGH && millis() - last_press_box > 2000){
    Serial.println("Hello box");
    count_box(host, port);
    last_press_box = millis();
  }
  if (lastState_paper == LOW && currentState_paper == HIGH && millis() - last_press_paper > 2000){
    Serial.println("Hello paper");
    count_paper(host, port);
    last_press_paper = millis();
  }


  
  lastState_box = currentState_box;
  lastState_paper = currentState_paper;
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


