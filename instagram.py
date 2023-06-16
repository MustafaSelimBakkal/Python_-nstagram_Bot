from instagramUserInfo import usarname,password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class Instagram:
    def __init__(self,usarname,password):
        self.browser = webdriver.ChromeOptions()
        self.browser.add_experimental_option("prefs",{"intl.accept_languages":"en,en_USA"})
        self.browser = webdriver.Chrome()
        self.usarname = usarname
        self.password = password

    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)

        usarnameInput= self.browser.find_element(By.XPATH,"//*[@id='loginForm']/div/div[1]/div/label/input")
        passwordInput = self.browser.find_element(By.XPATH,"//*[@id='loginForm']/div/div[2]/div/label/input")

        usarnameInput.send_keys(self.usarname)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(5)

    def getFollowers(self,max):
        self.browser.get(f"https://www.instagram.com/{self.usarname}")
        time.sleep(5)

        self.browser.get(f"https://www.instagram.com/{self.usarname}/followers/")
        time.sleep(5)

        dialog = self.browser.find_element(By.CSS_SELECTOR,"div[role=dialog] ul")
        followerCount = self.browser.find_elements(By.CSS_SELECTOR,"li")
        print(f"first count:{dialog}")
        action = webdriver.ActionChains(self.browser)

        while True:
            dialog.click()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(2)

            newCount = len(dialog.find_elements(By.CSS_SELECTOR,"li"))

            if followerCount < max:
                followerCount = newCount
                print(f"second count = {newCount}")
                time.sleep(1)
            else:
                break


        followerUsers = []
        i = 0

        for user in followerUsers:
            i += 1
            link = user.find_element(By.CSS_SELECTOR,"a").get_attribute("href")
            if i == max:
                break
            followerUsers.append(link)
            

        with open("followers.txt","w",encoding="UTF-8") as file:
            for item in followerUsers:
                file.write(item + "\n")
            

    def followUser(self,username):
        self.browser.get("https://instagram.com" + username)
        time.sleep(2)

        followButon = self.browser.find_element(By.TAG_NAME,"button")
        if followButon.text != "Following":
            followButon.click()
            time.sleep(2)
        else: 
            print("zaten takiptesin")

    def unFollowUser(self,usarname):
        self.browser.get("https://instagram.com" + usarname)
        time.sleep(2)

        followButton = self.browser.find_element(By.TAG_NAME,"button")
        if followButton.text == "Followwing":
            followButton.click()
            time.sleep(2)
            confirmButton = self.browser.find_element(By.XPATH,"//button[text()='UnFollow']")
            confirmButton.click()
        else:
            print("zaten takip etmiyorsun")


instagram =Instagram(usarname,password)
Liste = ["insatgramismi1","insatgramismi2"]
instagram.signIn()

instagram.getFollowers()

instagram.followUser(Liste)
time.sleep(2)

instagram.unFollowUser(Liste)
time.sleep(2)