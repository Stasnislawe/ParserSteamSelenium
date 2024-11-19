import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

service = Service(executable_path=GeckoDriverManager().install())
options = webdriver.FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(service=service, options=options)


def products_on_page(driver, count):
    for id in range(0, count):
        result = f'result_{id}'
        dr1 = driver.find_element("id", result)
        dr_price = dr1.find_elements("class name", "normal_price")[1]
        dr_name = dr1.find_element("class name", "market_listing_item_name")
        print(f'{dr_name.text} - {dr_price.text}')
    return print('Всё, страница закончилась')


def next_page(driver, pages):
    print(f'Всего страниц найдено == {pages.text}')
    count = len(driver.find_elements("xpath", "//a[@class='market_listing_row_link']"))
    print(f'Страница 1')
    print(f'Текующий юрл - {driver.current_url}')
    products_on_page(driver, count)
    for i in range(2, int(pages.text)+1):
        driver.find_element("xpath", "//span[@id='searchResults_btn_next']").click()
        time.sleep(5)
        count = len(driver.find_elements("xpath", "//a[@class='market_listing_row_link']"))
        print(f'Страница {i}')
        print(f'Текующий юрл - {driver.current_url}')
        products_on_page(driver, count)
    return print(f'Всё перебрал, устал, ушёл на перекур.')


driver.get("https://steamcommunity.com/market")

input_search = input('Поиск предметов: ')

if input_search:
    dr_search = driver.find_element("xpath", "//input[@id='findItemsSearchBox']")
    dr_search.send_keys(input_search)
    dr_submit = driver.find_element("xpath", "//input[@id='findItemsSearchSubmit']")
    dr_submit.click()

    pages = driver.find_elements("xpath", "//span[@class='market_paging_pagelink']")[-1]

    next_page(driver, pages)
else:
    dr_click = driver.find_element("xpath", "//span[@id='popularItemsMore']")
    dr_click.click()
    pages = driver.find_elements("xpath", "//span[@class='market_paging_pagelink']")[-1]
    next_page(driver, pages)

