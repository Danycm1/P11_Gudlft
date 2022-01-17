from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager


def test_booking_12_places():
    service = Service(GeckoDriverManager().install(), log_path='test/functional_test/geckodriver.log')
    driver = webdriver.Firefox(service=service)
    driver.get('http://127.0.0.1:5000/')

    button = driver.find_element(By.NAME, "email")
    button.send_keys("john@simplylift.co")
    button.submit()

    driver.implicitly_wait(1)

    button_book_place = driver.find_element(By.LINK_TEXT, "Book Places")
    button_book_place.click()

    button_place = driver.find_element(By.NAME, "places")
    button_place.send_keys("12")
    button_place.submit()

    WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.CLASS_NAME, 'message')))

    assert "Great-booking complete! you bought 12 places" in driver.find_element(By.CLASS_NAME, 'message').text
