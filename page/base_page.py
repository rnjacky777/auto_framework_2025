from typing import List
from appium.webdriver.webdriver import WebDriver
from appium.webdriver.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from core_framework.system.core_object import CoreObject


class BasePage(CoreObject):
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def find_element(self, xpath: str) -> WebElement:
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath)),
            f"Can't not find element xpath is {xpath}")
        return element

    def find_elements(self, xpath: str) -> List[WebElement]:
        elements = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, xpath)),
            f"Can't not find element xpath is {xpath}")
        return elements

    def element_screenshot(self, screenshot_name: str = "screenshot.png"):
        self.driver.save_screenshot(screenshot_name)
