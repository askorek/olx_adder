# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from time import sleep
#from selenium.webdriver import Select

class Advertisement:
    def set_title(self, title):
        self.title = title
    def set_description(self, description_file):
        self.description_file = description_file
        with open(self.description_file) as f:
            self.description = f.readlines()
    def set_price(self, price):
        self.price = str(price)
    def set_city(self, city):
        self.city = city
    def set_topic(self,topic):
        self.topic = topic
    def add_image(self, image):
        self.image = image

class olxAutomater:
    
    def __init__(self):
        self.driver = webdriver.Firefox()      
        self.driver.set_page_load_timeout(35)

    def setUP(self):
        self.logged_in = False
        self.login = "krk.korki@gmail.com"
        self.password = "fdsa1234"
        self.EXPECTED_MAIN_TITLE = "Og\u0142oszenia - Sprzedam, kupi\u0119 na OLX.pl".decode('unicode-escape')
        self.USERNAME = u'krk.korki'
        self.MIASTA = ["krakow", "warszawa", "poznan", "wroclaw"]
        self.TITLE = 'korepetycje w fizyki'
        #self.driver = webdriver.Firefox()
        
    def log_to_page(self):
        driver = self.driver
        driver.get('http://olx.pl')
        assert driver.title == self.EXPECTED_MAIN_TITLE
        driver.find_element_by_id("topLoginLink").click()
        driver.find_element_by_id("userEmail").send_keys(self.login)
        driver.find_element_by_id("userPass").send_keys(self.password)
        driver.find_element_by_id("se_userLogin").click()
        assert driver.find_element_by_id("topLoginLink").text == self.USERNAME
        self.logged_in = True

    def check_if_on_first_page(self,topic, city, check_title, max_position):
        driver = self.driver
        web_adress = 'http://olx.pl/muzyka-edukacja/korepetycje/korepetycje-%s/%s/?search[dist]=10' % (topic, city)
        driver.get(web_adress)
        normal_ads_table = driver.find_element_by_id("offers_table")
        ads_titles = normal_ads_table.find_elements(By.TAG_NAME, 'strong')[::2]
        counter = 1
        self.dupa = []
        for el in ads_titles:
            self.dupa.append(el)
            if el.text == self.TITLE:
                return True
            counter += 1
            if counter > max_position:
                return False
        return False

    def add_ad(self, ad):
        if not self.logged_in:
            self.log_to_page()
        driver = self.driver
        driver.get('http://olx.pl')
        driver.find_element_by_id("postNewAdLink").click()
        driver.find_element_by_id("add-title").send_keys(ad.title)
        driver.find_element_by_id("targetrenderSelect1-0").click()
        sleep(2)
        driver.find_element_by_link_text("Muzyka i Edukacja").click()
        driver.find_element_by_link_text("Korepetycje").click()
        subject_table = driver.find_element_by_id("category-130")
        for sub in subject_table.find_elements(By.TAG_NAME, 'span'):
            if sub.text.lower() == ad.topic:
                sub.click()
                break
        driver.find_element_by_id("param113").send_keys(ad.price)
        driver.find_element_by_id("targetid_private_business").click()
        hidden_field = olx.driver.find_element_by_xpath("/html/body/div[1]/section/div/div/form/fieldset[1]/div[3]/div[3]/div[2]/div/dl/dd/ul/li[2]/a/span")
        driver.execute_script("arguments[0].click()", hidden_field)
        driver.find_element_by_id("add-description").send_keys(ad.description)
        driver.find_element_by_id("show-gallery-html").click()
        driver.find_element_by_id("htmlbutton_1").find_element_by_tag_name("input").send_keys(os.getcwd() + '\\' + ad.image)
        #driver.find_element_by_id("save").click()
        
    def delete_ad(self, ad):
        if type(ad) == str:
            delete_title = ad
        else:
            delete_title = ad.title
        if not self.logged_in:
            self.log_to_page()
        driver = self.driver
        driver.get('http://olx.pl')
        driver.find_element_by_id("topLoginLink").click()
        all_ads = driver.find_element_by_id("adsTable").find_elements(By.TAG_NAME, 'h3')
        for element in all_ads:
            if element.text == delete_title:
                go_up = element.find_element_by_xpath("../../../../../../..")
                go_up.find_elements_by_xpath("//*[contains(text(), 'zakończ')]")[1].click()
                sleep(2)
                #driver.find_element_by_xpath("//*[contains(text(), 'tak')]")
        
ad1 = Advertisement()
ad1.set_title("Fizyka dla studentow i nie tylko")
ad1.set_city("Krakow")
ad1.set_topic("fizyka")
ad1.set_price(35)
ad1.set_description("ogloszenie1.txt")
ad1.add_image("photo1.jpg")
olx = olxAutomater()
olx.setUP()
olx.log_to_page()
#olx.log_to_page()
#try:
#    olx.add_ad(ad1)
#except selenium.common.exceptions.TimeoutException:
#    #olx.driver.close()
#    olx.add_ad(ad1)
#except selenium.common.exceptions.NoSuchElementException:
#    #olx.driver.close()
#    olx.add_ad(ad1)
#print olx.check_if_on_first_page("fizyka", "krakow",olx.TITLE,55)