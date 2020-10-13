import serial
import time

def establishConnection():

    #On this computer I am using COM5 you need to check your computer to see what port you are using and change it in the next line.
    #Instructions on how to do this have been outlined in the read me. The baudrate is set on the DL-RS1A device please do not change it.
    serialPort = serial.Serial(port = "COM5", baudrate=38400,bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
    serialPort.flushInput()
    return serialPort

def prompUserSetDelay(delay, defaultRate):
    print("Preparing lasers for reading...")
    time.sleep(1)
    print("Lasers are now reading!")

    sampleRate = int(input("Input samples per second. (Max 100hz): "))

    if(sampleRate > 100 or sampleRate < 1):
        print("Improper sample rate. Using default sample rate of: "+str(defaultRate))
        sleep(0.5)
        sampleRate = (1/defaultRate)-delay
    else:
        sampleRate = (1/sampleRate)-delay

    return sampleRate

def zeroLasers(serialPort):
    print("Performing zeroshift on lasers...")
    serialPort.write(b'aw,001,0\r\n')
    time.sleep(1)
    serialPort.write(b'aw,001,1\r\n')
    time.sleep(1)
    serialPort.read(serialPort.in_waiting or 1)
