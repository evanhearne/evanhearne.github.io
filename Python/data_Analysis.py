# Manual working of graphing and statistic analysis
import matplotlib.pyplot as plt
import csv

# Imports packages needed for file selection
import tkinter as tk
from tkinter import filedialog

# Greets the user
print('Hello, and welcome to the Data Analysis Program!')
name = input('And who do I have the pleasure of chatting to? (please enter name, followed by Enter) ')
print('Hello,', name + '.', 'A pleasure to meet you.')
y_n = input('I need help with finding data to analyse for you. Can you help me locate this data? (please enter yes or no, followed by Enter) ')

i = 0

# Handles user decisions
while i == 0:
    if y_n == "yes":
        i = i + 1
        print("Thank you. A pie chart has been generated to assist you in understanding the data given. '< 2 metres' means when no social distancing took place, and '> 2 metres' means when social distancing did take place. To access the pie chart, please click on the 'Python' window. After looking at the analysis, a text based analysis will appear upon closing the graph.")
    elif y_n == "no":
        print("I am sorry I could not help you today. If you change your mind, please run the program again, and I will be happy to assist you.")
        break
    else:
        y_n = input("Silly me! It must be my circuits or something, but I didn't quite catch that. Could you type yes or no again, please? ")

if i == 1:
    # Sets up file open GUI
    root = tk.Tk()
    root.withdraw()
    
    # Finds the csv file
    filePath = filedialog.askopenfilename()
    
    # Opens and closes csv file, uses csv as list
    file = open(filePath,"r")
    rawData = list(csv.reader(file))
    file.close()

    # Removes unwanted data
    rawData.pop(0)
    rawData.pop(0)

    # Converts list to string
    rawData = str(rawData)

    # Removes unwanted characters from string
    rawData = rawData.replace("[", "")
    rawData = rawData.replace("]", "")
    rawData = rawData.replace("t", "")
    rawData = rawData.replace("\\", ",")
    rawData = rawData.replace("'","")

    # Separates the data
    rawData = rawData.split(",")

    # Puts sorted data into new list
    cleanData = [float(item) for item in rawData]

    # Creates new lists for storing specifc data
    moreThanTwoMetres = []
    lessThanTwoMetres = []

    # Puts items into their list accordingly
    for item in cleanData:
        if item < -60:
            moreThanTwoMetres.append(item)
        if item > -60 and item < 0:
            lessThanTwoMetres.append(item)

    # Assigns values to new variables for use with Pie Chart
    percentageMoreThanTwoMetres = float((len(moreThanTwoMetres) / len(cleanData)) * 100)
    percentageLessThanTwoMetres = float((len(lessThanTwoMetres) / len(cleanData)) * 100)
    
    # Sets up variables to be used for Pie Chart
    labels = '> 2 metres', '< 2 metres'
    sizes = [percentageMoreThanTwoMetres, percentageLessThanTwoMetres]
    explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

    # Sets up information for Pie Chart
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Displays Pie Chart
    plt.show()
    
    # Tells user about the report
    print("Thank You. According to the file you have submitted, when the devices were in use, social distancing was maintained around", str(percentageMoreThanTwoMetres * 2) + "%", "of the time and social distancing was not maintained around", str(percentageLessThanTwoMetres * 2) + "%", "of the time.")
    print("I am delighted to have assisted you today. If you need my help with analysing another file, please run the program again and I will be more than happy to help.")
