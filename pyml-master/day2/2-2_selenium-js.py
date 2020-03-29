
import time
from selenium import webdriver

path = "C:/Users/ML_class/ML0322/webdriver/chromedriver.exe"
driver = webdriver.Chrome(path)

# ?��?��?�� ?�� ?��?���? ?���?
driver.get("https://google.com")

# ?��바스?��립트 ?��?��?���?
r = driver.execute_script("return 100 + 50")
print(r)
