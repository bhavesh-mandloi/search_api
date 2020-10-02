from selenium.webdriver.support import expected_conditions as EC
import driver as driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from seleniumwire import webdriver
import re
from selenium.webdriver.common.keys import Keys

brand_url = input("Please enter the location URL: ")

if brand_url.endswith("/"):
    brand_url = brand_url[:-1]

url_regex = re.compile('^http.*')

if url_regex.match(brand_url):
    url = brand_url
else:
    url = "https://" + brand_url

domain = url.replace("https://www.", "")

sitemap = url + "/sitemap.xml"
robots = url + "/robots.txt"

driver = webdriver.Firefox()


def open_links():
    driver.get(robots)

    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(sitemap)

    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[2])
    driver.get(url)


open_links()


def search_store():
    elements = driver.find_elements_by_tag_name('a')
    store = []
    for elem in elements:
        href = elem.get_attribute('href')
        url_match_regex = re.compile('.*centres.*|.*store.*|.*location.*|.*find-gym.*')
        if url_match_regex.match(str(href)):
            url_not_match_regex = re.compile('(?!.*google.*)')
            if url_not_match_regex.match(str(href)):
                store.append(href)
                print(href)
    return store


store_url = list(search_store())
# var_regex = r"\b(?=\w)" + re.escape(TEXTO) + r"\b(?!\w)"

store_url_index = input("Please type the store URL index; index starts from 0 and numbered only:")
store_url_index = int(store_url_index)
print("The selected store URL is: " + store_url[store_url_index])
'''
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[3])
driver.get(store_url[store_url_index])
'''

driver = webdriver.Firefox()
driver.get(store_url[store_url_index])


def respo():
    print("Current Browser URL is: " + driver.current_url)
    try:
        api_calls = []
        for requ in driver.requests:
            res = requ.response.headers['Content-Type']
            if res == "application/json" or res == "application/json; charset=utf-8":
                api_calls.append(requ.url)
                print(requ.url)
    except:
        print("Some headers does not have the Content-Type defined so ignoring then")
    return api_calls


all_apis = list(respo())


def location_api():
    api = []
    for items in all_apis:
        domain_match_regex = re.compile('.*' + domain + '.*')
        if domain_match_regex.match(str(items)):
            api.append(items)
            print(api)
    return (api)


main_location_api = list(location_api())

api_index = input("Please type the store URL index; index starts from 0 and numbered only:")
api_index = int(api_index)
print("The selected store URL is: " + main_location_api[api_index])

driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get('http://anno.web.parsec.apple.com:8000/fetch?source=maps_brand_scraper&url=' + main_location_api[api_index])