import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture()
def driver():
    service = Service("C://Program Files/ChromDriver/chromedriver.exe")
    options = Options()
    driver = webdriver.Chrome(service=service, options=options)
    driver.set_window_size(1024, 768)
    yield driver
    driver.quit()

def test_iframe(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/iframes.html")
    
    wait = WebDriverWait(driver, 10)
    iframe = wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "my-iframe")))

    element = driver.find_element(By.ID, "content")
    assert "semper posuere integer et senectus justo curabitur." in element.text
