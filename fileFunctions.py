def writeHeaderLines(file, length):
    message = "SampleNumber"

    for itr in range(1,length):
        message += ",Laser "+str(itr)

    file.write(message)
    file.write("\n")

def writeSensorValues(file, returnStrings):

    for itr in range(0, len(returnStrings)):

        writeMessage = str(itr + 1)

        #Removing the '+' character to allow it to go into csv file properly.
        returnStrings[itr] = returnStrings[itr].replace("+","")
        returnStrings[itr] = returnStrings[itr].replace("\\r\\n\'","")
        tempString = returnStrings[itr].split(',')

        for itr2 in range(1,len(tempString)):
            writeMessage += "," + str(tempString[itr2])

        file.write(writeMessage)
        file.write("\n")
