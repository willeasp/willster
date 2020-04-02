from selenium import webdriver
import time

class GurkBot:
    def __init__ (self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://gurka.se/")
        time.sleep(2)
        
        
    def klickaForever(self):
        while True:
            self.driver.find_element_by_xpath("/html/body/div")\
            .click() 

myGurk = GurkBot()
myGurk.klickaForever()