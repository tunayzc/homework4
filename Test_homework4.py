from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from datetime import date
from time import sleep 
import pytest
from pathlib import Path

class Test_homework4:
    
    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        self.folderPath=str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)
        

    def teardown_method(self):
        self.driver.quit()
    
    def waitForElementVisible(self,locator,timeout=5):
       WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))
    def inputName(self,userName):
        self.waitForElementVisible((By.ID,"user-name"))
        inputName = self.driver.find_element(By.ID,"user-name")
        inputName.send_keys(userName)

    def inputPassword(self,password):
        self.waitForElementVisible((By.ID,"password"))      
        inputPassword=self.driver.find_element(By.ID,"password")
        inputPassword.send_keys(password)
        
    def loginButtonClick(self):
        self.waitForElementVisible((By.ID,"login-button"))
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click() 
               
    def loginuser(self,username,password):
        self.inputName(username)
        self.inputPassword(password)
        self.loginButtonClick()

    def validLogin(self):
        self.inputName("standard_user")
        self.inputPassword("secret_sauce")
        self.loginButtonClick()
        
    def errorButtonClick(self):
        errorbutton = self.driver.find_element(By.CLASS_NAME, "error-button")
        errorbutton.click()  

    def add_all(self):
        self.validLogin()
        list=("add-to-cart-sauce-labs-backpack",
              "add-to-cart-sauce-labs-bike-light",
              "add-to-cart-sauce-labs-bolt-t-shirt",
              "add-to-cart-sauce-labs-fleece-jacket",
              "add-to-cart-sauce-labs-onesie",
              "add-to-cart-test.allthethings()-t-shirt-(red)")
        i=0
        for i in range(len(list)):

            self.waitForElementVisible((By.ID,list[i]))
            add_cart=self.driver.find_element(By.ID,list[i])
            add_cart.click()
            

#------------------------------------------------------------

    def  test_nullLogin(self):
        self.loginButtonClick()   

        self.waitForElementVisible((By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3"))
        errorMessage = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        assert errorMessage.text == "Epic sadface: Username is required"  
        
        self.driver.save_screenshot(f"{self.folderPath}/test_nullLogin.png")
        


    def test_nullPassword(self):
        
        self.inputName("standard_user")
        self.loginButtonClick()

      
        self.waitForElementVisible((By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]"))
        errorMessage=self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]")    
        assert errorMessage.text == "Epic sadface: Password is required"
        
        self.driver.save_screenshot(f"{self.folderPath}/test_nullPassword.png")


    def test_forbiddenUser(self):
        self.inputName("locked_out_user")       
        self.inputPassword("secret_sauce")         
        self.loginButtonClick()
      

        self.waitForElementVisible((By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3"))
        errorMessage=self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        assert errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        
        self.driver.save_screenshot(f"{self.folderPath}/test_forbiddenUser.png")


    def test_errorButton(self):
        
        self.loginButtonClick()
        self.waitForElementVisible((By.CLASS_NAME, "error-button"))         
        self.errorButtonClick()
        buttonIsVisible=len(self.driver.find_elements(By.CLASS_NAME, "error-button"))            
        self.driver.save_screenshot(f"{self.folderPath}/test_errorButton.png")
        
        
        
        assert buttonIsVisible==0
    
    def test_trueLogin(self):   
             
        self.validLogin()
        ifPageLoaded=(self.driver.current_url=="https://www.saucedemo.com/inventory.html")
        
        list = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert(ifPageLoaded and len(list)==6)
        
        self.driver.save_screenshot(f"{self.folderPath}/test_trueLogin.png")

    def test_add_cart(self):
        
        self.validLogin()
        saucelabsBackpack=self.driver.find_element(By.CLASS_NAME,"inventory_item_name")
        saucelabsBackpack.click()

        ifPageLoaded=self.driver.current_url=="https://www.saucedemo.com/inventory-item.html?id=4"
        assert (ifPageLoaded==True)
        
        self.driver.save_screenshot(f"{self.folderPath}/test_add_cart.png")


    def test_add_all(self):
        
        self.add_all()

        self.waitForElementVisible((By.CLASS_NAME,"shopping_cart_link"))
        cartLink=self.driver.find_element(By.CLASS_NAME,"shopping_cart_link")
        cartLink.click()
    
        self.waitForElementVisible((By.XPATH,"/html/body/div/div/div/div[2]/div/div[1]"))
        list=self.driver.find_elements(By.CLASS_NAME,"cart_item")
        assert (len(list)==6)
        
        self.driver.save_screenshot(f"{self.folderPath}/test_add_all.png")


    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce"),("performance_glitch_user","secret_sauce"),("problem_user","secret_sauce")])
    def test_valid_users(self,username,password):
        self.inputName(username)
        self.inputPassword(password)
        self.loginButtonClick()

        ifPageLoaded=self.driver.current_url=="https://www.saucedemo.com/inventory.html"
        assert (ifPageLoaded==True)
        self.driver.save_screenshot(f"{self.folderPath}/test_valid_users.png")