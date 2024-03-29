import unittest
import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException

class TestTemplate(unittest.TestCase):
    """Include test cases on a given url"""

    def setUp(self):
        """Start web driver"""
        self.driver = webdriver.Remote(
            command_executor='http://selenium-chrome:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)
        self.driver.implicitly_wait(2)

    def tearDown(self):
        """Stop web driver"""
        self.driver.quit()


    def test_ad_link(self):
        """Find and click ad title button"""
        try:
            self.driver.get('http://frontend:8000/')
            #time.sleep(15)
            el = self.driver.find_element_by_class_name('adClass')
            el.click()
            #time.sleep(15)
            info = self.driver.find_element_by_class_name("adClass");
            contains_title = "Google" in info.get_attribute("innerHTML")
            #time.sleep(15)
            self.assertTrue(contains_title)
        except NoSuchElementException as ex:
            self.fail(ex.msg)

    def test_login_logout(self):
        """Log in using web interface"""
        try:
            self.driver.get('http://frontend:8000/login')
            time.sleep(15)
            username = self.driver.find_element_by_id('id_email')
            username.send_keys("draden@gmail.com")
            password = self.driver.find_element_by_id('id_password')
            password.send_keys("1234")
            #self.driver.implicitly_wait(10)
            password.submit()

        except NoSuchElementException as ex:
            self.fail(ex.msg)


        try:
            #WebDriverWait(self.driver, 15)
            html = self.driver.execute_script("return document.body.innerHTML;")
            print("HERERER")
            #print(html)
            self.assertEqual(self.driver.title, "Home")
            #self.driver.implicitly_wait(4)
            logout = self.driver.find_element_by_partial_link_text("Logout")
            self.assertEqual(logout.get_attribute("href"), "http://frontend:8000/logout")
            #time.sleep(10)
            logout.click()

            login_button = self.driver.find_element_by_partial_link_text("Login")
            #time.sleep(10)
            self.assertEqual(login_button.get_attribute("href"), "http://frontend:8000/login")
        except NoSuchElementException as ex:
            self.fail(ex.msg)






        except NoSuchElementException as ex:
            self.fail(ex.msg)

    def test_create_ad(self):
        """Create a ad using web interface"""
        try:
            self.driver.get('http://frontend:8000/login')
            #time.sleep(15)
            username = self.driver.find_element_by_id('id_email')
            username.send_keys("draden@gmail.com")
            password = self.driver.find_element_by_id('id_password')
            password.send_keys("1234")
            #self.driver.implicitly_wait(10)
            password.submit()
        except NoSuchElementException as ex:
            self.fail(ex.msg)

        try:
            self.driver.get('http://frontend:8000/ad_create')
            time.sleep(15)
            site_title = self.driver.find_element_by_id('id_site_title')
            site_title.send_keys("Free")
            url = self.driver.find_element_by_id('id_url')
            url.send_keys("http://Free.com")
            price = self.driver.find_element_by_id('id_price')
            price.send_keys(12)
            duration = self.driver.find_element_by_id('id_duration')
            duration.send_keys(20)

            submit = self.driver.find_element_by_class_name("btn")
            submit.click()
            #time.sleep(15)
            self.assertEqual(self.driver.title, "Home")

        except NoSuchElementException as ex:
            self.fail(ex.msg)

    def test_search(self):
        """Search for an ad using web interface"""
        try:
            self.driver.get('http://frontend:8000/')
            #time.sleep(15)
            search = self.driver.find_element_by_class_name('form-control')
            search.send_keys("Google")
            search.submit()
            #time.sleep(15)
            info = self.driver.find_element_by_class_name("starter-template")
            contains_title = "Google" in info.get_attribute("innerHTML")
            #time.sleep(15)
            self.assertTrue(contains_title)

        except NoSuchElementException as ex:
            self.fail(ex.msg)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTemplate)
    unittest.TextTestRunner(verbosity=2).run(suite)
