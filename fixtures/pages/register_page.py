from faker import Faker
from selenium.webdriver.common.by import By

faker = Faker()


class RegisterPage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open_main_page(self):
        self.driver.get(self.url)
        pass

    # open_register_page
    def open_register_page(self):
        button_go_to_register = self.driver.find_element(By.XPATH, "xpath")
        button_go_to_register.click()

    # register
    def register(self, email=None, password1=None, password2=None):
        if email is None:
            email = faker.email()
        if password1 is None:
            password1 = faker.password()
            password2 = password1
        input_email = self.driver.find_element(By.XPATH, "xpath")
        input_email.send_keys(email)

        input_pass = self.driver.find_element(By.XPATH, "xpath")
        input_pass.send_keys(password1)

        input_pass_2 = self.driver.find_element(By.XPATH, "xpath")
        input_pass_2.send_keys(password2)

        button_register = self.driver.find_element(By.XPATH, "xpath")
        button_register.click()
        pass

    def get_toast_text(self):
        toast = self.driver.find_element(By.XPATH, "xpath")
        return toast.text

    def get_email_error_text(self):
        email_error = self.driver.find_element(By.XPATH, "xpath")
        return email_error.text
    pass
