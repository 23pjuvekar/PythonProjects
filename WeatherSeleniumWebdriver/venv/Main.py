from time import sleep
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import numpy as np
import tkinter
from tkinter import *
from tkmacosx import Button
import time
from datetime import datetime
import sys
from selenium.webdriver.chrome.options import Options

#Input location of selenium webdriver here
PATH = "/Users/ppjuvekar/sources/Coding/Code Extra/chromedriver"

# Selenium code for python
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(PATH, options=options)
sleep(1)

#Tick function
def tick():
    TimeDisplay = time.strftime("%H:%M:%S")
    TimeDisplayTK.config(text = TimeDisplay)
    TimeDisplayTK.after(200, tick)

#Date Function
def date():
    DateDisplay = datetime.today().strftime("%Y-%m-%d")
    DateDisplayTK.config(text = DateDisplay)
    DateDisplayTK.after(1000, date)

def day():
    DayDisplay = datetime.today().strftime("%A")
    DayDisplayTK.config(text = DayDisplay)
    DayDisplayTK.after(1000, day)

#Going to the basic website
def gotoweatherwebsite():
    driver.get("https://weather.com/")
    sleep(2)


#Takes in the location and give the information back
def Enter():
    city = CityInput.get("1.0","end")
    state = StateInput.get("1.0","end")
    # Don't input info into these variables

    gotoweatherwebsite()

    typesearch = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/header/div/div[2]/div[1]/div/div[1]/input")
    typesearch.send_keys(city + ", " + state)
    sleep(2)
    typesearch.send_keys(Keys.ENTER)
    sleep(2)

    # Collects elements from webpage
    weatherDataTableMorningTemp = driver.find_element_by_xpath("/html/body/div[1]/main/div[2]/div[2]/div[2]/section/div/ul/li[1]/a/div[1]")
    weatherDataTableMorningPercent = driver.find_element_by_xpath("/html/body/div[1]/main/div[2]/div[2]/div[2]/section/div/ul/li[1]/a/div[3]")
    weatherDataTableAfternoonTemp = driver.find_element_by_xpath("/html/body/div[1]/main/div[2]/div[2]/div[2]/section/div/ul/li[2]/a/div[1]")
    weatherDataTableAfternoonPercent = driver.find_element_by_xpath("/html/body/div[1]/main/div[2]/div[2]/div[2]/section/div/ul/li[2]/a/div[3]")
    weatherDataTableEveningTemp = driver.find_element_by_xpath("/html/body/div[1]/main/div[2]/div[2]/div[2]/section/div/ul/li[3]/a/div[1]")
    weatherDataTableEveningPercent = driver.find_element_by_xpath("/html/body/div[1]/main/div[2]/div[2]/div[2]/section/div/ul/li[3]/a/div[3]")
    weatherDataTableNightTemp = driver.find_element_by_xpath("/html/body/div[1]/main/div[2]/div[2]/div[2]/section/div/ul/li[4]/a/div[1]")
    weatherDataTableNightPercent = driver.find_element_by_xpath("/html/body/div[1]/main/div[2]/div[2]/div[2]/section/div/ul/li[4]/a/div[3]")

    # Converts web elements to variables
    MorningTemperature = weatherDataTableMorningTemp.text
    MorningPercent = weatherDataTableMorningPercent.text
    AfternoonTemperature = weatherDataTableAfternoonTemp.text
    AfternoonPercent = weatherDataTableAfternoonPercent.text
    EveningTemperature = weatherDataTableEveningTemp.text
    EveningPercent = weatherDataTableEveningPercent.text
    NightTemperature = weatherDataTableNightTemp.text
    NightPercent = weatherDataTableNightPercent.text

    #Updates new weather values
    MorningTempDisplay.config(text = MorningTemperature)
    MorningRainPercentDisplay.config(text = MorningPercent)
    AfternoonWeatherDisplay.config(text = AfternoonTemperature)
    AfternoonPercentDisplay.config(text = AfternoonPercent)
    EveningWeatherDisplay.config(text = EveningTemperature)
    EveningPercentDisplay.config(text = EveningPercent)
    NightWeatherDisplay.config(text = NightTemperature)
    NightPercentDisplay.config(text = NightPercent)



# Main code

window = tkinter.Tk()
window.configure(background = "black")


AppName = tkinter.Label(
    text = "Weather",
    fg = "white",
    bg = "black",
    width = "10",
    height = "3",
).grid(row = 0, column = 0)


