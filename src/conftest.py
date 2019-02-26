# from pytest import fixture
# from selenium import webdriver
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#
#
# @fixture(params=[webdriver.Remote(
#             command_executor='http://hub:4444/wd/hub',
#             desired_capabilities=DesiredCapabilities.CHROME,
#         )])
# def browser(request):
#     driver = request.param
#     drvr = driver()
#     yield drvr
#     drvr.quit()
