from selenium.webdriver.common.by import By


class firstPage:
    name = (By.CSS_SELECTOR, "input[name='name']:nth-child(2)")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.CSS_SELECTOR, "input[type='checkbox']")
    Dropdown = (By.ID, "exampleFormControlSelect1")
    Submit = (By.XPATH, "//input[@type='submit']")
    alert = (By.CLASS_NAME, "alert-success")

    def __init__(self, driver):
        self.driver = driver

    def EnterName(self):
        return self.driver.find_element(*firstPage.name)

    def EnterEmail(self):
        return self.driver.find_element(*firstPage.email)

    def EnterPassword(self):
        return self.driver.find_element(*firstPage.password)

    def ClickCheckbox(self):
        return self.driver.find_element(*firstPage.checkbox)

    def SelectGender(self):
        return self.driver.find_element(*firstPage.Dropdown)

    def ClickSubmit(self):
        return self.driver.find_element(*firstPage.Submit)

    def CheckAlert(self):
        return self.driver.find_element(*firstPage.alert)