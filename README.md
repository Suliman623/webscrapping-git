# GitHub Profile Scraper

## Overview
This project contains a Python script that uses Selenium to scrape basic information from a GitHub user profile. The script extracts the profile image URL, number of repositories, number of followers, and number of following for a given GitHub user.

## Requirements
- Python 3.x
- Selenium
- Chrome WebDriver

## Setup

1. **Install Required Packages:**

   You need to install the Selenium package. You can install it using pip:
   ```bash
   pip install selenium
   ```

2. **Download Chrome WebDriver:**

   Download the Chrome WebDriver compatible with your version of Chrome from [ChromeDriver](https://sites.google.com/chromium.org/driver/). Place the `chromedriver` executable in a directory of your choice.

3. **Update WebDriver Path:**

   In the script, update the path to the `chromedriver` executable if necessary:
   ```python
   driver = webdriver.Chrome(service=Service('/path/to/chromedriver'), options=chrome_options)
   ```

## Usage

1. **Run the Script:**

   Execute the script using Python:
   ```bash
   python github_profile_scraper.py
   ```

2. **Input GitHub Username:**

   When prompted, enter the GitHub username you want to scrape information for.

3. **View Output:**

   The script will print:
   - The URL of the GitHub profile image
   - The number of repositories
   - The number of followers
   - The number of following

## Example

```
Input Github User: exampleuser
Profile Image: https://avatars.githubusercontent.com/u/1234567?v=4
Number of Repositories: 42
Number of Followers: 100
Number of Following: 50
```

## Notes
- Ensure that you have the latest version of Chrome WebDriver and Chrome browser.
- GitHub's HTML structure may change, which could require updates to the XPath selectors used in the script.
- Running the script in headless mode (no UI) can be enabled by adding the `--headless` option to Chrome options.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
