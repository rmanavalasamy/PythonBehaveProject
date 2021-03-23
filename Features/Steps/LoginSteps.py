from behave import *
from selenium import webdriver



@given('Launch Browser')
def LaunchChromeBrowser(context):
    context.driver=webdriver.Chrome(r"C:\Users\ravikumarm\Downloads\chromedriver_win32\chromedriver.exe")


@when('Open Facebook Login Page')
def OpenFacebookLoginPage(context):
    context.driver.get("https://chocolatey.org/")


@then('Verify Facebook page successfully Launched')
def VerifyFacebookPageOpenedSuccessfully(context):
    status=context.driver.find_element_by_xpath("//img[@src='/content/images/global-shared/logo-square.svg']").is_displayed()
    assert status is True



