
#include <ETH.h>

char* host = "10.33.1.147";
uint16_t port = 5837;
const int led = 15;
const int box = 14;
const int paper = 12;
int lastState_box = HIGH;
int currentState_box;
unsigned long last_press_box;
int lastState_paper = HIGH;
int currentState_paper;
unsigned long last_press_paper;


void setup() {
  pinMode(box, INPUT_PULLUP);
  pinMode(paper, INPUT_PULLUP);
  Serial.begin(115200);
  ETH.begin();
}

void loop() {
  currentState_box = digitalRead(box);
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


