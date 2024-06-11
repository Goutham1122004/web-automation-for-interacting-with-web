import time
import openai
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


openai.api_key = 'Api_key'

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
except Exception as e:
    print("Error occurred while setting up the Chrome WebDriver:", e)
    exit()


try:
    driver.get("https://github.com/login")
    username_field = driver.find_element("id", "login_field")
    password_field = driver.find_element("id", "password")

    username_field.send_keys("your_github_username")
    password_field.send_keys("your_github_password")
    password_field.send_keys(Keys.RETURN)
    time.sleep(5)
except Exception as e:
    print("Error occurred while logging into GitHub:", e)
    driver.quit()
    exit()


try:
    driver.get("https://example-blog.com/some-post")
    time.sleep(5)
except Exception as e:
    print("Error occurred while navigating to the blog post:", e)
    driver.quit()
    exit()


comment_prompt = "Generate a comment about the importance of web automation."
comment_text = generate_response(comment_prompt)


try:
    comment_box = driver.find_element("id", "comment")
    comment_box.send_keys(comment_text)
    submit_button = driver.find_element("id", "submit")
    submit_button.click()
    time.sleep(5)
except Exception as e:
    print("Error occurred while posting the comment:", e)
    driver.quit()
    exit()


try:
    posted_comment = driver.find_element("xpath", f"//*[contains(text(), '{comment_text}')]")
    print("Comment posted successfully!")
except Exception as e:
    print("Comment posting failed:", e)

driver.quit()
