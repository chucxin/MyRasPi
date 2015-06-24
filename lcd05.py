from Adafruit_CharLCD import Adafruit_CharLCD
import time
import RPi.GPIO as GPIO

lcd = Adafruit_CharLCD()

lcd.begin(20, 4)

buttonUp = 11
buttonDown = 13
buttonEnter = 15
buttonBack = 37
Buzzer = 7

GPIO.setmode(GPIO.BOARD)

Button = [11, 13, 15, 37]
for x in Button:
    GPIO.setup(x, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(Buzzer, GPIO.OUT, initial=GPIO.LOW)    

time_stamp_0 = time.time()
time_stamp_1 = time.time()
time_stamp_2 = time.time()
time_stamp_3 = time.time()

screen = 0
arrow = 0
selected = 0
AHR = 0
AMIN =0
ASEC =0
Darrow=0
On=0





def display0Screen():
    lcd.setCursor(0,0)
    lcd.message(time.strftime("%Y-%m-%d %A", time.localtime(time.time())))
    lcd.setCursor(0,2)
    lcd.message(time.strftime("%H:%M:%S",time.localtime(time.time())))
    if On==1:
        lcd.setCursor(19,3)
        lcd.message("A")
    print "0 screen"
    print screen


def display1Screen():
    lcd.setCursor(3,0)
    lcd.message("Set alarm")
    lcd.setCursor(3,1)
    lcd.message("Turn off alarm")
    if arrow == 0:
        lcd.setCursor(0, 0)
        lcd.message("-->")
    if arrow == 1:
        lcd.setCursor(0,1)
        lcd.message("-->")
    print "1 screen"


def display2Screen():
    lcd.setCursor(3,0)
    lcd.message("HR   MIN   SEC")
    lcd.setCursor(3,2)
    if AHR < 10:
        lcd.message("0")
    lcd.message(str(AHR))
    lcd.setCursor(6,2)
    lcd.message(":")
    lcd.setCursor(8,2)
    if AMIN <10:
        lcd.message("0")
    lcd.message(str(AMIN))
    lcd.setCursor(12,2)
    lcd.message(":")
    lcd.setCursor(15,2)
    if ASEC <10:
        lcd.message("0")
    lcd.message(str(ASEC))
    if Darrow == 0:
        lcd.setCursor(2,2)
        lcd.message(">")
        lcd.setCursor(5,2)
        lcd.message("<")
    elif Darrow==1:
        lcd.setCursor(7,2)
        lcd.message(">")
        lcd.setCursor(10,2)
        lcd.message("<")
    elif Darrow==2:
        lcd.setCursor(14,2)
        lcd.message(">")
        lcd.setCursor(17,2)
        lcd.message("<")
def display3Screen():
    global screen
    lcd.setCursor(4,1)
    lcd.message("Alarm Set")
    time.sleep(1)
    lcd.clear()
    screen=0
def display4Screen():
    global screen
    lcd.setCursor(4,1)
    lcd.message("Alarm Off")
    time.sleep(1)
    lcd.clear()
    screen=0

 
def button():
    global AHR
    global AMIN
    global ASEC
    global time_stamp_0
    global time_stamp_1
    global time_stamp_2
    global time_stamp_3
    global screen
    global selected
    global arrow
    global Darrow
    global On
    if GPIO.input(buttonEnter) == False:
        time_now_0 = time.time()
        if (time_now_0 - time_stamp_0) >= 0.1:
            print "Enter"
            if screen==0:
                screen=1
            elif screen==1:
                if selected==0:
                    screen=2         
		elif selected==1:
		    screen=4
		    On=0
            elif screen==2:
                if Darrow==0:
                    Darrow=1
                elif Darrow==1:
                    Darrow=2
                elif Darrow==2:
                    screen=3
                    On=1
            lcd.clear()
            time_stamp_0 = time.time()
    elif GPIO.input(buttonBack) == False:
        time_now_1 = time.time()
        if (time_now_1 - time_stamp_1) >= 0.1:
            print "Back"
            if screen == 1:
                screen=0
            elif screen==2:
                if Darrow==0:
                    screen=1
                elif Darrow==1:
                    Darrow=0
                elif Darrow==2:
 		    Darrow=1
            lcd.clear()
    
            lcd.clear()
        time_stamp_1 = time.time()
    elif GPIO.input(buttonUp) == False:
        time_now_2 =time.time()
        if (time_now_2 - time_stamp_2) >=0.1:
            print "Up"
 	    if screen ==1:
                if arrow >0:
                    arrow=arrow - 1
                if selected >0:
                    selected=selected - 1    
	    elif screen==2:
                if Darrow==0:
                    if AHR<23:
                        AHR=AHR + 1
                    elif AHR ==23:
                        AHR=0      
                elif Darrow==1:
                    if AMIN<59:
                        AMIN=AMIN + 1
                    elif AMIN ==59:
                        AMIN=0
                elif Darrow==2:
                    if ASEC<59:
                        ASEC=ASEC + 1
                    elif ASEC ==59:
                        ASEC=0
            lcd.clear()       
        time_stamp_2 = time.time()
    elif GPIO.input(buttonDown) == False:
        time_now_3 = time.time()
        if (time_now_3 - time_stamp_3) >= 0.1:
            print "Down"
            if screen ==1:
                if arrow <1:
                    arrow=arrow + 1
                if selected <1:
 		    selected=selected + 1
            elif screen==2:
                if Darrow==0:
                    if AHR>0:
                        AHR=AHR -1 
                    elif AHR ==0:
                        AHR=23
                elif Darrow==1:
                    if AMIN>0:
                        AMIN=AMIN -1
                    elif AMIN ==0:
                        AMIN=59
                elif Darrow==2:
                    if ASEC>0:
                        ASEC=ASEC -1
                    elif ASEC ==0:
                        ASEC=59
            lcd.clear()
        time_stamp_3 = time.time()
def Alarm():
    global On
    HRN =int(time.strftime("%H",time.localtime(time.time())))
    MINN=int(time.strftime("%M",time.localtime(time.time())))
    SECN=int(time.strftime("%S",time.localtime(time.time())))
    if AHR==HRN and AMIN==MINN and ASEC==SECN and On==1:
        GPIO.output(Buzzer, GPIO.HIGH)
        print "alarm"
    print HRN, MINN, SECN, AHR, AMIN, ASEC    

while 1:
    Alarm()
    button()  
    if screen == 0:
        display0Screen()
    elif screen == 1:
        display1Screen()
    elif screen == 2:
        display2Screen()
    elif screen ==3:
        display3Screen()
    elif screen==4:
        display4Screen()


