from selenium import webdriver
from selenium.webdriver.common.keys import Keys # Enter key to submit
from shutil import which

chrome_path = which("./chromedriver")

driver = webdriver.Chrome(executable_path=chrome_path)
driver.get('https://www.duckduckgo.com')

search_input = driver.find_element_by_xpath("//input[contains(@class,'js-search-input search__input--adv')][1]")
search_input.send_keys("my user agent")

# search_btn= driver.find_element_by_id("search_button_homepage")
# search_btn.click()
search_input.send_keys(Keys.ENTER) 