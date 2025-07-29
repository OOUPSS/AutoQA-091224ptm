import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def setup_driver():
    """Fixture для инициализации драйвера и открытия сайта"""
    service = Service("C://Program Files/ChromDriver/chromedriver.exe")
    options = Options()
    driver = webdriver.Chrome(service=service, options=options)
    driver.set_window_size(1024, 768)
    driver.get("http://uitestingplayground.com/textinput")
    yield driver
    driver.quit()


def test_button_text_changes(setup_driver):
    """Проверка, что текст кнопки изменяется на 'ITCH' после ввода текста"""
    driver = setup_driver
    input_field = driver.find_element(By.ID, "newButtonName")
    input_field.send_keys("ITCH")  # Вводим текст в поле ввода
    button = driver.find_element(By.ID, "updatingButton")
    
    # Ожидаем, что текст кнопки изменится на 'ITCH'
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element_value((By.ID, "updatingButton"), "ITCH")
    )
    
    # Проверяем, что текст кнопки действительно изменился
    assert button.text == "ITCH", "Текст кнопки не изменился на 'ITCH'"
