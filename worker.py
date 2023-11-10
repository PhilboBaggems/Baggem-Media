from setup import startup
from actions import search#, comment, gpt

driver = startup.initialize_chrome_webdriver()
# email = startup.prompt_user_google_email_address()
# password = startup.prompt_user_for_google_password()
email = 'ryanneilparker@gmail.com'

# hashtags = ['#SoftwareDevelopment']
hashtag = '#SoftwareDevelopment'

startup.initialize_script(driver)

search.for_posts(driver, hashtag)

# for hashtag in hashtags:
    # search.for_posts(driver, hashtag)
    # comment.on_ten_posts()
        # gpt.get_response()
