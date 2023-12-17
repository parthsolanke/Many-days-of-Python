from selenium import webdriver
# for selecting elements we have to import By class
from selenium.webdriver.common.by import By

# for keeping the browser open we have to configure chrome options
# because by default it closes the browser after execution
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# defining the driver
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.in/Axor-Jet-Open-Helmet-Chestnut/dp/B07LCXWFT7/ref=sr_1_9?keywords=axor%2Bhelmets%2Bfor%2Bmen&sr=8-9&th=1")

# finding element by class
price = driver.find_element(By.CLASS_NAME, "a-price-whole")
print(f"\nThe price of the product is: {price.text}")

# for closing the browser
driver.quit()