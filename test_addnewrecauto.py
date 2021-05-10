# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestAddnewrecauto():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_addnewrecauto(self):
    self.driver.get("https://redsealine.net/wp-login.php?redirect_to=https%3A%2F%2Fredsealine.net%2Fwp-admin%2F&reauth=1")
    self.driver.set_window_size(1054, 808)
    self.driver.find_element(By.ID, "user_login").send_keys("admin")
    self.driver.find_element(By.ID, "user_pass").send_keys("A6yhKou22")
    self.driver.find_element(By.ID, "wp-submit").click()
    self.driver.find_element(By.CSS_SELECTOR, ".menu-icon-post > .wp-menu-name").click()
    self.driver.find_element(By.LINK_TEXT, "Добавить новую").click()
    self.driver.find_element(By.ID, "title").send_keys("new_record")
    self.driver.find_element(By.ID, "publish").click()
    self.driver.find_element(By.CSS_SELECTOR, "#wp-admin-bar-my-account > .ab-item > .display-name").click()
    self.driver.find_element(By.LINK_TEXT, "Привет, admin").click()
  
