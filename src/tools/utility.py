import sys
sys.path.append('.')
# from .combine_html import combine as comb
import os


def driver_path(chrome_version=''):
    curr_path = os.path.dirname(os.path.realpath(__file__))
    # TO DO : add if else environtment, which one of chrome version to be used
    # driver_path = f"\ChromeWebdriver\97.0.4692.71\chromedriver.exe"
    # driver_path = ".\ChromeWebdriver\96.0.4664.45\chromedriver.exe"
    # driver_path = ".\ChromeWebdriver\95.0.4638.69\chromedriver.exe"
    driver_path = ".\ChromeWebdriver\\101.0.4951.41\chromedriver.exe"

    return curr_path + driver_path
#
# def combine(src,dest):
#     try:
#         comb.combine_allure(folder_source=src,folder_destination=dest)
#     except Exception as err:
#         raise Exception('error combining HTML')