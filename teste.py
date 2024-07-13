import unittest
from unittest.mock import patch, MagicMock
from selenium.webdriver.remote.webelement import WebElement

class TestWebScraper(unittest.TestCase):

#test select region
    @patch('selenium.webdriver.Chrome.find_element_by_class_name')
    def test_select_region(self, mock_find_element):
        mock_find_element.return_value = WebElement
        from caseCrawler import select_region
        self.assertIsInstance(select_region, WebElement)

#test button find
    @patch('selenium.webdriver.remote.webelement.WebElement.find_element_by_xpath')
    def test_button(self, mock_find_xpath):
        mock_find_xpath.return_value = WebElement
        from caseCrawler import button
        self.assertIsInstance(button, WebElement)

#testing page information
    @patch('selenium.webdriver.remote.webdriver.WebDriver.find_element_by_class_name')
    def test_information(self, mock_find_element):
        mock_find_element.return_value = WebElement
        from caseCrawler import information
        self.assertIsInstance(information, WebElement)

if __name__ == '__main__':
    unittest.main()
