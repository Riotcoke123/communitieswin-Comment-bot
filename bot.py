from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

def wait_for_element(driver, by, value, timeout=20):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((by, value))
    )

def read_comments(file_path):
    with open(file_path, 'r') as file:
        comments = file.readlines()
    return [comment.strip() for comment in comments]

def check_comment_exists(driver, comment_text):
    comments_section = driver.find_elements(By.CSS_SELECTOR, ".comment")  # Adjust the selector based on the actual comment class
    for comment in comments_section:
        if comment_text in comment.text:
            return True
    return False

def check_bot_comment_exists(driver):
    bot_comments = driver.find_elements(By.XPATH, "//*[contains(text(), '')]")  # Adjust the XPath based on the actual comment content
    return len(bot_comments) > 0

# Path to the comments text file
comments_file_path = 'comments.txt'

# Read comments from the file
comments = read_comments(comments_file_path)

# Initialize the WebDriver (Make sure the chromedriver is in your PATH or provide the executable path)
driver = webdriver.Chrome()

# Track processed posts
processed_posts = set()

try:
    # Open the main page directly to the new posts section
    print("Navigating to the new posts section...")
    driver.get("https://communities.win/c/ip2always/new")
    print("Navigated to new posts section")

    # Click on the login button using the provided selector
    print("Waiting for the login button...")
    login_button = wait_for_element(driver, By.CSS_SELECTOR, "#app > header > div.sc-1tg9jte-35.chhaHL.navbar > div.sc-1tg9jte-1.fsVFHt.desktop > div.sc-1tg9jte-34.bwtFHD > div > div.sc-1tg9jte-5.dGvpnF")
    login_button.click()
    print("Clicked on the login button")

    # Wait for the login modal to appear
    print("Waiting for the login modal...")
    login_modal = wait_for_element(driver, By.CSS_SELECTOR, "#chakra-modal-1")
    print("Login modal located")

    # Wait for the username field to be present
    print("Waiting for the username field...")
    username_field = wait_for_element(driver, By.CSS_SELECTOR, "#field-2")
    print("Username field located")

    # Find and fill the username field
    username = ""
    print("Entering username...")
    username_field.send_keys(username)

    # Find and fill the password field
    print("Waiting for the password field...")
    password_field = wait_for_element(driver, By.CSS_SELECTOR, "#field-3")
    print("Password field located")
    password = ""
    print("Entering password...")
    password_field.send_keys(password)

    # Submit the login form using the modal button
    print("Waiting for the submit button...")
    submit_button = wait_for_element(driver, By.CSS_SELECTOR, "#chakra-modal-1 > footer > button.chakra-button.css-za4or7")
    submit_button.click()
    print("Clicked on the submit button")

    # Wait for login to complete and ensure the page is fully loaded
    print("Waiting for the page to load completely...")
    time.sleep(5)  # Adjust the sleep duration if necessary

    # Loop through posts
    while True:
        try:
            # Locate the first comment link on the page
            print("Waiting for the comment link...")
            post_links = driver.find_elements(By.CSS_SELECTOR, "div > div > div > div.sc-1bet0vd-1.cCcGax > div.sc-1bet0vd-2.gZebQC > div > a")
            new_post_link = None

            for link in post_links:
                post_url = link.get_attribute('href')
                if post_url not in processed_posts:
                    new_post_link = link
                    processed_posts.add(post_url)
                    break

            if not new_post_link:
                print("No new posts to process.")
                break

            new_post_link.click()
            print("Clicked on the comment link")

            # Wait for the comment input field to appear
            print("Waiting for the 'Type your comment...' placeholder...")
            comment_input = wait_for_element(driver, By.XPATH, "//textarea[@placeholder='Type your comment...']")
            comment_input.click()
            print("Clicked on the comment input field")

            # Select a random comment from the list
            comment_text = random.choice(comments)
            print("Selected comment:", comment_text)

            # Check if the comment already exists
            if not check_comment_exists(driver, comment_text):
                # Enter the comment text
                print("Entering comment:", comment_text)
                comment_input.send_keys(comment_text)

                # Click the save button to post the comment
                print("Waiting for the save button...")
                save_button = wait_for_element(driver, By.CSS_SELECTOR, "#app > div > main > div > div.sc-2e1ezt-0.gqeLlp.comments > form > div.sc-2e1ezt-2.dPOMCj > button")
                save_button.click()
                print("Clicked on the save button")

                # Wait to ensure the comment is posted
                print("Waiting for the comment to be posted...")
                time.sleep(5)
                print("Comment posted successfully")
            else:
                print("Comment already exists, not posting again")

            # Navigate back to the main page with new posts
            print("Navigating back to the new posts section...")
            driver.get("https://communities.win/c/ip2always/new")
            print("Navigated back to the new posts section")

            # Wait to avoid being detected as a bot
            time.sleep(random.randint(5, 10))  # Adjust the sleep duration if necessary
        except Exception as e:
            print(f"An error occurred while processing a post: {e}")
            # Navigate back to the main page if an error occurs and continue with the next post
            driver.get("https://communities.win/c/ip2always/new")
            time.sleep(5)

        # Scroll down to the next post
        print("Scrolling down to the next post...")
        driver.execute_script("window.scrollBy(0, 1000);")  # Adjust the scroll amount if necessary
        time.sleep(2)  # Wait to ensure the page is loaded after scrolling

        # Check if the bot has already commented on the new post
        print("Checking if the bot has already commented...")
        if check_bot_comment_exists(driver):
            print("Bot has already commented, moving to the next post...")
            continue

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()
