import time
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
options = uc.ChromeOptions() 

# options.headless = True 

# Change to your own path to the chrome profile
options.add_argument("user-data-dir=C:\\Users\\Mark\\AppData\\Local\\Google\\Chrome\\User Data") 

# Change to your own profile name
options.add_argument('--profile-directory=Profile 1')

driver = uc.Chrome(use_subprocess=True, options=options) 
driver.maximize_window() 
driver.get('https://app.datacamp.com/groups/gdsc-pup-main/leaderboard')

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='accountModal']/div/div/div[3]/div/div/a[3]"))).click()

time.sleep(10)
driver.quit()
