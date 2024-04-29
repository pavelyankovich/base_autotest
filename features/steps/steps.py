import time

from behave import step
from selenium.webdriver.common.by import By

@step('Я захожу на страничку "{name}"')
def step_impl(context,name):
    url = f"{name}"
    context.driver.get(url)
    time.sleep(10)