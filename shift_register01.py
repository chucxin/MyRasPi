import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

SERpin = 16
RCLKpin = 18
SRCLKpin = 22

registers = [0,0,0,0,0,0,0,0]

GPIO.setup(SERpin, GPIO.OUT)
GPIO.setup(RCLKpin, GPIO.OUT)
GPIO.setup(SRCLKpin, GPIO.OUT)

def clearRegister():
    global registers
    for i in range(len(registers)):
        registers[i] = 0

def writeRegisters():
    GPIO.output(RCLKpin, GPIO.LOW)

    for i in reversed(registers):
        GPIO.output(SRCLKpin, GPIO.LOW)

        GPIO.output(SERpin, i)
        GPIO.output(SRCLKpin, GPIO.HIGH)

    GPIO.output(RCLKpin, GPIO.HIGH)

def setRegisterPin(index, val):
    global registers
    registers[index] = val


while 1:
    clearRegister()
    setRegisterPin(0, 1)
    setRegisterPin(1, 0)
    setRegisterPin(6, 0)
    setRegisterPin(7, 1)

    writeRegisters()

