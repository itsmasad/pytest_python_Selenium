from conftest import wait

class TestLogin:
    def test_navigate_to_google(self, browser):
        browser.get("https://www.google.com")
        wait()