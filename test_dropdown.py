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

class TestDropdown():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_dropdown(self):
    self.driver.get("https://www.nopcommerce.com/en")
    self.driver.set_window_size(1936, 1048)
    element = self.driver.find_element(By.CSS_SELECTOR, ".navigation-top-menu-main > .navigation-top-menu-item:nth-child(1) > .navigation-top-menu-label")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".navigation-top-menu-main > .navigation-top-menu-item:nth-child(1) > .navigation-top-menu-sublist > .navigation-top-menu-item:nth-child(1) .navigation-top-menu-label")
    assert len(elements) > 0
    element = self.driver.find_element(By.CSS_SELECTOR, ".navigation-top-menu-main > .navigation-top-menu-item:nth-child(1) > .navigation-top-menu-label")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    assert self.driver.find_element(By.CSS_SELECTOR, ".navigation-top-menu-main > .navigation-top-menu-item:nth-child(1) > .navigation-top-menu-sublist > .navigation-top-menu-item:nth-child(1) .navigation-top-menu-label").text == "Store demo"
    element = self.driver.find_element(By.CSS_SELECTOR, ".navigation-top-menu-main > .navigation-top-menu-item:nth-child(1) > .navigation-top-menu-label")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".navigation-top-menu-main > .navigation-top-menu-item:nth-child(1) > .navigation-top-menu-sublist > .navigation-top-menu-item:nth-child(2) .navigation-top-menu-label")
    assert len(elements) > 0
    element = self.driver.find_element(By.CSS_SELECTOR, ".navigation-top-menu-main > .navigation-top-menu-item:nth-child(1) > .navigation-top-menu-label")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    assert self.driver.find_element(By.CSS_SELECTOR, ".navigation-top-menu-main > .navigation-top-menu-item:nth-child(1) > .navigation-top-menu-sublist > .navigation-top-menu-item:nth-child(2) .navigation-top-menu-label").text == "Showcase"
    element = self.driver.find_element(By.CSS_SELECTOR, ".navigation-top-menu-main > .navigation-top-menu-item:nth-child(1) > .navigation-top-menu-label")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".navigation-top-menu-main > .navigation-top-menu-item:nth-child(1) > .navigation-top-menu-sublist > .navigation-top-menu-item:nth-child(3) .navigation-top-menu-label")
    assert len(elements) > 0
    assert self.driver.find_element(By.CSS_SELECTOR, ".navigation-top-menu-main > .navigation-top-menu-item:nth-child(1) > .navigation-top-menu-sublist > .navigation-top-menu-item:nth-child(3) .navigation-top-menu-label").text == "Features"
    element = self.driver.find_element(By.CSS_SELECTOR, ".navigation-top-menu-main > .navigation-top-menu-item:nth-child(1) > .navigation-top-menu-label")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".navigation-top-menu-main > .navigation-top-menu-item:nth-child(1) > .navigation-top-menu-sublist > .navigation-top-menu-item:nth-child(4) .navigation-top-menu-label")
    assert len(elements) > 0
    element = self.driver.find_element(By.CSS_SELECTOR, ".navigation-top-menu-main > .navigation-top-menu-item:nth-child(1) > .navigation-top-menu-label")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    assert self.driver.find_element(By.CSS_SELECTOR, ".navigation-top-menu-main > .navigation-top-menu-item:nth-child(1) > .navigation-top-menu-sublist > .navigation-top-menu-item:nth-child(4) .navigation-top-menu-label").text == "Why for developers"
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".navigation-top-menu-main > .navigation-top-menu-item:nth-child(1) > .navigation-top-menu-sublist > .navigation-top-menu-item:nth-child(5) .navigation-top-menu-label")
    assert len(elements) > 0
    assert self.driver.find_element(By.CSS_SELECTOR, ".navigation-top-menu-main > .navigation-top-menu-item:nth-child(1) > .navigation-top-menu-sublist > .navigation-top-menu-item:nth-child(5) .navigation-top-menu-label").text == "Why for store owners"
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".navigation-top-menu-item:nth-child(6) > .navigation-top-menu-label")
    assert len(elements) > 0
    assert self.driver.find_element(By.CSS_SELECTOR, ".navigation-top-menu-item:nth-child(6) > .navigation-top-menu-label").text == "Industries"
    element = self.driver.find_element(By.CSS_SELECTOR, ".navigation-top-menu-item:nth-child(6) > .navigation-top-menu-label")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".navigation-top-menu-item:nth-child(6) .navigation-top-menu-item:nth-child(1) .navigation-top-menu-label")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".navigation-top-menu-item:nth-child(6) .navigation-top-menu-item:nth-child(2) .navigation-top-menu-label")
    assert len(elements) > 0
    assert self.driver.find_element(By.CSS_SELECTOR, ".navigation-top-menu-item:nth-child(6) .navigation-top-menu-item:nth-child(2) .navigation-top-menu-label").text == "Health & Beauty"
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".navigation-top-menu-item:nth-child(6) .navigation-top-menu-item:nth-child(3) .navigation-top-menu-label")
    assert len(elements) > 0
    assert self.driver.find_element(By.CSS_SELECTOR, ".navigation-top-menu-item:nth-child(6) .navigation-top-menu-item:nth-child(3) .navigation-top-menu-label").text == "Food & Beverage"
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".navigation-top-menu-item:nth-child(6) .navigation-top-menu-item:nth-child(4) .navigation-top-menu-label")
    assert len(elements) > 0
    assert self.driver.find_element(By.CSS_SELECTOR, ".navigation-top-menu-item:nth-child(6) .navigation-top-menu-item:nth-child(4) .navigation-top-menu-label").text == "Automotive"
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".navigation-top-menu-item:nth-child(6) .navigation-top-menu-item:nth-child(5) .navigation-top-menu-label")
    assert len(elements) > 0
    assert self.driver.find_element(By.CSS_SELECTOR, ".navigation-top-menu-item:nth-child(6) .navigation-top-menu-item:nth-child(5) .navigation-top-menu-label").text == "Industrial & Scientific"
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".navigation-top-menu-item:nth-child(6) .navigation-top-menu-item:nth-child(6) .navigation-top-menu-label")
    assert len(elements) > 0
    assert self.driver.find_element(By.CSS_SELECTOR, ".navigation-top-menu-item:nth-child(6) .navigation-top-menu-item:nth-child(6) .navigation-top-menu-label").text == "Furniture"
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".navigation-top-menu-item:nth-child(6) .navigation-top-menu-item:nth-child(7) .navigation-top-menu-label")
    assert len(elements) > 0
    assert self.driver.find_element(By.CSS_SELECTOR, ".navigation-top-menu-item:nth-child(6) .navigation-top-menu-item:nth-child(7) .navigation-top-menu-label").text == "B2B eCommerce"
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".navigation-top-menu-item:nth-child(6) .navigation-top-menu-item:nth-child(8) .navigation-top-menu-label")
    assert len(elements) > 0
    assert self.driver.find_element(By.CSS_SELECTOR, ".navigation-top-menu-item:nth-child(6) .navigation-top-menu-item:nth-child(8) .navigation-top-menu-label").text == "International"
    element = self.driver.find_element(By.CSS_SELECTOR, ".navigation-top-menu-item:nth-child(2) > .navigation-top-menu-label")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".navigation-top-menu-item:nth-child(2) .navigation-top-menu-item:nth-child(1) .navigation-top-menu-label")
    assert len(elements) > 0
    assert self.driver.find_element(By.CSS_SELECTOR, ".navigation-top-menu-item:nth-child(2) .navigation-top-menu-item:nth-child(1) .navigation-top-menu-label").text == "Download nopCommerce"
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".navigation-top-menu-item:nth-child(2) .navigation-top-menu-item:nth-child(2) .navigation-top-menu-label")
    assert len(elements) > 0
    assert self.driver.find_element(By.CSS_SELECTOR, ".navigation-top-menu-item:nth-child(2) .navigation-top-menu-item:nth-child(2) .navigation-top-menu-label").text == "Marketplace"
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".navigation-top-menu-item:nth-child(2) .navigation-top-menu-item:nth-child(3) .navigation-top-menu-label")
    assert len(elements) > 0
    assert self.driver.find_element(By.CSS_SELECTOR, ".navigation-top-menu-item:nth-child(2) .navigation-top-menu-item:nth-child(3) .navigation-top-menu-label").text == "Translations"
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".navigation-top-menu-item:nth-child(2) .navigation-top-menu-item:nth-child(4) .navigation-top-menu-label")
    assert len(elements) > 0
    assert self.driver.find_element(By.CSS_SELECTOR, ".navigation-top-menu-item:nth-child(2) .navigation-top-menu-item:nth-child(4) .navigation-top-menu-label").text == "Copyright removal key"
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".navigation-top-menu-item:nth-child(2) .navigation-top-menu-item:nth-child(5) .navigation-top-menu-label")
    assert len(elements) > 0
    assert self.driver.find_element(By.CSS_SELECTOR, ".navigation-top-menu-item:nth-child(2) .navigation-top-menu-item:nth-child(5) .navigation-top-menu-label").text == "Mobile application"
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".navigation-top-menu-item:nth-child(2) .navigation-top-menu-item:nth-child(6) .navigation-top-menu-label")
    assert len(elements) > 0
    assert self.driver.find_element(By.CSS_SELECTOR, ".navigation-top-menu-item:nth-child(2) .navigation-top-menu-item:nth-child(6) .navigation-top-menu-label").text == "Web API"
    element = self.driver.find_element(By.CSS_SELECTOR, ".navigation-top-menu-main > .navigation-top-menu-item:nth-child(3) > .navigation-top-menu-label")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".navigation-top-menu-item:nth-child(3) .navigation-top-menu-item:nth-child(1) > .navigation-top-menu-link > .navigation-top-menu-label")
    assert len(elements) > 0
    assert self.driver.find_element(By.CSS_SELECTOR, ".navigation-top-menu-item:nth-child(3) .navigation-top-menu-item:nth-child(1) > .navigation-top-menu-link > .navigation-top-menu-label").text == "Training"
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".navigation-top-menu-item:nth-child(3) .navigation-top-menu-item:nth-child(2) > .navigation-top-menu-link > .navigation-top-menu-label")
    assert len(elements) > 0
    assert self.driver.find_element(By.CSS_SELECTOR, ".navigation-top-menu-item:nth-child(3) .navigation-top-menu-item:nth-child(2) > .navigation-top-menu-link > .navigation-top-menu-label").text == "Documentation"
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".navigation-top-menu-item:nth-child(3) .navigation-top-menu-item:nth-child(3) .navigation-top-menu-label")
    assert len(elements) > 0
    assert self.driver.find_element(By.CSS_SELECTOR, ".navigation-top-menu-item:nth-child(3) .navigation-top-menu-item:nth-child(3) .navigation-top-menu-label").text == "Community forums"
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".navigation-top-menu-item:nth-child(3) .navigation-top-menu-item:nth-child(4) .navigation-top-menu-label")
    assert len(elements) > 0
    assert self.driver.find_element(By.CSS_SELECTOR, ".navigation-top-menu-item:nth-child(3) .navigation-top-menu-item:nth-child(4) .navigation-top-menu-label").text == "Premium support services"
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".navigation-top-menu-item:nth-child(3) .navigation-top-menu-item:nth-child(5) .navigation-top-menu-label")
    assert len(elements) > 0
    assert self.driver.find_element(By.CSS_SELECTOR, ".navigation-top-menu-item:nth-child(3) .navigation-top-menu-item:nth-child(5) .navigation-top-menu-label").text == "Request a quote"
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".navigation-top-menu-item:nth-child(3) .navigation-top-menu-item:nth-child(6) .navigation-top-menu-label")
    assert len(elements) > 0
    assert self.driver.find_element(By.CSS_SELECTOR, ".navigation-top-menu-item:nth-child(3) .navigation-top-menu-item:nth-child(6) .navigation-top-menu-label").text == "Contact us"
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".navigation-top-menu > .navigation-top-menu-item > .navigation-top-menu-link > .navigation-top-menu-label")
    assert len(elements) > 0
    assert self.driver.find_element(By.CSS_SELECTOR, ".navigation-top-menu > .navigation-top-menu-item > .navigation-top-menu-link > .navigation-top-menu-label").text == "PARTNERS"
    element = self.driver.find_element(By.CSS_SELECTOR, ".navigation-top-menu-language-selector > .navigation-top-menu-item > .navigation-top-menu-label")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".navigation-top-menu-language-selector > .navigation-top-menu-item .navigation-top-menu-item:nth-child(1) .navigation-top-menu-label")
    assert len(elements) > 0
    assert self.driver.find_element(By.CSS_SELECTOR, ".navigation-top-menu-language-selector > .navigation-top-menu-item .navigation-top-menu-item:nth-child(1) .navigation-top-menu-label").text == "English"
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".navigation-top-menu-language-selector .navigation-top-menu-item:nth-child(2) .navigation-top-menu-label")
    assert len(elements) > 0
    assert self.driver.find_element(By.CSS_SELECTOR, ".navigation-top-menu-language-selector .navigation-top-menu-item:nth-child(2) .navigation-top-menu-label").text == "Español"
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".navigation-top-menu-language-selector .navigation-top-menu-item:nth-child(3) .navigation-top-menu-label")
    assert len(elements) > 0
    assert self.driver.find_element(By.CSS_SELECTOR, ".navigation-top-menu-language-selector .navigation-top-menu-item:nth-child(3) .navigation-top-menu-label").text == "Deutsch"
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".navigation-top-menu-language-selector .navigation-top-menu-item:nth-child(4) .navigation-top-menu-label")
    assert len(elements) > 0
    assert self.driver.find_element(By.CSS_SELECTOR, ".navigation-top-menu-language-selector .navigation-top-menu-item:nth-child(4) .navigation-top-menu-label").text == "Russian"
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".navigation-top-menu-language-selector .navigation-top-menu-item:nth-child(5) .navigation-top-menu-label")
    assert len(elements) > 0
    assert self.driver.find_element(By.CSS_SELECTOR, ".navigation-top-menu-language-selector .navigation-top-menu-item:nth-child(5) .navigation-top-menu-label").text == "Français"
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".navigation-top-menu-item:nth-child(1) > .navigation-top-menu-sublist > .navigation-top-menu-item:nth-child(6) > .navigation-top-menu-link > .navigation-top-menu-label")
    assert len(elements) > 0
    assert self.driver.find_element(By.CSS_SELECTOR, ".navigation-top-menu-item:nth-child(1) > .navigation-top-menu-sublist > .navigation-top-menu-item:nth-child(6) > .navigation-top-menu-link > .navigation-top-menu-label").text == "Italiano"
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".navigation-top-menu-item:nth-child(1) > .navigation-top-menu-sublist > .navigation-top-menu-item:nth-child(7) .navigation-top-menu-label")
    assert len(elements) > 0
    assert self.driver.find_element(By.CSS_SELECTOR, ".navigation-top-menu-item:nth-child(1) > .navigation-top-menu-sublist > .navigation-top-menu-item:nth-child(7) .navigation-top-menu-label").text == "Português"
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".navigation-top-menu-item:nth-child(1) > .navigation-top-menu-sublist > .navigation-top-menu-item:nth-child(8) .navigation-top-menu-label")
    assert len(elements) > 0
    assert self.driver.find_element(By.CSS_SELECTOR, ".navigation-top-menu-item:nth-child(1) > .navigation-top-menu-sublist > .navigation-top-menu-item:nth-child(8) .navigation-top-menu-label").text == "Türkçe"
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".navigation-top-menu-item:nth-child(9) .navigation-top-menu-label")
    assert len(elements) > 0
    assert self.driver.find_element(By.CSS_SELECTOR, ".navigation-top-menu-item:nth-child(9) .navigation-top-menu-label").text == "简体中文"
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".navigation-top-menu-item:nth-child(10) .navigation-top-menu-label")
    assert len(elements) > 0
    assert self.driver.find_element(By.CSS_SELECTOR, ".navigation-top-menu-item:nth-child(10) .navigation-top-menu-label").text == "日本語"
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".navigation-top-menu-item:nth-child(11) .navigation-top-menu-label")
    assert len(elements) > 0
    assert self.driver.find_element(By.CSS_SELECTOR, ".navigation-top-menu-item:nth-child(11) .navigation-top-menu-label").text == "Tiếng Việt"
    element = self.driver.find_element(By.CSS_SELECTOR, ".navigation-top-menu-main > .navigation-top-menu-item:nth-child(1) > .navigation-top-menu-label")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
  
# R a d i m i r - J a v i e r 
 