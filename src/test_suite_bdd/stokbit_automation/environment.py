from src.tools import utility as Ut
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

def before_all(context):
    pass

def before_feature(context, feature):
    context.feature.base_web = "https://stockbit.com//"
    context.feature.driver   = webdriver.Chrome(Ut.driver_path())
    context.feature.actions  = ActionChains(context.feature.driver)

def before_scenario(context, scenario):
    pass

def after_feature(context, feature):
    context.feature.driver.quit()

def after_scenario(context, scenario):
    pass