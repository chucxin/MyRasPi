from Adafruit_CharLCD import Adafruit_CharLCD
import time
import RPi.GPIO as GPIO
import pygame.mixer


# music
pygame.mixer.init()

Music= pygame.mixer.Sound("")
MusicList = ["Ylvis- What The Fox Say- Lyrics.wav", "David Bowie Starman Lyrics.wav", "Queen - 'Bohemian Rhapsody'.wav"]

AlarmMusicList= [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]



# LCD
lcd = Adafruit_CharLCD()
lcd.begin(20, 4)

# Buttons
buttonUp = 11
buttonDown = 13
buttonEnter = 15
buttonBack = 37

GPIO.setmode(GPIO.BOARD)

Button = [buttonUp, buttonDown, buttonEnter, buttonBack]
for x in Button:
    GPIO.setup(x, GPIO.IN, GPIO.PUD_UP)

time_stamp_0 = time.time()
time_stamp_1 = time.time()
time_stamp_2 = time.time()
time_stamp_3 = time.time()

#
screen = 0
arrow = 0
selected = 0
Aselected =0

AHR = [0,0,0,0,0,0,0,0,0,0]
AMIN =[0,0,0,0,0,0,0,0,0,0]
ASEC =[0,0,0,0,0,0,0,0,0,0]
Darrow=0 
AArrow = 0
On=[0,0,0,0,0,0,0,0,0,0]
Sound=0
Scroll=0
LastSound=time.time()

# get data from files
for x in range(10):
    myfile=open("Alarm"+str(x)+".al", "r")
    fl = myfile.readlines()
    On[x]=int(fl[0])
    AHR[x]=int(fl[1])
    AMIN[x]=int(fl[2])
    ASEC[x]=int(fl[3])
    AlarmMusicList[x]=int(fl[4])
    myfile.close()
 
#
def display0Screen():
    lcd.setCursor(0,0)
    lcd.message(time.strftime("%Y-%m-%d %A", time.localtime(time.time())))
    lcd.setCursor(0,2)
    lcd.message(time.strftime("%H:%M:%S",time.localtime(time.time())))
    for x in range(10):
        if On[x]==1:
            lcd.setCursor((0+x) * 2,3)
            lcd.message(str(x+1))
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
    lcd.setCursor(5,0)
    lcd.message("Alarm ")
    lcd.message(str(Aselected + 1))
    lcd.setCursor(3,1)
    lcd.message("HR   MIN   SEC")
    lcd.setCursor(3,2)
    if AHR[Aselected] < 10:
        lcd.message("0")
    lcd.message(str(AHR[Aselected]))
    lcd.setCursor(6,2)
    lcd.message(":")
    lcd.setCursor(8,2)
    if AMIN[Aselected] <10:
        lcd.message("0")
    lcd.message(str(AMIN[Aselected]))
    lcd.setCursor(12,2)
    lcd.message(":")
    lcd.setCursor(15,2)
    if ASEC[Aselected] <10:
        lcd.message("0")
    lcd.message(str(ASEC[Aselected]))
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
def display5Screen():
    lcd.setCursor(3,0)
    lcd.message("Alarm!")
    lcd.setCursor(3,2)
    lcd.message(time.strftime("%H:%M:%S", time.localtime(time.time())))
def display6Screen():
    for x in range(0, 4):   
        lcd.setCursor(3,x)
        lcd.message("Alarm ")
        lcd.message(str(x + Scroll+ 1))
        lcd.setCursor(11,x)
        lcd.message("(")
        if AHR[x+Scroll] < 10:
            lcd.message("0")
        lcd.message(str(AHR[x + Scroll]))
        lcd.message(":")
        if AMIN[x+Scroll] < 10:
            lcd.message("0")
        lcd.message(str(AMIN[x + Scroll]))
        lcd.message(")")
        if On[x+Scroll]==1:
            lcd.setCursor(19,x)
            lcd.message("A")
    lcd.setCursor(0,AArrow)
    lcd.message("-->")    
