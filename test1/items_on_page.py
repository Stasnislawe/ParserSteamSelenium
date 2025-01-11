import time

from test1.table import create_tablename_table, Dbsession


def add_values(name, price, Parser):
    existing_value = Dbsession.query(Parser).filter_by(name=name).first()
    if existing_value is None:
        tab = Parser(str(name), str(price))
        Dbsession.add(tab)
        Dbsession.commit()
    else:
        pass


def products_on_page(driver, count, Parser):
    for id in range(0, count):
        result = f'result_{id}'
        dr1 = driver.find_element("id", result)
        dr_price = dr1.find_elements("class name", "normal_price")[1]
        dr_name = dr1.find_element("class name", "market_listing_item_name")
        print(f'{dr_name.text} - {dr_price.text}')
        add_values(str(dr_name.text), str(dr_price.text), Parser)
    return print('Всё, страница закончилась')


def next_page(driver, pages, input_search='Общее'):
    Parser = create_tablename_table(input_search)
    print(f'Всего страниц найдено == {pages.text}')
    count = len(driver.find_elements("xpath", "//a[@class='market_listing_row_link']"))
    print(f'Страница 1')
    print(f'Текующий юрл - {driver.current_url}')
    products_on_page(driver, count, Parser)
    for i in range(2, int(pages.text)+1):
        driver.find_element("xpath", "//span[@id='searchResults_btn_next']").click()
        time.sleep(5)
        count = len(driver.find_elements("xpath", "//a[@class='market_listing_row_link']"))
        print(f'Страница {i}')
        print(f'Текующий юрл - {driver.current_url}')
        products_on_page(driver, count, Parser)
    return print(f'Всё перебрал, устал, ушёл на перекур.')