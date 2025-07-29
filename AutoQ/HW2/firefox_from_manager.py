import pytest
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

# Настройка драйвера
@pytest.fixture
def driver():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    yield driver
    driver.quit()

def test_payment_methods_section(driver):
    driver.get("https://itcareerhub.de/ru")
    sleep(2)

    try:
        payment_methods_link = driver.find_element(By.LINK_TEXT, "Способы оплаты")
        payment_methods_link.click()
        sleep(2)
    except Exception as e:
        print(f"Ошибка при переходе в раздел 'Способы оплаты': {e}")
        driver.quit()
        return

    try:
        payment_section = driver.find_element(By.XPATH, "//section[contains(@class, 'payment-methods')]")
        
        # Скроллим до секции, если она не видна
        actions = ActionChains(driver)
        actions.move_to_element(payment_section).perform()
        sleep(1)  # Ждем немного, чтобы страница успела отрендерить секцию

        # Делаем скриншот этой секции
        payment_section.screenshot("./payment_methods_section.png")
        print("Скриншот сделан успешно!")

    except Exception as e:
        print(f"Ошибка при поиске секции или снятии скриншота: {e}")
        driver.quit()
        return
