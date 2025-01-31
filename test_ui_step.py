from appium import webdriver
from appium.options.android import UiAutomator2Options
import time
import allure
from selenium.webdriver.support import expected_conditions as EC
import json
from ui_function import click_element, send_key, scroll_page, element_screenshot, wait_element, wait_element_disappear
with open("xpath.json", "r", encoding="utf-8") as file:
    data = json.load(file)
with open("config.json", "r", encoding="utf-8") as file:
    capabilities = json.load(file)['capabilities']


@allure.title("wap test")
@allure.description("use selenium to open twitch and scroll web select one streamer")
def test_ui_function():
    appium_server_url = 'http://localhost:4723'
    driver = webdriver.Remote(
        appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
    driver.get("https://m.twitch.tv/")
    click_element(driver, data['search_button'])
    click_element(driver, data['input_button'])
    click_element(driver, data['input_button'])
    send_key(driver, data['input_button'], "StarCraft II")
    time.sleep(1)
    click_element(driver, data['title1_button'])
    time.sleep(1)
    scroll_page(driver, 200)
    scroll_page(driver, 200)
    click_element(driver, data['streamer_button'])
    wait_element_disappear(driver, data['loading_icon'])
    wait_element(driver, data['video_info'])
    time.sleep(2)
    element_screenshot(driver, screenshot_name="screenshot.png")
    driver.quit()
