
from selenium import webdriver
import random
import string
import time
import pandas as pd
from selenium.webdriver.chrome.options import Options
import csv


df = pd.read_csv('articles.csv')
saved_column = df['Author Link']
saved_column = saved_column.tolist()

options = webdriver.ChromeOptions() 
options.add_argument("--headless")
driver = webdriver.Chrome(executable_path="/Users/aldrin0n9/Documents/Python Projects/chromedriver", options=options)



def randomString():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(8))

def get_random_alphaNumeric_string():
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join((random.choice(lettersAndDigits) for i in range(8)))

array = []
emails = []
for x in range(6000,7000):
    
    if (x % 20 == 0):
        print('Creating email')
        name = randomString()
        email = name + '@gmail.com'
        password = get_random_alphaNumeric_string()
        family = randomString()
        
        driver.get('https://hq.ssrn.com/login/pubsigninjoin.cfm#')
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="email"]').send_keys(email)
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="maincontent"]/div/div[2]/div/div[5]').click()
        
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="register-form"]/div[2]/input').send_keys(name)
        driver.find_element_by_xpath('//*[@id="register-form"]/div[3]/input').send_keys(family)
        driver.find_element_by_xpath('//*[@id="txtPassword"]').send_keys(password)
        driver.find_element_by_xpath('//*[@id="txtRtPassword"]').send_keys(password)
        driver.find_element_by_xpath('//*[@id="registerBtn"]').click()
        time.sleep(3)
        print('Email created')
    
    id = saved_column[x].replace('https://papers.ssrn.com/sol3/cf_dev/AbsByAuth.cfm?per_id=', '')
    driver.get('https://papers.ssrn.com/sol3/GetAuthorEmail.cfm?partid=' + id + '&pag=auth')
    time.sleep(1)
    try:
        name = driver.find_element_by_xpath('/html/body/center/table/tbody/tr[2]/td/table/tbody/tr[1]/td/b').text
        email = driver.find_element_by_xpath('/html/body/center/table/tbody/tr[2]/td/table/tbody/tr[2]/td[4]/a').text
        emails.append([name,email])
        with open('6k_7k.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, email])
        print(name + ': ' + email)
    except:
        with open('6k_7k.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Does not exist', 'Does not exist'])
        emails.append(['',''])
        print('No email or name')
    print(x)
print(emails)

