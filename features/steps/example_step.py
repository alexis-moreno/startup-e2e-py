from behave import *
from hamcrest import *
from features.lib.pages.google_home_page import GoogleHomePage
from features.lib.pages.google_results_page import GoogleResultsPage


@given('open Google page')
def open_google_home(context):
    google = GoogleHomePage(context)
    context.GoogleHomePage = google


@when('type Selenium on search input')
def search_selenium(context):
    context.GoogleHomePage.search_term('Selenium')


@then('verify the results are being shown')
def verify_first_result(context):
    google_res = GoogleResultsPage(context)
    assert_that(google_res.first_result(), contains_string('Selenium'))
