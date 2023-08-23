import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_option = Options()

driver = webdriver.Chrome(options=chrome_option)
start_url = 'https://web.whatsapp.com'
driver.get(start_url)
time.sleep(50)

search_box = driver.find_element(By.CLASS_NAME, '_2vDPL')
search_box.send_keys('Larry Marin')  
time.sleep(5)
search_box.send_keys(Keys.ENTER)
time.sleep(5)

for i in range(3):
    chat = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]/p')
    time.sleep(1)
    chat.send_keys(f'este es el mensaje desde python {i}')  
    chat.send_keys(Keys.ENTER)

driver.quit()
