import random

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def element_are_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def element_are_presents(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_clickable(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def double_click_action(self, element):
        actions = ActionChains(self.driver)
        actions.double_click(element)
        actions.perform()

    def right_click_action(self, element):
        actions = ActionChains(self.driver)
        actions.context_click(element)
        actions.perform()

    def click_to_element(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click()
        actions.perform()

    def click_to_enter(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ENTER)
        actions.perform()

    def click_to_arrow_down(self):
        actions = ActionChains(self.driver)
        for i in range(random.randint(3, 20)):
            actions.send_keys(Keys.ARROW_DOWN)
        actions.perform()

    def remove_ads(self):
        self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();")
        self.driver.execute_script("document.getElementById('fixedban').remove();")



