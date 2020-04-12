#!/usr/bin/env python3


from selenium import webdriver
import time

class InstaBot:
    def __init__ (self, username, pw):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.instagram.com/?hl=sv")
        self.username = username
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pw)
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]")\
            .click()
        time.sleep(2)
        self.driver.refresh()
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Inte nu')]")\
            .click()
        time.sleep(1)
          

    def followPeople(self):
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]")\
            .click()  
        time.sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/h2/a")\
            .click() 
        time.sleep(1)           
        while True:
            pbox = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[2]")
            buttons = pbox.find_elements_by_tag_name('button')
            for button in buttons:
                button.click()
                time.sleep(2)
            print("done")
            time.sleep(1)
            self.driver.refresh()
            time.sleep(3)
            




bot = InstaBot('billy_eyelash_v1.0', 'kaWasaki99')
bot.followPeople()