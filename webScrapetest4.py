from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import re
import os
import pyautogui
import time
import runpy
import datetime
from datetime import date

pyautogui.PAUSE = .35


onLaunchX = 960
onLaunchY = 600

onLaunch = (onLaunchX,onLaunchY)


PATH = "C:\ProgramData\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.set_window_size(1024, 600)
driver.maximize_window()

print ("HERE")

driver.get("https://predict.sondehub.org/")
print (driver.title)
print (driver.find_element_by_id("cursor_pred_landrange"))


dt = date.today() + datetime.timedelta(days = 4)




lat     = driver.find_element_by_id("lat")
lon     = driver.find_element_by_id("lon")
alt     = driver.find_element_by_id("initial_alt")




lat.clear()
lat.send_keys("34.0592")

lon.clear()
lon.send_keys("-117.8213")

alt.clear()
alt.send_keys("230")


#selecting date 7 days from this instant in time

mSel    = Select(driver.find_element_by_id("month"))
day     = driver.find_element_by_id("day")
year    = driver.find_element_by_id("year")

mSel.select_by_value(str(dt.month))
day.clear()
day.send_keys(str(dt.day))
year.clear()
year.send_keys(str(dt.year))

launchTime = driver.find_element_by_id("hour")
launchTime.clear()
launchTime.send_keys("18")
launchTime = driver.find_element_by_id("min")
launchTime.clear()
launchTime.send_keys('00')

drag = driver.find_element_by_id("drag")
drag.clear()
drag.send_keys("8")

#giving values for burst calc

burstCalc       = driver.find_element_by_id("burst-calc-show")
burstCalc.click()

payMass         = driver.find_element_by_id("mp")
payMass.clear()
payMass.send_keys("3700")

ascent          = driver.find_element_by_id("tar")
ascent.clear()
ascent.send_keys("5")

balSel    = Select(driver.find_element_by_id("mb"))
balSel.select_by_value("h1600")


burstAlt        = driver.find_element_by_id("tba")
burstAlt.clear()

bUse         = driver.find_element_by_id("burst-calc-use")
bUse.click()

bUsePRED         = driver.find_element_by_id("run_pred_btn")
bUsePRED.click()

time.sleep(2)

driver.find_element_by_id("showHideForm").click()
time.sleep(1)


bUsePan         = driver.find_element_by_id("panto")
bUsePan.click()

#pyautogui.moveTo(onLaunch)#Moves the mouse to the coordinates of the image


# try:
    # element = WebDriverWait(driver, 10).until(
        # EC.presence_of_element_located((By.CLASS_NAME, 'leaflet-marker-icon leaflet-zoom-animated leaflet-interactive'))
    # #print(element.text)
    # )
# except:
    # driver.quit()


# launchMark = driver.find_element_by_id("map_canvas")
# print (launchMark.text)

launchLoc = driver.find_element_by_xpath('//*[@id="map_canvas"]/div[1]/div[4]/img[1]').location
landLoc = driver.find_element_by_xpath('//*[@id="map_canvas"]/div[1]/div[4]/img[2]').location

print (launchLoc)
launchLocX =  launchLoc['x']
launchLocY =  launchLoc['y']

landLocX = landLoc['x']
landLocY = landLoc['y']

scrollX = landLocX - launchLocX
scrollY = landLocY - launchLocY

scrollPt = (scrollX,scrollY)

print (launchLoc)
print (landLoc)
print (scrollPt)



origin = (262,290)
centerDist = (701,321)
pyautogui.moveTo(origin)
time.sleep(2)
pyautogui.move(centerDist)
pyautogui.move(scrollPt)
print (pyautogui.position())


pyautogui.scroll(1)
pyautogui.scroll(1)

time.sleep(2)
print(driver.current_url)

seeSim = driver.current_url

driver.save_screenshot('currSim.png')
driver.quit()

with open("Output.txt", "w") as text_file:
    text_file.write(seeSim)
    text_file.close()
