import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.chrome.service import Service as ChromeService 

options = Options()

# Change to your own path to the chrome profile
options.add_argument("user-data-dir=C:\\Users\\Mark\\AppData\\Local\\Google\\Chrome\\User Data") 

# Change to your own profile name
options.add_argument('--profile-directory=Profile 1')

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install())) 
driver.get('https://app.datacamp.com/groups/gdsc-pup-main/leaderboard')

driver.find_element(By.XPATH, '//*[@id="accountModal"]/div/div/div[3]/div/div/a[3]').click()

time.sleep(10)
driver.quit()
