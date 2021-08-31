import inspect

import pytest
from selenium.webdriver.support.select import Select
import logging


@pytest.mark.usefixtures("setup")

class baseclass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger

    def GenderSelection(self, locator, index):
        dropdown = Select(locator)
        dropdown.select_by_index(index)