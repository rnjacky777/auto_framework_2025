import json
import allure
from page.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, driver, platform):
        super().__init__(driver)
        with open(f"page_data/{platform}/home_page.json", "r", encoding="utf-8") as file:
            self.data = json.load(file)

    @allure.step
    def click_search_btn(self):
        self.find_element(self.data['search_button']).click()

    @allure.step
    def click_search_field(self):
        self.find_element(self.data['search_field']).click()

    @allure.step
    def input_search_text(self, text: str):
        self.find_element(self.data['search_field']).send_keys(text)

    @allure.step
    def go_to_twich(self):
        match self.platform:
            case "web":
                self.driver.get("https://twitch.tv/")
            case "wap":
                self.driver.get("https://m.twitch.tv/")
            case _:
                raise ValueError(f"Unsupported platform: {self.platform}")

    @allure.step
    def click_follow_btn(self):
        self.find_element(self.data['follow_btn']).click()

    @allure.step
    def click_search_result(self, index: int = 0):
        search_results = self.find_elements(self.data['search_results'])
        search_results[index].click()
