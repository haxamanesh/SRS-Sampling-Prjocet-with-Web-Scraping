from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import numpy as np
import statistics as st 
import random
from scipy.stats import norm
url = "https://www.tgju.org/profile/price_dollar_rl/history"
driver = webdriver.Chrome()
driver.get(url)
time.sleep(4)
data= []
p =5
for i in range(p):
    table= driver.find_element(By.XPATH,value = "//table[@class = 'table widgets-dataTable table-hover text-center history-table dataTable no-footer']")
    rows = table.find_elements(By.XPATH, value = ".//tr")[1:]
    for row in rows:
    # In each row, get the columns
        cols = row.find_elements(By.XPATH, value = ".//td[4]")
        for col in cols:
        # Print the text of each column
            print(col.text) 
            data.append(col.text)     
    # data.append(col.text)
    driver.refresh()        
    search_button = driver.find_element(By.ID,value = "DataTables_Table_0_next")
    search_button.click()
    time.sleep(4)
price = [int(s.replace(',', '')) for s in data]
print(price)
np.savetxt("samplingfinaldata.csv", price, delimiter=",")
mean = st.mean(price)
var = st.variance(price)
N = len(price)
presample = random.sample(price,10)
print("nemoone moghadamti:",presample)
xbar = st.mean(presample)
s2 = st.variance(presample)
r= 0.01
alpha = 0.05
z = norm.ppf(1-alpha/2, loc = 0, scale = 1)
z**2*s2
n = (((r*xbar)**2)/((z**2)*s2))**(-1)
print("n =",n)
index = presample.index(price)
for value in price:
    if value in presample:
        price.remove(value)
len(price)   
sample1 = random.sample(price,35)  
sample = presample + sample1 
sample
len(sample) 
xbarfinal = st.mean(sample)
s2final = st.variance(sample)
print("xbarfinal =",xbarfinal,"s2final =",s2final) 
print("mean =",mean, "var =",var)  