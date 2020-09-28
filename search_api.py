from selenium.webdriver.support import expected_conditions as EC
import driver as driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from seleniumwire import webdriver
import re
from selenium.webdriver.common.keys import Keys

location_url = input("Please enter the location URL: ")

if location_url.endswith("/"):
    location_url = location_url[:-1]

url_regex = re.compile('^http.*')

if url_regex.match(location_url):
    url = location_url
else:
    url = "https://" + location_url

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

elements = driver.find_elements_by_tag_name('a')
for elem in elements:
    href = elem.get_attribute('href')
    url_match_regex = re.compile('.*centres.*|.*store.*|.*location.*')
    if url_match_regex.match(str(href)):
        url_not_match_regex = re.compile('(?!.*google.*)')
        if url_not_match_regex.match(str(href)):
            print(href)


# var_regex = r"\b(?=\w)" + re.escape(TEXTO) + r"\b(?!\w)"


def respo():
    try:
        for requ in driver.requests:
            res = requ.response.headers['Content-Type']
            if res == "application/json" or res == "application/json; charset=utf-8":
                print(requ.url)
    except:
        print("Some headers does not have the Content-Type defined so ignoring then")
    return requ.url


api_list = [respo()]
