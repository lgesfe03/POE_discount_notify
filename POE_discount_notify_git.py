import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

look = "Invisible Buff Effect"
# test
# look = "Scavenger Ratmother Pet"
# look = "Midnight Pact Character Effect"
url = "https://www.pathofexile.com/shop/category/specials"
LINE_url = 'https://notify-api.line.me/api/notify'
LINE_token = '' #regist at https://notify-bot.line.me/zh_TW/
LINE_headers = {'Authorization': 'Bearer ' + LINE_token}
Content = ""
# Use Chrome as the browser
browser = webdriver.Chrome()
is_exist = False
# Load the webpage
browser.get(url)

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
if is_exist == False:
    print(look + " is NOT on discount!")
else:
    # send part
    LINE_data = {'message': Content}
    LINE_Send_data = requests.post(LINE_url, headers=LINE_headers, data=LINE_data)
# Close the browser
browser.quit()