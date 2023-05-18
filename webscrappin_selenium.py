from selenium import webdriver
import os

github_user = input('Input Github User: ')


driver = webdriver.Chrome()

# Load the GitHub user profile page
url = 'https://github.com/' + github_user
driver.get(url)

# Fetch profile image
avatar_element = driver.find_element_by_xpath('//*[@alt="Avatar"]')
profile_image = avatar_element.get_attribute('src')
print("Profile Image:", profile_image)

# Fetch number of repositories
repositories_element = driver.find_element_by_xpath("//a[contains(@class, 'UnderlineNav-item') and contains(@href, '/{0}?tab=repositories')]/span".format(github_user))
repositories_count = repositories_element.text.strip()
print("Number of Repositories:", repositories_count)

# Fetch number of followers
followers_element = driver.find_element_by_xpath("//a[contains(@href, '?tab=followers')]/span[@class='text-bold color-fg-default']".format(github_user))
followers_count = followers_element.text.strip()
print("Number of Followers:", followers_count)

# Fetch number of following
following_element = driver.find_element_by_xpath("//a[contains(@href, '?tab=following')]/span[@class='text-bold color-fg-default']".format(github_user))
following_count = following_element.text.strip()
print("Number of Following:", following_count)

# Quit the WebDriver
driver.quit()
