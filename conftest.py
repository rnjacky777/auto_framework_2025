import pytest
from appium import webdriver as appium_webdriver
from selenium import webdriver as selenium_webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def driver(request):
    platform = request.param
    match platform:
        case "web":
            options = Options()
            options.chrome_executable_path = "./core_framework/util/chromedriver.exe"
            driver = selenium_webdriver.Chrome(options=options)
        case "wap":
            caps = {
                "platformName": "Android",
                "platformVersion": "14.0",
                "deviceName": "Pixel 9 Pro API 35",
                "browserName": "Chrome",
                "automationName": "UiAutomator2",
                "udid": "emulator-5554"
            }
            driver = appium_webdriver.Remote("http://localhost:4723/wd/hub", caps)
        case _:
            raise ValueError(f"Unsupported platform: {platform}")

    yield driver
    driver.quit()
