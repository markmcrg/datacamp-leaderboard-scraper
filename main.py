import time
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
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

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'table')))

# Get table headers
table = driver.find_element(By.CSS_SELECTOR, 'table')
headers = [th.text for th in table.find_elements(By.CSS_SELECTOR, "th")]

table_data = []

rows = table.find_elements(By.CSS_SELECTOR, "tr")
for row in rows:
    row_data = [cell.text for cell in row.find_elements(By.CSS_SELECTOR, "td")]
    if row_data and '\n' in row_data[0]:
        row_data[0] = row_data[0][2:].replace('\n', '')
    if row_data:
        table_data.append(row_data)
        
# Convert list of lists to df
df = pd.DataFrame(table_data, columns=headers)
df.to_csv('datacamp_leaderboard.csv', index=False)

driver.quit()
