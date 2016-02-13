from olx_adder import *

'''
author: askorek@gmail.com
all rights reserved

DEMO OF USAGE of olx_adder
set your own account and password
'''				

ACCOUNT = ''
PASSWORD = ''
 
user_waw = User(ACCOUNT,PASSWORD,"warszawa")
user_waw.add_proxy('94.20.63.134',3128)

ad_waw_fiz = Advertisement()
ad_waw_fiz.set_topic("fizyka")
ad_waw_fiz.set_title("Fizyka wszystkie poziomy")
ad_waw_fiz.set_city("warszawa")
ad_waw_fiz.set_price(35)
ad_waw_fiz.set_description("waw-fiz.txt")
ad_waw_fiz.add_image("p-waw.jpg")

ad_waw_stat = Advertisement()
ad_waw_stat.set_topic("inne")
ad_waw_stat.set_title("Statystyka - korepetycje")
ad_waw_stat.set_city("warszawa")
ad_waw_stat.set_price(35)
ad_waw_stat.set_description("waw-stat.txt")
ad_waw_stat.add_image("p-waw.jpg")

user_waw.add_ad_to_list(ad_waw_fiz)
user_waw.add_ad_to_list(ad_waw_stat)

auto_waw = olxAutomater(user_waw)
auto_waw.add_user(user_waw)
auto_waw.setUP()          
auto_waw.log_to_page()

olx = olxAutomater()
olx.setUP()
olx.log_to_page()


try:
    olx.add_ad(ad1)
except selenium.common.exceptions.TimeoutException:
    olx.driver.close()

except selenium.common.exceptions.NoSuchElementException:
    olx.driver.close()

print olx.check_if_on_first_page("fizyka", "krakow",olx.TITLE,55)