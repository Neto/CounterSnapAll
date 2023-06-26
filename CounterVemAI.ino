
#include <Adafruit_GFX.h>    // Core graphics library
#include <Adafruit_TFTLCD.h> // Hardware-specific library
#include <Fonts/Org_01.h>
#include <Fonts/FreeSansBold12pt7b.h>

//Definicao de cores
#define BLACK           0x0000
#define BLUE            0x001F
#define RED             0xF800
#define GREEN           0x07E0
#define CYAN            0x07FF
#define MAGENTA         0xF81F
#define YELLOW          0xFFE0
#define WHITE           0xFFFF


//CS, CD, WR, RD, RESET
Adafruit_TFTLCD tft(A3, A2, A1, A0, A4);

int a = 35;

void setup() 
{
  Serial.begin(9600);
  tft.reset();
  tft.begin(0x9341);
  tft.setRotation(1);
  tft.fillScreen(BLACK);
  waitingForData();
}

void loop() {
    static char buffer[250];
    static size_t pos = 0; 

    if (Serial.available()) {
        char c = Serial.read();
        if (c != '>') {
            if (pos < sizeof(buffer) - 1) {
                buffer[pos++] = c;
            } else {
                pos = 0;  // reset buffer if it's full
            }
        } else {
            buffer[pos] = '\0'; // terminate the string

            // refresh display
            tft.fillScreen(BLACK);
            displayHeader();
            buffer[pos] = '\0'; // terminate the string
            displayText(buffer);

            pos = 0; // reset to start of buffer
        }
    }
}

void displayHeader() {
    tft.setFont(&FreeSansBold12pt7b); // Set the new font here
    tft.setTextColor(YELLOW);
    tft.setTextSize(1);
    tft.setCursor(0, 20);
    tft.println("VEMAI EARNINGS");
}

void displayText(char buffer[]) {
    tft.setFont(&FreeSansBold12pt7b); // Set the new font here
    tft.setTextColor(WHITE);
    tft.setTextSize(1);
    tft.setCursor(0, a++);
    tft.println(buffer);
}

void waitingForData()
{
   tft.setFont(&FreeSansBold12pt7b); // Set the new font here
   tft.setTextColor(YELLOW);
   tft.setTextSize(1);
   tft.setCursor(20,120);    
   tft.println("VEMAI EARNINGS");  
}