RefreshButton = Button(
    text = "Enter",
    bg = "black",
    fg = "white",
    activebackground = "black",
    activeforeground = "green",
    width = 96,
    height = 53
)
RefreshButton.grid(row = 0, column = 1)
RefreshButton.config(command = Enter)

TimeDisplayTK = tkinter.Label(
    text = "",
    fg = "white",
    bg = "black",
    width = "10",
    height = "3",
)
TimeDisplayTK.grid(row = 0, column = 3)

Blankspace2 = tkinter.Label(
    text = "Time:",
    fg = "white",
    bg = "black",
    width = "10",
    height = "3",
).grid(row = 0, column = 2)

State = tkinter.Label(
    text = "State:",
    fg = "white",
    bg = "black",
    width =" 10",
    height = "3",
).grid(row = 1, column = 0)

StateInput = tkinter.Text(
    fg = "white",
    bg = "black",
    width = "11",
    height = "3",
    highlightbackground = "white",
    highlightthickness = "1",
    font=("flat", 12),
)
StateInput.grid(row = 1, column = 1)
Date = tkinter.Label(
    text = "Date:",
    fg = "white",
    bg = "black",
    width = "10",
    height = "3",
).grid(row = 1, column = 2)

DateDisplayTK = tkinter.Label(
    text = "",
    fg = "white",
    bg = "black",
    width = "10",
    height = "3",
)
DateDisplayTK.grid(row = 1, column = 3)

Day = tkinter.Label(
    text = "Day:",
    fg = "white",
    bg = "black",
    width = "10",
    height = "3",
).grid(row = 2, column = 2)

DayDisplayTK = tkinter.Label(
    text = "",
    fg = "white",
    bg = "black",
    width = "10",
    height = "3",
)
DayDisplayTK.grid(row = 2, column = 3)

City = tkinter.Label(
    text = "City:",
    fg = "white",
    bg = "black",
    width = "10",
    height = "3",
).grid(row = 2, column = 0)


CityInput = tkinter.Text(
    fg = "white",
    bg = "black",
    width = "11",
    height = "3",
    highlightbackground = "white",
    highlightthickness = "1",
    font=("flat", 12),
)
CityInput.grid(row = 2, column = 1)

MorningTextDisplay = tkinter.Label(
    text="Morning",
    fg="white",
    bg="black",
    width="10",
    height="3",
).grid(row = 3, column = 0)

MorningTempDisplay = tkinter.Label(
    text = "",
    fg = "white",
    bg = "black",
    width = "10",
    height = "5",
)
MorningTempDisplay.grid(row = 4, column = 0)

MorningRainPercentDisplay = tkinter.Label(
    text= "",
    fg="white",
    bg="black",
    width="10",
    height="5",
)
MorningRainPercentDisplay.grid(row = 5, column = 0)

AfternoonTextDisplay = tkinter.Label(
    text="Afternoon",
    fg="white",
    bg="black",
    width="10",
    height="3",
).grid(row = 3, column = 1)

AfternoonWeatherDisplay = tkinter.Label(
    text="",
    fg="white",
    bg="black",
    width="10",
    height="5",
)
AfternoonWeatherDisplay.grid(row = 4, column = 1)

AfternoonPercentDisplay = tkinter.Label(
    text="",
    fg="white",
    bg="black",
    width="10",
    height="5",
)
AfternoonPercentDisplay.grid(row = 5, column = 1 )

EveningTextDisplay = tkinter.Label(
    text="Evening",
    fg="white",
    bg="black",
    width="10",
    height="3",
).grid(row = 3, column = 2)

EveningWeatherDisplay = tkinter.Label(
    text="",
    fg="white",
    bg="black",
    width="10",
    height="5",
)
EveningWeatherDisplay.grid(row = 4, column = 2)

EveningPercentDisplay = tkinter.Label(
    text="",
    fg="white",
    bg="black",
    width="10",
    height="5",
)
EveningPercentDisplay.grid(row = 5, column = 2)

NightTextDisplay = tkinter.Label(
    text="Night",
    fg="white",
    bg="black",
    width="10",
    height="3",
).grid(row = 3, column = 3)

NightWeatherDisplay = tkinter.Label(
    text="",
    fg="white",
    bg="black",
    width="10",
    height="5",
)
NightWeatherDisplay.grid(row = 4, column = 3)

NightPercentDisplay = tkinter.Label(
    text="",
    fg="white",
    bg="black",
    width="10",
    height="5",
)
NightPercentDisplay.grid(row = 5, column = 3)

tick()
date()
day()

tkinter.mainloop()

