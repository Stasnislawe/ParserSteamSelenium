from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

service = Service(executable_path=GeckoDriverManager().install())
options = webdriver.FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(service=service, options=options)

driver.get("https://steamcommunity.com/market")