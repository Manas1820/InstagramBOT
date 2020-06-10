# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 17:02:24 2020

@author: Manas gupta
"""

from selenium import webdriver
from time import sleep


class InstagramBot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(2)
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(4)
        
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(1)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(2)

    def get_unfollowers(self):
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username)).click()
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}/following')]".format(self.username)).click()
        following = self._get_names()
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}/followers')]".format(self.username)).click()
        followers = self._get_names()
        not_following_back = [user for user in following if user not in followers]
        print(not_following_back)

    def _get_names(self):
        sleep(2)
        # To scroll through the followers list
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        # close button
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button").click()
        return names


my_bot = InstagramBot('manasgupta1820','password') #pass your username and password as arguments , try passing the username as it wont work with email
my_bot.get_unfollowers()


