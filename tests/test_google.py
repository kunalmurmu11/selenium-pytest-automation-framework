import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")
class TestGoogleSearch:

    def test_search_automationstepbystep(self):
        self.driver.get("https://www.google.com")
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.send_keys("Automation Step by Step")
        search_box.submit()

        assert "Google" in self.driver.title

    def test_search_raghav(self):
        self.driver.get("https://www.google.com")
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.send_keys("Raghav Pal")
        search_box.submit()

        assert "Google" in self.driver.title