from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class testhomework3:
    driver=webdriver.Chrome()
    website = "https://www.saucedemo.com"
    def null_login(self):
        self.driver.get(self.website)
        sleep(1)
        userNameInput = self.driver.find_element(By.ID ,"user-name")
        userPwInput = self.driver.find_element(By.ID, "password")      
        userNameInput.send_keys("")
        userPwInput.send_keys("")
        sleep(1)
        loginButton = self.driver.find_element(By.ID, "login-button")
        loginButton.click()
        sleep(1)
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3" )
        testResult=errorMessage.text == "Epic sadface: Username is required"
        print(f"Test Sonucu: ---{testResult}---")
        sleep(2)

    def null_password_login(self):
        self.driver.get(self.website)
        userNameInput = self.driver.find_element(By.ID ,"user-name")
        userPwInput = self.driver.find_element(By.ID, "password")              
        userNameInput.send_keys("standard_user")
        userPwInput.send_keys("")
        sleep(1)
        loginButton=self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        sleep(1)
        errorMessage= self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult=errorMessage.text == "Epic sadface: Password is required"
        print(f"Test Sonucu: ---{testResult}---")
        sleep(2)
    
    def forbidden_user_login(self):
        self.driver.get(self.website)
        userNameInput = self.driver.find_element(By.ID, "user-name")
        userPwInput = self.driver.find_element(By.ID, "password")        
        userNameInput.send_keys("locked_out_user")
        userPwInput.send_keys("secret_sauce")
        sleep(1)
        loginButton = self.driver.find_element(By.ID, "login-button")
        loginButton.click()
        sleep(1)
        errorMessage = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"Test Sonucu: ---{testResult}---")
        sleep(2)
    
    def error_showcase(self):
        self.driver.get(self.website)
        userNameInput = self.driver.find_element(By.ID, "user-name")
        userPwInput = self.driver.find_element(By.ID, "password")  
        userNameInput.send_keys("")
        userPwInput.send_keys("")
        sleep(1)
        loginButton = self.driver.find_element(By.ID, "login-button")
        loginButton.click()
        sleep(1)
        errorButton= self.driver.find_element(By.CLASS_NAME, "error-button")
        errorButton.click()
        errorIcons = self.driver.find_elements(By.CLASS_NAME,"error_icon")
        testResult = len(errorIcons)==0
        print(f"Test Sonucu: ---{testResult}---")
        sleep(2)
    
    def true_login(self):
        self.driver.get(self.website)
        userNameInput = self.driver.find_element(By.ID, "user-name")
        userPwInput = self.driver.find_element(By.ID, "password")        
        userNameInput.send_keys("standard_user")
        userPwInput.send_keys("secret_sauce")
        sleep(1)
        loginButton = self.driver.find_element(By.ID, "login-button")
        loginButton.click()
        sleep(1)
        self.driver.get("https://www.saucedemo.com/inventory.html")
        testResult = self.driver.current_url == "https://www.saucedemo.com/inventory.html"
        print(f"Test Sonucu: ---{testResult}---")
        sleep(2)
    
    def qty_item(self):
        test_homework3.true_login(self)
        sleep(2)
        currentItems = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        testResult= len(currentItems) == 6
        print(f"Satıştaki ürün sayısı: {len(currentItems)}")
        print(f"Test Sonucu: ---{testResult}---")
        sleep(5)
        
test = test_homework3()
test.null_login()
test.null_password_login()
test.forbidden_user_login()
test.error_showcase()
test.true_login()
test.qty_item()