import pytest
from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from fixtures.pages.register_page import RegisterPage


# faker = Faker()
#
#
# # open_register_page
# def open_register_page(driver):
#     button_go_to_register = driver.find_element(By.XPATH, "xpath")
#     button_go_to_register.click()
#
#
# # register
# def register(driver, email=None, password1=None, password2=None):
#     if email is None:
#         email = faker.email()
#     if password1 is None:
#         password1 = faker.password()
#         password2 = password1
#     input_email = driver.find_element(By.XPATH, "xpath")
#     input_email.send_keys(email)
#
#     input_pass = driver.find_element(By.XPATH, "xpath")
#     input_pass.send_keys(password1)
#
#     input_pass_2 = driver.find_element(By.XPATH, "xpath")
#     input_pass_2.send_keys(password2)
#
#     button_register = driver.find_element(By.XPATH, "xpath")
#     button_register.click()
#     pass
#
#
# def get_toast_text(driver):
#     toast = driver.find_element(By.XPATH, "xpath")
#     return toast.text
#
#
# def get_email_error_text(driver):
#     email_error = driver.find_element(By.XPATH, "xpath")
#     return email_error.text


@pytest.mark.xfail
def test_register_valid_data(driver):
    # driver conftest usage param in func (driver)
    # options = Options()
    # options.add_argument("--headless=new")  # without GUI on CICD
    # driver = webdriver.Chrome(options=options)
    # driver.implicitly_wait(10)
    driver, url = driver
    driver.get(url)
    # open_register_page
    register_page = RegisterPage(driver=driver, url=url)
    register_page.open_main_page()
    register_page.open_register_page()

    # register
    register_page.register()
    # assert
    assert register_page.get_toast_text() == "Success"
    driver.quit()


# def test_register_invalid_email():
#     # driver
#     options = Options()
#     options.add_argument("--headless=new")  # without GUI on CICD
#     driver = webdriver.Chrome(options=options)
#     driver.get("https://chainik.fun/welcome")
#     # register
#     open_register_page(driver)
#     # register_page
#     invalid_email = "test@test"
#     register(driver, email=invalid_email)
#     assert_stage
#     assert get_email_error_text(driver) == f'Error, {invalid_email} is not email address'
#     driver.quit()
