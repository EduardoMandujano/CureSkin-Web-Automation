from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application
from time import sleep

# I reinstalled the webdriver_manager package to the CureSkin project

from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.events import EventFiringWebDriver

from support.logger import logger, MyListener


# Allure command
# Run this command in the Terminal after installing allure-behave to the project
# Verify that the project has (venv) activated.
# To display the results enter in the terminal allure serve test_results/ OR the name of the results directory
# behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/product_page.feature


def browser_init(context, test_name):

    """
    :param context: Behave context
    :param test_name: scenario.name
    """
    # The line below does NOT work anymore with the Chrome Webdriver Update
    # service = ChromeService('/Users/eduar/Automation/CureSkin-Web-Automation/chromedriver')

    # Uncomment the line below for Firefox testing
    # service = FirefoxService('geckodriver.exe')

    # Comment OUT the line below to run Headless Mode
    # context.driver = webdriver.Chrome(service=service)

    # To update Chrome Webdriver uncomment the line below
    # You need ONLY ONE instance of context.driver, never more than ONE.
    # context.driver = webdriver.Chrome(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # This below is a workaround for the Chrome 115 issue
    # context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(version="114.0.5735.90").install()))
    # context.driver = webdriver.Chrome(service=service, options=options)

    # Hopefully this will fix the Chrome/Python/Selenium Debacle
    # Change .Chrome to .Firefox to switch browsers September 3, 2023
    # I may need to remove chromedriver.exe in the future
    context.driver = webdriver.Chrome()
    # service = Service()
    # options = webdriver.ChromeOptions()
    # options.add_experimental_option('excludeSwitches', ['enable-logging'])
    #
    # context.driver = webdriver.Chrome(service=service, options=options)


    # Uncomment the line below for Firefox testing (NOT working anymore)
    # context.driver = webdriver.Firefox(service=service)

    # Use this line ONLY for Firefox testing
    # context.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    # I added this line below to make this work. There was a recent change in Python 3 VS Python 4.
    # context.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    # context.driver = webdriver.Safari()

    ## HEADLESS MODE ####
    # Uncomment the code block below to launch Headless Mode
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # context.driver = webdriver.Chrome(
    #    chrome_options=options,
    #    service=service
    # )


    ### EventFiringWebDriver - log file ###
    ### for drivers ###
    # context.driver = EventFiringWebDriver(
    #      webdriver.Chrome(service=service),
    #      MyListener()
    #  )
    # for headless mode ###
    # context.driver = EventFiringWebDriver(webdriver.Chrome(chrome_options = options), MyListener())

    # for browerstack ###
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    # bs_user = 'eduardomandujano_hQWLx6'
    # bs_key = 'r87z3v1uSm3tpePpwNq7'
    #
    # desired_cap = {
    #     'browserName': 'Firefox',
    #     'bstack:options': {
    #         'os': 'OS X',
    #         'osVersion': 'Monterey',
    #         'sessionName': test_name
    #     }
    # }
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    # context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)

    # Mobile-Web Emulator
    # mobile_emulation = {"deviceName": "iPhone 12 Pro"}
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    # context.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)

    # The line below did NOT work. Leaving here for later reference.
    # context.driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
    #                                   desired_capabilities=chrome_options.to_capabilities())

    # For Specific Individual Mobile Device Attributes
    # Produced Inconsistent Results Use Above Code Block
    # mobile_emulation = {
    #     "deviceMetrics": {"width": 812, "height": 375, "pixelRatio": 3.0},
    #     "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"}
    # chrome_options = Options()
    # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    # context.driver = webdriver.Chrome(chrome_options=chrome_options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    # print('\nStarted scenario: ', scenario.name)
    # browser_init(context)
    print('\nStarted scenario: ', scenario.name)
    logger.info(f'Started scenario: {scenario.name}')
    browser_init(context, scenario.name)


def before_step(context, step):
    # print('\nStarted step: ', step)
    print('\nStarted step: ', step)
    logger.info(f'Started step: {step}')


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
