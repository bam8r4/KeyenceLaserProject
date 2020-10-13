from laserFunctions import *
from fileFunctions import *

#Setting some default values for the user.
defaultDelay = 0.0005
defaultSampleRate = 50

#Creating a list to store all the responses from our serial unit and setting value for laser count.
returnStrings = []
laserCount = 0

#Opening serial port and flushing system.
serialPort = establishConnection()

#Zeroing out all lasers.
zeroLasers(serialPort)

#Getting our sample sampleRate
sampleRate = prompUserSetDelay(defaultDelay, defaultSampleRate)


try:
    while(True):
        #The sleeping is needed to allow the serial module time to process. M0 command returns reading from all amplifiers.
        serialPort.write(b'M0\r\n')
        time.sleep(sampleRate)
        response = serialPort.read(serialPort.in_waiting or 1)
        print(response)
        returnStrings.append(str(response))

except KeyboardInterrupt:
    print("Writing to file...")
    file = open("output.csv","w")

    #Next two lines only determine the number of lasers used and do not actually write to any files.
    laserSplit = returnStrings[0].split(',')
    laserCount = len(laserSplit)

    writeHeaderLines(file, laserCount)
    writeSensorValues(file, returnStrings)
    pass

serialPort.close()
file.close()
