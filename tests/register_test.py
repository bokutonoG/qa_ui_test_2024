import pytest
from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://chainik.fun/welcome"

faker = Faker()


def open_register_page(driver):
    button_go_to_register = driver.find_element(By.XPATH, "xpath")
    button_go_to_register.click()


def register(driver, email=None, password1=None, password2=None):
    if email is None:
        email = faker.email()
    if password1 is None:
        password1 = faker.password()
        password2 = password1
    input_email = driver.find_element(By.XPATH, "xpath")
    input_email.send_keys(email)

    input_pass = driver.find_element(By.XPATH, "xpath")
    input_pass.send_keys(password1)

    input_pass_2 = driver.find_element(By.XPATH, "xpath")
    input_pass_2.send_keys(password2)

    button_register = driver.find_element(By.XPATH, "xpath")
    button_register.click()
    pass


def get_toast_text(driver):
    toast = driver.find_element(By.XPATH, "xpath")
    return toast.text


def get_email_error_text(driver):
    email_error = driver.find_element(By.XPATH, "xpath")
    return email_error.text


@pytest.mark.xfail
def test_register_valid_data():
    # driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://chainik.fun/welcome")
    # open_register_page
    open_register_page(driver)
    # register
    register(driver)
    # assert
    assert get_toast_text(driver) == "Success"
    driver.quit()


def test_register_invalid_email():
    # driver
    driver = webdriver.Chrome()
    driver.get("https://chainik.fun/welcome")

    # register
    open_register_page(driver)
    # register_page
    invalid_email = "test@test"
    register(driver, email=invalid_email)
    # assert
    assert get_email_error_text(driver) == f'Error, {invalid_email} is not email address'
    driver.quit()
