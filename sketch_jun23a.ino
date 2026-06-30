int donjiMotorPulPin = 4;
int donjiMotorDirPin = 3;
int donjiMotorEnaPin = 2;
unsigned long vremeDonjiMotor = 0;
int donjiMotorBrojac = -1;

int desniMotorPulPin = 7;
int desniMotorDirPin = 6;
int desniMotorEnaPin = 5;
unsigned long vremeDesniMotor = 0;
int desniMotorBrojac = -1;

int leviMotorPulPin = 10;
int leviMotorDirPin = 9;
int leviMotorEnaPin = 8;
unsigned long vremeLeviMotor = 0;
int leviMotorBrojac = -1;

int prednjiMotorPulPin = 13;
int prednjiMotorDirPin = 12;
int prednjiMotorEnaPin = 11;
unsigned long vremePrednjiMotor = 0;
int prednjiMotorBrojac = -1;

int zadnjiMotorPulPin = A2;
int zadnjiMotorDirPin = A1;
int zadnjiMotorEnaPin = A0;
unsigned long vremeZadnjiMotor = 0;
int zadnjiMotorBrojac = -1;

String sledeciPotez = "";
String redosled = "";
int brojacSledecegPoteza = 0;
int brzina = 10;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  
  pinMode(donjiMotorEnaPin, OUTPUT);
  pinMode(donjiMotorDirPin, OUTPUT);
  pinMode(donjiMotorPulPin, OUTPUT);
  digitalWrite(donjiMotorEnaPin, HIGH);

  pinMode(desniMotorEnaPin, OUTPUT);
  pinMode(desniMotorDirPin, OUTPUT);
  pinMode(desniMotorPulPin, OUTPUT);
  digitalWrite(desniMotorEnaPin, HIGH);

  pinMode(leviMotorEnaPin, OUTPUT);
  pinMode(leviMotorDirPin, OUTPUT);
  pinMode(leviMotorPulPin, OUTPUT);
  digitalWrite(leviMotorEnaPin, HIGH);

  pinMode(prednjiMotorEnaPin, OUTPUT);
  pinMode(prednjiMotorDirPin, OUTPUT);
  pinMode(prednjiMotorPulPin, OUTPUT);
  digitalWrite(prednjiMotorEnaPin, HIGH);

  pinMode(zadnjiMotorEnaPin, OUTPUT);
  pinMode(zadnjiMotorDirPin, OUTPUT);
  pinMode(zadnjiMotorPulPin, OUTPUT);
  digitalWrite(zadnjiMotorEnaPin, HIGH);
}

void loop() {
  // put your main code here, to run repeatedly:
  citanje();
  Dfja(brzina);
  Rfja(brzina);
  Lfja(brzina);
  Ffja(brzina);
  Bfja(brzina);
}

void Dfja(int pauza){
  if(donjiMotorBrojac == -1 && sledeciPotez[0] == 'D'){
    donjiMotorBrojac++;
    digitalWrite(donjiMotorEnaPin, LOW);
    if(sledeciPotez == "D1"){
      digitalWrite(donjiMotorDirPin, HIGH);
    }
    else{
      digitalWrite(donjiMotorDirPin, LOW);
    }
  }
  else if(donjiMotorBrojac >= 0 && donjiMotorBrojac%2==0 && millis()-vremeDonjiMotor>=pauza){
    digitalWrite(donjiMotorPulPin, HIGH);
    donjiMotorBrojac++;
    vremeDonjiMotor = millis();
  }
  else if(donjiMotorBrojac >= 0 && donjiMotorBrojac%2==1 && millis()-vremeDonjiMotor>=pauza){
    digitalWrite(donjiMotorPulPin, LOW);
    donjiMotorBrojac++;
    vremeDonjiMotor = millis();
  }
  if(donjiMotorBrojac == 200){
    donjiMotorBrojac = -1;
    digitalWrite(donjiMotorEnaPin, HIGH);
    pokreniSledeciPotez();
  }
}

void Rfja(int pauza){
  if(desniMotorBrojac == -1 && sledeciPotez[0] == 'R'){
    desniMotorBrojac++;
    digitalWrite(desniMotorEnaPin, LOW);
    if(sledeciPotez == "R1"){
      digitalWrite(desniMotorDirPin, HIGH);
    }
    else{
      digitalWrite(desniMotorDirPin, LOW);
    }
  }
  else if(desniMotorBrojac >= 0 && desniMotorBrojac%2==0 && millis()-vremeDesniMotor>=pauza){
    digitalWrite(desniMotorPulPin, HIGH);
    desniMotorBrojac++;
    vremeDesniMotor = millis();
  }
  else if(desniMotorBrojac >= 0 && desniMotorBrojac%2==1 && millis()-vremeDesniMotor>=pauza){
    digitalWrite(desniMotorPulPin, LOW);
    desniMotorBrojac++;
    vremeDesniMotor = millis();
  }
  if(desniMotorBrojac == 200){
    desniMotorBrojac = -1;
    digitalWrite(desniMotorEnaPin, HIGH);
    pokreniSledeciPotez();
  }
}

