import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

@pytest.fixture()
def driver():
    service = Service("C://Program Files/ChromDriver/chromedriver.exe")
    options = Options()
    driver = webdriver.Chrome(service=service, options=options)
    driver.set_window_size(1024, 768)
    yield driver
    driver.quit()

def test_dragging(driver):
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")

    wait = WebDriverWait(driver, 10)
    consent_btn = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "button.fc-button.fc-cta-consent.fc-primary-button")
        )
    )
    consent_btn.click()

    iframe = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, 'div[rel-title="Photo Manager"] > p > iframe')
        )
    )
    driver.switch_to.frame(iframe)

    source = driver.find_element(By.CSS_SELECTOR, "#gallery > li:nth-child(1)")
    target = driver.find_element(By.ID, "trash")

    actions = ActionChains(driver)
    actions.drag_and_drop(source, target).perform()

    wait.until(EC.visibility_of_element_located((By.ID, "trash")))

    ul = driver.find_element(By.ID, "gallery")
    li = ul.find_elements(By.TAG_NAME, "li")
    assert len(li) == 3
