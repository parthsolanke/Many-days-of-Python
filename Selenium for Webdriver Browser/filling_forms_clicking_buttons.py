from selenium import webdriver
from selenium.webdriver.common.by import By
# for sending keys as inpt in forms we have to import Keys
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Clicking
# link
link = driver.find_element(By.LINK_TEXT, "Wikipedia")
link.click()
# button
menu = driver.find_element(By.ID, "vector-main-menu-dropdown-checkbox")
menu.click()
random_page = driver.find_element(By.ID, "n-randompage")
random_page.click()

# Typing
search_box = driver.find_element(By.NAME, "search")
search_box.send_keys("PyTorch") # Types "Python"
search_box.send_keys(Keys.ENTER) # Presses Enter

driver.quit()
