import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

look =      "Invisible Buff Effect"
look2 =     "Vanishing Dye"
url = "https://www.pathofexile.com/shop/category/specials"
# test
# look = "Gore Stormbind Effect"
# url = "https://www.pathofexile.com/shop/category/alternate-skill-effects"
LINE_url = 'https://notify-api.line.me/api/notify'
LINE_token = 'vunr6lJWO9OcwAT08caWQ8s1RRNjZrpA9ErRypGEOiN' #regist at https://notify-bot.line.me/zh_TW/
LINE_headers = {'Authorization': 'Bearer ' + LINE_token}
Content = ""
# Use Chrome as the browser
browser = webdriver.Chrome()
is_exist = False
# Load the webpage
browser.get(url)

# Scroll down the page
# Get the initial scroll position
prev_scroll_position = browser.execute_script("return window.pageYOffset;")
# Scroll down the page
browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
while True:
    # Wait for the page to load
    time.sleep(1)
    # Get the current scroll position
    curr_scroll_position = browser.execute_script("return window.pageYOffset;")
    if curr_scroll_position == prev_scroll_position:
        # Reached the bottom of the page
        break
    # Scroll down again
    browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    prev_scroll_position = curr_scroll_position
# Find all elements with class="shopItem-container"
shop_items = browser.find_elements(By.CLASS_NAME, "shopItem-container")

for shop_item in shop_items:
    # Find the element with class="name" inside each shop item
    name_element = shop_item.find_element(By.CLASS_NAME, "name")

    # Check if the name contains "Splintering Shield"
    if look in name_element.text:
        # Print the content of the shop item
        is_exist = True
        print(shop_item.text)
        Content += str(shop_item.text)
    elif look2 in name_element.text:
        # Print the content of the shop item
        is_exist = True
        print(shop_item.text)
        Content += str(shop_item.text) 
if is_exist == False:
    print(look +" & "+ look2 + " is NOT on discount!")
else:
    # send part
    LINE_data = {'message': Content}
    LINE_Send_data = requests.post(LINE_url, headers=LINE_headers, data=LINE_data)
# Close the browser
browser.quit()