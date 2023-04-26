from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the Chrome driver
driver = webdriver.Chrome()

# Navigate to the website
driver.get("https://ec2-3-131-85-246.us-east-2.compute.amazonaws.com/search/")

# Validate the page title
assert "Search" in driver.title

# Find the search box and enter a query
search_box = driver.find_element(By.NAME, "s")
search_box.send_keys("Trump")

# Click the search button
search_button = driver.find_element(By.CLASS_NAME, "search-icon")
search_button.click()
print(driver.title)
input("Press any key to continue testing...")
print("Let's check search result... Count is= ")
# Validate the search results page title
assert "Search Results" in driver.title
assert "Trump" in driver.title


# find all links on the webpage
searchResultCountInFirstPage = driver.page_source.count("<article")
print(searchResultCountInFirstPage)
assert 10 == searchResultCountInFirstPage, "Count is not 10, check application for error or fix testcase"
# loop through the links and print their href attribute

assert "Trump Tweeted Nine Times To Deleted Russian Twitter Accounts And No One Is Talking About It" in driver.page_source
assert "Military Veterans HUMILIATE Trump For Attacking Senator" in driver.page_source
assert "Here Is A Comprehensive And Up To Date List Of All The Allies Trump Has Offended" in driver.page_source

input("Press any key to close the browser window...")
# Close the browser
driver.quit()