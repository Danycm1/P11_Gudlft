from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support import expected_conditions as ec


def test_login_with_correct_email():
    service = Service(GeckoDriverManager().install(), log_path='test/functional_test/geckodriver.log')
    driver = webdriver.Firefox(service=service)
    driver.get('http://127.0.0.1:5000/')

    button = driver.find_element(By.NAME, "email")
    button.send_keys("john@simplylift.co")
    button.submit()

    WebDriverWait(driver, 10).until(ec.url_to_be('http://127.0.0.1:5000/showSummary'))
    assert "Summary | GUDLFT Registration" in driver.title
    driver.quit()


def test_login_with_wrong_email():
    service = Service(GeckoDriverManager().install(), log_path='test/functional_test/geckodriver.log')
    driver = webdriver.Firefox(service=service)
    driver.get("http://127.0.0.1:5000/")

    button = driver.find_element(By.NAME, "email")
    button.send_keys("wrong@example.com")
    button.submit()

    WebDriverWait(driver, 10).until(ec.url_to_be('http://127.0.0.1:5000/showSummary'))
    assert "Summary | GUDLFT Registration" not in driver.title
    driver.quit()
