from appium import webdriver
from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC


@allure.step('click element')
def click_element(driver, xpath: str) -> WebElement:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath)),
        f"Can't not find element xpath is {xpath}"
    )
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath)),
        f"Can't not find element xpath is {xpath}")
    element.click()


@allure.step('send key')
def send_key(driver, xpath: str, text: str) -> WebElement:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath)),
        f"Can't not find element xpath is {xpath}"

    )
    element.send_keys(text)


@allure.step('scroll page')
def scroll_page(driver: webdriver.Remote, pixels: int):
    driver.execute_script(f"window.scrollBy(0, {pixels});")

@allure.step('take screenshot')
def element_screenshot(driver: webdriver.Remote, screenshot_name: str = "screenshot.png"):
    driver.save_screenshot(screenshot_name)

@allure.step('wait for element disappear')
def wait_element_disappear(driver, xpath):
    WebDriverWait(driver, 2).until(
        EC.invisibility_of_element_located((By.XPATH, xpath))
    )

@allure.step('waiting element')
def wait_element(driver, xpath):
    WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
