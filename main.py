import selenium.common
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def get_book_info(url):
    driver.get(url)
    time.sleep(5)
    title_info = driver.find_element(By.XPATH, '//meta[@property="og:title"]')
    try:
        call_numb = driver.find_element(By.XPATH, "//p[@class='ng-binding ng-scope zero-margin'][1]/span[5]")
    except selenium.common.NoSuchElementException:
        call_numb = driver.find_element(By.XPATH, "//div[@class='flex-xs-100 flex']/p/span[5]")

    # Clicks permalink button
    permalink = driver.find_element(By.XPATH,"//button[@id='PermalinkButtonFullView']"
                                             "/span[@class='_md-nav-button-text']/div[@class='layout-column']"
                                             "/prm-icon/md-icon[@class='md-primoExplore-theme']")
    permalink.click()
    permalink = driver.find_element(By.XPATH,"//div[@class='word-break-all scrolled-url-text"
                                             " layout-fill layout-margin']")

    return call_numb.text, title_info.get_attribute('content').removesuffix(' - Florida State Univ.'), permalink.text


options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)


url =input("Enter the url: ")
call_number, title, permlink = get_book_info(url)
print(title, call_number, permlink)