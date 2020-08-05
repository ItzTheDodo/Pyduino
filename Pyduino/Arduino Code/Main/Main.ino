/*
 * Pyduino Sketch v1.0
 * By: ItzTheDodo
 * Credits: https://github.com/lekum/pyduino/blob/master/pyduino_sketch.ino
 * 
 * Commands:
 * AR:pin
 * DR:pin
 * AW:pin:data
 * DW:pin:data
 * M:pin:data
 * 
 */

int digital_value;
int analog_value;
String operation;
String pin;
String op;

void set_pin_mode(int pin_number, String mode){
  if (mode == "I"){
    pinMode(pin_number, INPUT);
  }
  if (mode == "O"){
    pinMode(pin_number, OUTPUT);
  }
  if (mode == "P"){
    pinMode(pin_number, INPUT_PULLUP);
  }

}

void digital_read(int pin_number){

  digital_value = digitalRead(pin_number);
  Serial.print('D');
  Serial.print(pin_number);
  Serial.print(':');
  Serial.println(digital_value);
}

void analog_read(int pin_number){

  analog_value = analogRead(pin_number);
  Serial.print('A');
  Serial.print(pin_number);
  Serial.print(':');
  Serial.println(analog_value);
}

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(100);
}

void loop() {

  if (Serial.available() > 0) {
    operation = Serial.read();
    int a = operation.indexOf(":");
    String li[3] = {operation.substring(0, a - 1), operation.substring(a + 1)};
    pin = li[1];
    op = li[0];

    if (op == "AR"){
      analog_read(pin.toInt());
    }
    if (op == "DR"){
      digital_read(pin.toInt());
    }
    if (op == "DW"){
      a = pin.indexOf(":");
      String lid[3] = {pin.substring(0, a - 1), pin.substring(a + 1)};
      pin = lid[0];
      String dv = lid[1];
      digitalWrite(pin.toInt(), dv.toInt());
    }
    if (op == "AW"){
      a = pin.indexOf(":");
      String lia[3] = {pin.substring(0, a - 1), pin.substring(a + 1)};
      pin = lia[0];
      String av = lia[1];
      digitalWrite(pin.toInt(), av.toInt());
    }
    if (op == "M") {
      a = pin.indexOf(":");
      String lia[3] = {pin.substring(0, a - 1), pin.substring(a + 1)};
      pin = lia[0];
      String mode = lia[1];
      set_pin_mode(pin.toInt(), mode);
    }
    
  }

}
