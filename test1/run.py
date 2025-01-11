from test1.items_on_page import next_page
from test1.pysel import driver

input_search = input('Поиск предметов: ')


if input_search:
    dr_search = driver.find_element("xpath", "//input[@id='findItemsSearchBox']")
    dr_search.send_keys(input_search)
    dr_submit = driver.find_element("xpath", "//input[@id='findItemsSearchSubmit']")
    dr_submit.click()

    pages = driver.find_elements("xpath", "//span[@class='market_paging_pagelink']")[-1]

    next_page(driver, pages, input_search)
else:
    dr_click = driver.find_element("xpath", "//span[@id='popularItemsMore']")
    dr_click.click()
    pages = driver.find_elements("xpath", "//span[@class='market_paging_pagelink']")[-1]
    next_page(driver, pages)