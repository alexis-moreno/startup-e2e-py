from selenium import webdriver
from dotenv import load_dotenv


def before_all(context):
    load_dotenv()


def before_feature(context, feature):

    if 'browser' in context.config.userdata.keys():
        if context.config.userdata['browser'] is None:
            browser = 'chrome'
        else:
            browser = context.config.userdata['browser']
    else:
        browser = 'chrome'

    if browser == 'chrome':
        context.driver = webdriver.Chrome()
    elif browser == 'firefox':
        context.driver = webdriver.Firefox()
    elif browser == 'safari':
        context.driver = webdriver.Safari()
    elif browser == 'ie':
        context.driver = webdriver.Ie()
    elif browser == 'opera':
        context.driver = webdriver.Opera()
    elif browser == 'phantomjs':
        context.driver = webdriver.PhantomJS()
    else:
        context.driver = webdriver.Chrome()

    context.driver.maximize_window()
    context.driver.implicitly_wait(10)


def after_feature(context, feature):
    context.driver.close()


