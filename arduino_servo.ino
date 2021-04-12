#include <Servo.h>
#define maxRange 6000
Servo servo;

int pos = 0;
int posDir = 0;
unsigned long lastMillis;

inline int getPos() {
    return pos + posDir * (millis() - lastMillis);
}

inline void lock() {
    pos = getPos();
    lastMillis = millis();
    posDir = -1;
    servo.write(0);
}

inline void unlock() {
    pos = getPos();
    lastMillis = millis();
    posDir = 1;
    servo.write(180);
}

inline void halt() {
    pos = getPos();
    posDir = 0;
    servo.write(90);
}

void setup() {
  Serial.begin(9600);
  servo.attach(9);
  servo.write(0);
  delay(maxRange);
  servo.write(90);
}

void loop() {
  if (getPos() <= 0 && posDir == -1 || getPos() >= maxRange && posDir == 1) {
    halt();
  }
  if (Serial.available() > 0) {
    int i = Serial.parseInt();
    switch (i) {
        case 1:
            lock();
            break;
        case 2:
            unlock();
            break;
        case 3:
            halt();
            break;
    }
  }
}

