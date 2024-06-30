import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_search():
    driver = webdriver.Firefox()
    driver.get("https://ya.ru")

    search_input = driver.find_element(By.ID, "text")
    search_input.send_keys("Hello World")

    find_button = driver.find_element(By.XPATH, "//button[contains(text(),'Найти')]")
    find_button.click()

