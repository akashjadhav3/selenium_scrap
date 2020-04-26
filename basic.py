from selenium import webdriver
from selenium.webdriver.common.keys import Keys # Enter key to submit
from selenium.webdriver.chrome.options import Options # not open chrome browser
from shutil import which

chrome_options = Options() # not open chrome browser
chrome_options.add_argument("--headless") # not open chrome browser
chrome_path = which("./chromedriver")

driver = webdriver.Chrome(executable_path=chrome_path, options=chrome_options) #options without open chrome browser
driver.get('https://www.duckduckgo.com')

search_input = driver.find_element_by_xpath("//input[contains(@class,'js-search-input search__input--adv')][1]")
search_input.send_keys("my user agent")

# search_btn= driver.find_element_by_id("search_button_homepage")
# search_btn.click()
search_input.send_keys(Keys.ENTER) 

print(driver.page_source) # not open chrome browser
driver.close() # always close driver