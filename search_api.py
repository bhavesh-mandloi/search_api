from selenium.webdriver.support import expected_conditions as EC
import driver as driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from seleniumwire import webdriver
import re
from selenium.webdriver.common.keys import Keys

# Create a new instance of the Firefox driver. We can also use the Chrome


location_url = input("Please enter the location URL: ")
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
        print("Store locations URL can be:" + href)


#    if href is not None:
#       assert isinstance(href, object)
#      print(href)


# var_regex = r"\b(?=\w)" + re.escape(TEXTO) + r"\b(?!\w)"


def resp():
    for request in driver.requests:
        if request.response:
            print(
                request.url,
                request.response.headers['Content-Type']
            )


def respo():
    for requ in driver.requests:
        res = requ.response.headers['Content-Type']
        if res == "application/json" or res == "application/json; charset=utf-8":
            print(requ.url)

'''
try:
    respo()
except:
    print("Some headers does not have the Content-Type defined so ignoring then")
'''