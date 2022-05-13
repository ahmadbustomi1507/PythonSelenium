from page_factory import stokbit
from tools import utility as Ut
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def before_all(context):
    #TO DO : set the driver here
    pass

def before_feature(context, feature):
    context.feature.base_web = "https://stockbit.com//"
    context.feature.driver   = webdriver.Chrome(Ut.driver_path())

def before_scenario(context, scenario):
    pass

def after_feature(context, feature):
    pass

def after_scenario(context, scenario):
    pass