# Code to generate sample text files for testing
infile1 = open("Fx.txt", 'w')
infile1.write("-19\n-42\n3\n5\n22\n-7\n-21\n-33\n-42")
infile1.close()

infile1 = open("Fy.txt", 'w')
infile1.write("24\n13\n45\n17\n18\n37\n13\n0\n35")
infile1.close()

infile1 = open("Fx2.txt", 'w')
infile1.write("-4.41\n25.17\n-29.20\n-50.21\n35.36\n47.7\n-11.43\n-47.41\n-19.6\n31.30\n-5.27")
infile1.close()

infile1 = open("Fy2.txt", 'w')
infile1.write("56.70\n21.58\n32.66\n65.55\n8.58\n48.19\n60.14\n80.54\n38.60\n100.82\n64.30")
infile1.close()

# Calculating R - The correlation coefficient of the data in Fx and Fy
def R(file1, file2):
    
    """This function calculates the correlation coefficient R for the x values stored in file1 and 
    the y values stored in file2"""
    
    import math
    
    #Generates a list of x values from a file containing x values
    infile1 = open(file1, "r")
    xList = []
    #Reads through each line of the file, stripping away the \n characters and converting the string to a float
    #then adding the remaining value to a list of x values.
    for line in infile1:
        tempString = line.strip("\n")
        tempFloat = float(tempString)
        xList.append(tempFloat)
    infile1.close()
    
    #Generates a list of y values form a file containing y values
    infile2 = open(file2, "r")
    yList = []
    #Reads through each line of the file, stripping away the \n characters and converting 
    #the string to a float then adding the remaining value to a list of y values.
    for line in infile2:
        tempString = line.strip("\n")
        tempFloat = float(tempString)
        yList.append(tempFloat)
    infile2.close()
    
    #Calculating a in equation
    sumOfXtimesY = 0
    numberOfDataPoints = (len(xList))
    #Finds the sum of all x*y values by using a loop to add the multiplication 
    #of an x value and its corresponding y value to a running total
    for i in range(numberOfDataPoints):
        sumOfXtimesY += xList[i]*yList[i]
    #Finds a by multiplying the sum of all x*y values and the number of data points
    a = numberOfDataPoints*sumOfXtimesY
    
    #Calculating b in equation
    sumX = 0
    sumY = 0
    #Calcluates the sum of all x values, as well as the sum of all y values by looping
    #through each value and adding it to a running total
    for i in range(numberOfDataPoints):
        sumX += xList[i]
        sumY += yList[i]
    #Finds b by multipling the sum of all x values by the sum of all y values
    b = sumX*sumY
    
    #Calculating c in equation
    sumXSquared = 0
    #Calculates the sum of all x^2 values by looping through each value, 
    #squaring it, then adding it to a running total
    for i in range(numberOfDataPoints):
        sumXSquared += (xList[i])**2
    #Finds c by square rooting the number of data points*sum of all x^2 values minus the sum of x values squared
    c = math.sqrt((numberOfDataPoints*sumXSquared) - (sumX**2))
    
    #Calculating d in equation
    sumYSquared = 0
    #Calculates the sum of all y^2 values by looping through each value, 
    #squaring it, then adding it to a running total
    for i in range(numberOfDataPoints):
        sumYSquared += (yList[i])**2
    #Finds d by square rooting the number of data points*sum of all y^2 values minus the sum of y values squared
    d = math.sqrt((numberOfDataPoints*sumYSquared) - (sumY**2))
    
    #Calculates R
    R = (a-b)/(c*d)
    
    return R