void Lfja(int pauza){
  if(leviMotorBrojac == -1 && sledeciPotez[0] == 'L'){
    leviMotorBrojac++;
    digitalWrite(leviMotorEnaPin, LOW);
    if(sledeciPotez == "L1"){
      digitalWrite(leviMotorDirPin, HIGH);
    }
    else{
      digitalWrite(leviMotorDirPin, LOW);
    }
  }
  else if(leviMotorBrojac >= 0 && leviMotorBrojac%2==0 && millis()-vremeLeviMotor>=pauza){
    digitalWrite(leviMotorPulPin, HIGH);
    leviMotorBrojac++;
    vremeLeviMotor = millis();
  }
  else if(leviMotorBrojac >= 0 && leviMotorBrojac%2==1 && millis()-vremeLeviMotor>=pauza){
    digitalWrite(leviMotorPulPin, LOW);
    leviMotorBrojac++;
    vremeLeviMotor = millis();
  }
  if(leviMotorBrojac == 200){
    leviMotorBrojac = -1;
    digitalWrite(leviMotorEnaPin, HIGH);
    pokreniSledeciPotez();
  }
}

void Ffja(int pauza){
  if(prednjiMotorBrojac == -1 && sledeciPotez[0] == 'F'){
    prednjiMotorBrojac++;
    digitalWrite(prednjiMotorEnaPin, LOW);
    if(sledeciPotez == "F1"){
      digitalWrite(prednjiMotorDirPin, HIGH);
    }
    else{
      digitalWrite(prednjiMotorDirPin, LOW);
    }
  }
  else if(prednjiMotorBrojac >= 0 && prednjiMotorBrojac%2==0 && millis()-vremePrednjiMotor>=pauza){
    digitalWrite(prednjiMotorPulPin, HIGH);
    prednjiMotorBrojac++;
    vremePrednjiMotor = millis();
  }
  else if(prednjiMotorBrojac >= 0 && prednjiMotorBrojac%2==1 && millis()-vremePrednjiMotor>=pauza){
    digitalWrite(prednjiMotorPulPin, LOW);
    prednjiMotorBrojac++;
    vremePrednjiMotor = millis();
  }
  if(prednjiMotorBrojac == 200){
    digitalWrite(prednjiMotorEnaPin, HIGH);
    prednjiMotorBrojac = -1;
    pokreniSledeciPotez();
  }
}

void Bfja(int pauza){
  if(zadnjiMotorBrojac == -1 && sledeciPotez[0] == 'B'){
    zadnjiMotorBrojac++;
    digitalWrite(zadnjiMotorEnaPin, LOW);
    if(sledeciPotez == "B1"){
      digitalWrite(zadnjiMotorDirPin, HIGH);
    }
    else{
      digitalWrite(zadnjiMotorDirPin, LOW);
    }
  }
  else if(zadnjiMotorBrojac >= 0 && zadnjiMotorBrojac%2==0 && millis()-vremeZadnjiMotor>=pauza){
    digitalWrite(zadnjiMotorPulPin, HIGH);
    zadnjiMotorBrojac++;
    vremeZadnjiMotor = millis();
  }
  else if(zadnjiMotorBrojac >= 0 && zadnjiMotorBrojac%2==1 && millis()-vremeZadnjiMotor>=pauza){
    digitalWrite(zadnjiMotorPulPin, LOW);
    zadnjiMotorBrojac++;
    vremeZadnjiMotor = millis();
  }
  if(zadnjiMotorBrojac == 200){
    zadnjiMotorBrojac = -1;
    digitalWrite(zadnjiMotorEnaPin, HIGH);
    pokreniSledeciPotez();
  }
}

void citanje(){
  if(sledeciPotez == "" && Serial.available() > 0){
      redosled = Serial.readStringUntil('\n');
      redosled.trim(); // Uklanja skrivene karaktere (\r) sa kraja
      brojacSledecegPoteza = 0;
      sledeciPotez = redosled.substring(brojacSledecegPoteza, brojacSledecegPoteza+2);
      brojacSledecegPoteza+=2;
  }
}

void pokreniSledeciPotez() {
  sledeciPotez = redosled.substring(brojacSledecegPoteza, brojacSledecegPoteza+2);
  brojacSledecegPoteza+=2;
  if(sledeciPotez == "TE"){
    brojacSledecegPoteza = 0;
    sledeciPotez = "";
    Serial.print("Izvrsio sam komandu: ");
    Serial.println(redosled);
  }
}
