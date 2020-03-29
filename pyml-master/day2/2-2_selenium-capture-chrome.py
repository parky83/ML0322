from selenium import webdriver

path = "C:/Users/ML_class/ML0322/webdriver/chromedriver.exe"
driver = webdriver.Chrome(path)

options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome(path, chrome_options=options)

driver.get('http://naver.com')
driver.implicitly_wait(3)
driver.get_screenshot_as_file(
    'C:/Users/ML_class/ML0322/pyml-master/day2/naver_main.png')
driver.quit()
