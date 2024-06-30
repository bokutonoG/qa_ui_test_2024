from selenium import webdriver
import time
URL = "https://chainik.fun/welcome"


def test_register_valid_data():
    driver = webdriver.Chrome()
    driver.get("https://chainik.fun/welcome")
    time.sleep(5)
    pass




