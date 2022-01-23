from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support import expected_conditions as ec


def test_show_club_point_page():
    service = Service(GeckoDriverManager().install(), log_path='test/functional_test/geckodriver.log')
    driver = webdriver.Firefox(service=service)
    driver.get('http://127.0.0.1:5000/')

    button = driver.find_element(By.LINK_TEXT, 'View clubs points')
    button.click()

    WebDriverWait(driver, 10).until(ec.url_to_be('http://127.0.0.1:5000/displayPoints'))
    assert "GUDLFT Club Information" in driver.title
    driver.quit()