def display7Screen():
    for x in range(0, 4):
        lcd.setCursor(2,x)
        lcd.message("Alarm Off")
        lcd.message(str(x + Scroll+ 1))
        lcd.setCursor(13,x)
        lcd.message("(")
        if AHR[x+Scroll] < 10:
            lcd.message("0")
        lcd.message(str(AHR[x + Scroll]))
        lcd.message(":")
        if AMIN[x+Scroll] < 10:
            lcd.message("0")
        lcd.message(str(AMIN[x + Scroll]))
        lcd.message(")")
    lcd.setCursor(0,AArrow)
    lcd.message("->")
def display8Screen():
    lcd.setCursor(4,0)
    lcd.message("<Music List>")
    lcd.setCursor(3,1)
    lcd.message("What the Fox Say")
    lcd.setCursor(3,2)
    lcd.message("Starman")
    lcd.setCursor(3,3)
    lcd.message("Bohemian Rhapsody")
    lcd.setCursor(0,AArrow)
    lcd.message("-->")

 
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
    global Sound
    global AArrow
    global Scroll
    global Aselected
    # ENTER
    if GPIO.input(buttonEnter) == False:
        time_now_0 = time.time()
        if (time_now_0 - time_stamp_0) >= 0.13:
            print "Enter"
            if screen==0:
                screen=1
                selected=0
                arrow= 0
            elif screen==1:
		# set alarm
                if selected==0:
                    screen=6
                    Darrow=0
                    Aselected=0
                    Scroll = 0
                    AArrow = 0
		# turn off alarm         
		elif selected==1:
		    screen=7
		    Aselected=0
                    Scroll = 0
                    AArrow = 0

            elif screen==2: # set alarm
                if Darrow==0:
                    Darrow=1
                elif Darrow==1:
                    Darrow=2
                elif Darrow==2:
                    screen=8
                    AArrow = AlarmMusicList[Aselected] + 1
            elif screen ==8: # select music
                On[Aselected]=1
                myfile = open("Alarm"+str(Aselected)+".al","w")
                myfile.write(str(On[Aselected])+"\n")
                myfile.write(str(AHR[Aselected])+"\n")
                myfile.write(str(AMIN[Aselected])+"\n")
                myfile.write(str(ASEC[Aselected])+"\n")
                myfile.write(str(AlarmMusicList[Aselected])+"\n")
                myfile.close()    
                screen=0 
            elif screen==5:
                screen=0
                Sound=0

            elif screen == 6: # select alarm
                screen=2

            elif screen==7: # turn off alarm
                On[Aselected]=0
                myfile = open("Alarm"+str(Aselected)+".al","w")
                myfile.write(str(On[Aselected])+"\n")
                myfile.write(str(AHR[Aselected])+"\n")
                myfile.write(str(AMIN[Aselected])+"\n")
                myfile.write(str(ASEC[Aselected])+"\n")
                myfile.write(str(AlarmMusicList[Aselected])+"\n")
                myfile.close()
                screen=4
            lcd.clear()
            time_stamp_0 = time.time()
    # Back
    elif GPIO.input(buttonBack) == False:
        time_now_1 = time.time()
        if (time_now_1 - time_stamp_1) >= 0.13:
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
            elif screen==5:
                screen=0
                Sound=0
            elif screen==6:
                screen=1
            elif screen == 7:
                screen = 1
            elif screen ==8:
                screen=2
            lcd.clear()
        time_stamp_1 = time.time()
    elif GPIO.input(buttonUp) == False:
        time_now_2 =time.time()
        if (time_now_2 - time_stamp_2) >=0.13:
            print "Up"
 	    if screen ==1:
                if arrow >0:
                    arrow=arrow - 1
                if selected >0:
                    selected=selected - 1    
	    elif screen==2:
                if Darrow==0:
                    if AHR[Aselected]<23:
                        AHR[Aselected]=AHR[Aselected] + 1
                    elif AHR[Aselected] ==23:
                        AHR[Aselected]=0      
                elif Darrow==1:
                    if AMIN[Aselected]<59:
                        AMIN[Aselected]=AMIN[Aselected] + 1
                    elif AMIN[Aselected] ==59:
                        AMIN[Aselected]=0
                elif Darrow==2:
                    if ASEC[Aselected]<59:
                        ASEC[Aselected]=ASEC[Aselected] + 1
                    elif ASEC[Aselected] ==59:
                        ASEC[Aselected]=0
            elif screen==6:
                if Scroll>0 and AArrow ==0:
                    Scroll=Scroll -1
                if AArrow>0:
                    AArrow = AArrow -1
                if Aselected>0:
                    Aselected=Aselected -1
                print Aselected
            elif screen==7:
                if Scroll>0 and AArrow ==0:
                    Scroll=Scroll -1
                if AArrow>0:
                    AArrow = AArrow -1
                if Aselected>0:
                    Aselected=Aselected -1
                print Aselected
            elif screen==8:
                if AArrow>1:
                    AArrow = AArrow -1
                if AlarmMusicList[Aselected] >0:
                    AlarmMusicList[Aselected]=AlarmMusicList[Aselected]-1

            lcd.clear()       
        time_stamp_2 = time.time()
    # Down
    elif GPIO.input(buttonDown) == False:
        time_now_3 = time.time()
        if (time_now_3 - time_stamp_3) >= 0.13:
            print "Down"
            if screen ==1:
                if arrow <1:
                    arrow=arrow + 1
                if selected <1:
 		    selected=selected + 1
            elif screen==2:
                if Darrow==0:
                    if AHR[Aselected]>0:
                        AHR[Aselected]=AHR[Aselected] -1 
                    elif AHR[Aselected] ==0:
                        AHR[Aselected]=23
                elif Darrow==1:
                    if AMIN[Aselected]>0:
                        AMIN[Aselected]=AMIN[Aselected] -1
                    elif AMIN[Aselected] ==0:
                        AMIN[Aselected]=59
                elif Darrow==2:
                    if ASEC[Aselected]>0:
                        ASEC[Aselected]=ASEC[Aselected] -1
                    elif ASEC[Aselected] ==0:
                        ASEC[Aselected]=59
            elif screen ==6:
                if Scroll<6 and AArrow ==3:
                    Scroll=Scroll +1
                if AArrow<3:
                    AArrow = AArrow +1
                if Aselected<9:
                    Aselected = Aselected +1
            elif screen==7:
                if Scroll<6 and AArrow ==3:
                    Scroll=Scroll +1
                if AArrow<3:
                    AArrow = AArrow +1
                if Aselected<9:
                    Aselected = Aselected +1
            elif screen==8:
                if AArrow<3:
                    AArrow = AArrow +1
                if AlarmMusicList[Aselected]< 2:
                    AlarmMusicList[Aselected]=AlarmMusicList[Aselected]+1
            lcd.clear()

        time_stamp_3 = time.time()




ifplayed = 0

def Alarm():
    global On
    global Sound
    global screen
    global LastSound
    global Nowtime
    global Music
    global ifplayed

    HRN =int(time.strftime("%H",time.localtime(time.time())))
    MINN=int(time.strftime("%M",time.localtime(time.time())))
    SECN=int(time.strftime("%S",time.localtime(time.time())))
    for x in range(10):
        if AHR[x]==HRN and AMIN[x]==MINN and ASEC[x]==SECN and On[x]==1:
            Sound = 1
            Music= pygame.mixer.Sound(MusicList[AlarmMusicList[x]])
            Nowtime=time.time()
            lcd.clear()
            print "music:", MusicList[AlarmMusicList[x]]
    if Sound==1:
        if ifplayed == 0:
            Music.play()
            ifplayed = 1          
        screen=5 
        if time.time()-Nowtime > 60:
            Sound=0
            lcd.clear()
            screen=0
    elif Sound==0:
         ifplayed = 0       
         pygame.mixer.stop()

    print HRN, MINN, SECN, AHR, AMIN, ASEC, Sound, ifplayed





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
    elif screen==5:
        display5Screen()
    elif screen==6:
        display6Screen()
    elif screen==7:
        display7Screen()
    elif screen==8:
        display8Screen()

