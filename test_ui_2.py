import allure
import pytest
from core_framework.system.core_object import CoreObject
from page.home_page import HomePage


class TestFirst(CoreObject):

    @pytest.fixture(scope="function", autouse=True)
    def setup_teardown_method(self, driver):
        print("Setup method")
        self.home_page = HomePage(driver=driver, platform=self.platform)
        yield
        print("Teardown method")

    @allure.title("wap test")
    @allure.description("use selenium to open twitch and scroll web select one streamer")
    @pytest.mark.parametrize("driver", ["web"], indirect=True)
    def test_first_testcase_1(self):
        self.home_page.go_to_twich()
        self.home_page.input_search_text("StarCraft II")
        self.home_page.click_search_result(index=0)
        print("Test case 1")


