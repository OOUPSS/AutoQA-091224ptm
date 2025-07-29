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
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    yield driver
    driver.quit()


def test_image_alt_attribute(setup_driver):
    """Проверка, что атрибут alt третьего изображения равен 'award'"""
    driver = setup_driver
    
    # Ожидаем, пока все изображения загрузятся, проверяя видимость третьего изображения
    third_image = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, "(//img[@alt])[3]"))
    )
    
    # Проверяем атрибут alt
    assert third_image.get_attribute("alt") == "award", "Атрибут alt третьего изображения не равен 'award'"
