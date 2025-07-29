import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep


@pytest.fixture
def setup_browser():
    chrome_options = Options()
    chrome_driver_path = "C://Program Files/ChromDriver/chromedriver.exe"
    service = Service(chrome_driver_path)
    
    browser = webdriver.Chrome(service=service, options=chrome_options)
    browser.set_window_size(1280, 1024)
    browser.get("https://itcareerhub.de/ru")
    
    yield browser
    
    browser.quit()


def test_logo_visible(setup_browser):
    logo = setup_browser.find_element(By.CSS_SELECTOR, "img.tn-atom__img")
    assert logo.is_displayed(), "Логотип не отображается на странице"


def test_navigation_links(setup_browser):
    expected_links = [
        "Программы",
        "Способы оплаты",
        "Новости",
        "О нас",
        "Отзывы"
    ]
    
    for link_text in expected_links:
        link = setup_browser.find_element(By.LINK_TEXT, link_text)
        assert link.is_displayed(), f"Ссылка '{link_text}' не найдена"


def test_language_toggle(setup_browser):
    switch_to_de = setup_browser.find_element(By.LINK_TEXT, "de")
    sleep(1)
    switch_to_de.click()
    sleep(1)
    
    current_url = setup_browser.current_url
    assert current_url == "https://itcareerhub.de/", f"Ошибка при переключении на немецкую версию, текущий URL: {current_url}"


def test_phone_icon_click(setup_browser):
    phone_icon = setup_browser.find_element(By.CSS_SELECTOR, "img[imgfield='tn_img_1710153310161']")
    phone_icon.click()
    sleep(1)
    
    message = setup_browser.find_element(By.CSS_SELECTOR, 'div[class="t396__elem tn-elem tn-elem__7679561671711363912027"]')
    assert message.is_displayed(), "Сообщение не отображается после клика по иконке"
    assert message.text == "Если вы не дозвонились, заполните форму на сайте. Мы свяжемся с вами", "Текст сообщения не соответствует ожидаемому"
