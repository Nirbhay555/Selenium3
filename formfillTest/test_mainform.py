import pytest
from selenium.webdriver.support.select import Select

from InputData import firstpageData
from PageObjects.HomepageObj import firstPage
from utilities.BaseClass import baseclass


class TestFormFill(baseclass):
    def test_formFilling(self,getData):
        log = self.getLogger()
        FirstPageObj = firstPage(self.driver)

        FirstPageObj.EnterName().send_keys(getData["name"])
        FirstPageObj.EnterEmail().send_keys(getData["email"])
        FirstPageObj.EnterPassword().send_keys(getData["password"])
        FirstPageObj.ClickCheckbox().click()
        self.GenderSelection(FirstPageObj.SelectGender(), getData["index"])
        FirstPageObj.ClickSubmit().click()
        alert = FirstPageObj.CheckAlert().text
        assert "success" in alert
        self.driver.refresh()

    @pytest.fixture(params=firstpageData.first_pageData.Available_data)
    def getData(self, request):
        return request.param



