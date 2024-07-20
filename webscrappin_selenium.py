from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os

# Initialize WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Optional: run headless for no UI
driver = webdriver.Chrome(service=Service('/path/to/chromedriver'), options=chrome_options)

github_user = input('Input Github User: ')

# Load the GitHub user profile page
url = f'https://github.com/{github_user}'
driver.get(url)

# Fetch profile image
avatar_element = driver.find_element(By.XPATH, '//*[@alt="Avatar"]')
profile_image = avatar_element.get_attribute('src')
print("Profile Image:", profile_image)

# Fetch number of repositories
repositories_element = driver.find_element(By.XPATH, "//a[contains(@href, '?tab=repositories')]/span")
repositories_count = repositories_element.text.strip()
print("Number of Repositories:", repositories_count)

# Fetch number of followers
followers_element = driver.find_element(By.XPATH, "//a[contains(@href, '?tab=followers')]/span[@class='text-bold color-fg-default']")
followers_count = followers_element.text.strip()
print("Number of Followers:", followers_count)

# Fetch number of following
following_element = driver.find_element(By.XPATH, "//a[contains(@href, '?tab=following')]/span[@class='text-bold color-fg-default']")
following_count = following_element.text.strip()
print("Number of Following:", following_count)

# Quit the WebDriver
driver.quit()
