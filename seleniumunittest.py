import unittest
from selenium import webdriver


class GoogleTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_google_search(self):
        self.driver.get('https://www.google.com/xhtml')
        self.assertIn('Google', self.driver.title)
        search_field = self.driver.find_element_by_name('q')
        search_field.send_keys('google')
        search_field.submit()
        assert "Es wurden keine mit deiner Suchanfrage" not in self.driver.page_source

    def test_google_negative_search(self):
        self.driver.get('https://www.google.com/xhtml')
        self.assertIn('Google', self.driver.title)
        search_field = self.driver.find_element_by_name('q')
        search_field.send_keys('asdasdadasdasdasdasdasdadasdasdasdsdfggdfhgdhdfhfghvbvcbcb')
        search_field.submit()
        assert "Es wurden keine mit deiner Suchanfrage" not in self.driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()


