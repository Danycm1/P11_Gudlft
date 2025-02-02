from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager


def test_logout():
    service = Service(GeckoDriverManager().install(), log_path='test/functional_test/geckodriver.log')
    driver = webdriver.Firefox(service=service)
    driver.get('http://127.0.0.1:5000/')

    button = driver.find_element(By.NAME, "email")
    button.send_keys("john@simplylift.co")
    button.submit()

    driver.implicitly_wait(1)

    button_logout = driver.find_element(By.LINK_TEXT, "Logout")
    button_logout.click()

    WebDriverWait(driver, 10).until(ec.url_to_be('http://127.0.0.1:5000/'))
    assert "GUDLFT Registration" in driver.title
    driver.quit()
