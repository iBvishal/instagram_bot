from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random 
import sys

class InstagramBot:
    def __init__(self,username,password):
        self.username = username 
        self.password = password
        self.driver = webdriver.Firefox()
    
    def CloseBrowser(self):
        self.driver.close()
    
    def login(self):
        # "//input[@name='username']"
        # nothing to be added significantly
        # "//input[@name='password']"
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(2)
        login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        login_button.click()
        time.sleep(2)

        username_element = driver.find_element_by_xpath("//input[@name='username']")
        username_element.clear()
        username_element.send_keys(self.username)

        password_element = driver.find_element_by_xpath("//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        password_element.send_keys(Keys.RETURN)
        time.sleep(2)
    
    def like_photo(self,hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(2)

        # gathering photos
        pic_hrefs = []
        for i in range(1, 6):
            try:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                # get tags
                hrefs_in_view = driver.find_elements_by_tag_name('a')
                # finding relevant hrefs
                hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view
                                 if '.com/p/' in elem.get_attribute('href')]
                # building list of unique photos
                [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]
                # print("Check: pic href length " + str(len(pic_hrefs)))
            except Exception:
                continue

        # Liking Photos
        unique_photos = len(pic_hrefs)
        for pic_href in pic_hrefs:
            driver.get(pic_href)
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                time.sleep(random.randint(2, 4))
                like_button = lambda: driver.find_element_by_xpath('//span[@aria-label="Like"]').click()
                like_button().click()
                for second in reversed(range(0, random.randint(18, 28))):
                    print("#"+hashtag+': unique photos left: '+str(unique_photos)+" | Sleeping "+ str(second))
                    time.sleep(1)
            except Exception as e:
                print(e)
                time.sleep(2)
            unique_photos -= 1

if __name__ == '__main__':
    username = "USERNAME"
    password = "PASSWORD"
    bot = InstagramBot(username, password)
    bot.login()
    hashtags = ['love', 'photooftheday','instagood','fashion','beautiful','happy','cute','follow','me','selfie','summer','art','friends','repost','nature','fun','style','smile','food','instalike','family','travel','likeforlike','fitness','beauty','amazing','instagram','photography','photo','sun','music','beach','sunset','dog','cat','motivation','party','cool','lol','design','funny','healthy','night','instapic','lifestyle','flowers','hot','instafood','wedding','fit','black','pink','blue','workout','holiday','home','sea','winter','blessed','summer','sunkissed']
    
    while(True):
        try:
            # select any random tag from list of hashtags
            tag = random.choice(hashtags)
            bot.like_photo(tag)
        except Exception:
            bot.CloseBrowser()
            time.sleep(10)
            bot = InstagramBot(username,password)
            bot.login()