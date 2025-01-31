import json
from page.base_page import BasePage


class SearchPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        with open("page_data/search_page.json", "r", encoding="utf-8") as file:
            self.data = json.load(file)

    def click_input_btn(self):
        self.find_element(self.data['input_button'])
    
    