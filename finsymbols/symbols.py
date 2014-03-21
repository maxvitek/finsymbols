from bs4 import BeautifulSoup
from .symbol_helper import *


def get_sp500_symbols():
    page_html = wiki_html('List_of_S%26P_500_companies', 'SP500.html')
    wiki_soup = BeautifulSoup(page_html, 'html5lib')
    symbol_table = wiki_soup.find(attrs={'class': 'wikitable sortable'})

    symbol_data_list = list()

    for symbol in symbol_table.find_all("tr"):
        symbol_data_content = dict()    
        symbol_raw_data = symbol.find_all("td")
        td_count = 0
        for symbol_data in symbol_raw_data:
            if td_count == 0:
                symbol_data_content['symbol'] = symbol_data.text.encode('utf-8')
            elif td_count == 1:
                symbol_data_content['company'] = symbol_data.text.encode('utf-8')
            elif td_count == 3:
                symbol_data_content['sector'] = symbol_data.text.encode('utf-8')
            elif td_count == 4:
                symbol_data_content['industry'] = symbol_data.text.encode('utf-8')
            elif td_count == 5:
                symbol_data_content['headquarters'] = symbol_data.text.encode('utf-8')
            
            td_count += 1
                
        symbol_data_list.append(symbol_data_content)

    return symbol_data_list[1::]


def get_nyse_symbols():
    symbol_list = read_csv('NYSE')
    return symbol_list


def get_amex_symbols():
    symbol_list = read_csv('AMEX')
    return symbol_list


def get_nasdaq_symbols():
    symbol_list = read_csv('NASDAQ')
    return symbol_list
