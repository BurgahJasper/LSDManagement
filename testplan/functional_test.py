from selenium import webdriver
from selenium.webdriver.common.by import By

passCount = 0
failCount = 0
# Set up the Chrome driver
driver = webdriver.Chrome()

# Navigate to the website to test search functionality
driver.get("https://ec2-3-131-85-246.us-east-2.compute.amazonaws.com/search/")

# Validate the page title
try:
    assert "Search" in driver.title
    print("PASSED: Search title found")
    passCount = passCount  + 1
except AssertionError as e:
    print("FAILED: Search title not found", e)
    failCount = failCount + 1

# Find the search box and enter a query
search_box = driver.find_element(By.NAME, "s")
search_box.send_keys("Trump")

# Click the search button
search_button = driver.find_element(By.CLASS_NAME, "search-icon")
search_button.click()
#print(driver.title)
#input("Press any key to continue testing...")
#print("Let's check search result... Count is= ")
# Validate the search results page title
try:
    assert "Search Results" in driver.title
    print("PASSED: Search result title found")
    passCount = passCount  + 1
except AssertionError as e:
    print("FAILED: Search result title not found", e)
    failCount = failCount + 1



try:
    assert "Trump" in driver.title
    print("PASSED: Search text found")
    passCount = passCount  + 1
except AssertionError as e:
    print("FAILED: Search text not found", e)
    failCount = failCount + 1


# find all links on the webpage
searchResultCountInFirstPage = driver.page_source.count("<article")
#print(searchResultCountInFirstPage)

try:
    assert 10 == searchResultCountInFirstPage
    print("PASSED: 10 == searchResultCountInFirstPage")
    passCount = passCount  + 1
except AssertionError as e:
    print("FAILED: Count is not 10, check application for error or fix test case",e)
    failCount = failCount + 1
# loop through the links and print their href attribute


try:
    assert "Trump Tweeted Nine Times To Deleted Russian Twitter Accounts And No One Is Talking About It" in driver.page_source
    print("PASSED: ", "Trump Tweeted Nine Times To Deleted Russian Twitter Accounts And No One Is Talking About It", " Found")
    passCount = passCount  + 1
except AssertionError as e:
    print("FAILED: ",
    "Trump Tweeted Nine Times To Deleted Russian Twitter Accounts And No One Is Talking About It", " Not Found",e)
    failCount = failCount + 1

try:
    assert "Military Veterans HUMILIATE Trump For Attacking Senator" in driver.page_source
    print("PASSED: ", "Military Veterans HUMILIATE Trump For Attacking Senator", " Found")
    passCount = passCount  + 1
except AssertionError as e:
    print("FAILED: ",
    "Military Veterans HUMILIATE Trump For Attacking Senator", " Not Found",e)
    failCount = failCount + 1

try:
    assert "Here Is A Comprehensive And Up To Date List Of All The Allies Trump Has Offended" in driver.page_source
    print("PASSED: ", "Here Is A Comprehensive And Up To Date List Of All The Allies Trump Has Offended", " Found")
    passCount = passCount  + 1
except AssertionError as e:
    print("FAILED: ",
    "Here Is A Comprehensive And Up To Date List Of All The Allies Trump Has Offended", " Not Found",e)
    failCount = failCount + 1

#input("Press any key to close the browser window...")


# Close the browser
driver.quit()


##Validate home page is loaded.
driver = webdriver.Chrome()
# Navigate to the website to test search functionality
driver.get("https://ec2-3-131-85-246.us-east-2.compute.amazonaws.com/")
try:
    assert "CoolerLSDMFakeNews" in driver.page_source
    print("PASSED: ", "Home page loaded successfully and CoolerLSDMFakeNews text", " Found")
    passCount = passCount  + 1
except AssertionError as e:
    print("FAILED: ",
    "Home page did not load successfully and CoolerLSDMFakeNews text", " Not Found",e)
    failCount = failCount + 1

driver.quit()

##Validate visualization pgae is loaded.
driver = webdriver.Chrome()
# Navigate to the website to test search functionality
driver.get("https://ec2-3-131-85-246.us-east-2.compute.amazonaws.com/visualizations/")


try:
    assert "Visualizations" in driver.title
    print("PASSED: Visualizations page loaded and Visualizations title found")
    passCount = passCount  + 1
except AssertionError as e:
    print("FAILED: Visualizations title not found", e)
    failCount = failCount + 1

try:
    assert "site-main" in driver.page_source
    print("PASSED: ", "Visualization page Visualization Section is loaded")
    passCount = passCount  + 1
except AssertionError as e:
    print("FAILED: ",
    "Visualization page Visualization Section is not loaded",e)
    failCount = failCount + 1

driver.quit()


print('--------------------------------Test Summary----------------------------------------')
print('Total Test cases : ', passCount+failCount)
print('Total Test case PASSED : ', passCount)
print('Total Test case FAILED : ', failCount)