#!/usr/bin/env python
# coding: utf-8

# In[1]:


import selenium
import pandas as pd 
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time 

import warnings
warnings.filterwarnings('ignore')


# In[20]:


# Answer No. 1

# To connect to the driver
driver = webdriver.Chrome(r"C:\Users\rehan\Downloads\chromedriver_win32\chromedriver.exe")


# In[21]:


# To open the naukari page in the automated chrome browser
driver.get('https://www.naukri.com/')


# In[22]:


# To enter the designation name 
designation = driver.find_element(By.CLASS_NAME, 'suggestor-input')
designation.send_keys('Data Analyst')


# In[23]:


# To enter the location 
location = driver.find_element(By.XPATH,"/html/body/div[1]/div[7]/div/div/div[5]/div/div/div/div[1]/div/input")
location.send_keys('Bangalore')


# In[24]:


# To click on the search button to get the search results
search = driver.find_element(By.CLASS_NAME, 'qsbSubmit')
search.click()


# In[25]:


# To store the data
job_title = []
job_location = []
company_name = []


# In[26]:


# Scraping job title from the naukari page
title_tag = driver.find_elements(By.XPATH, '//a[@class="title ellipsis"]')
for i in title_tag[0:10]:
    title = i.text
    job_title.append(title)
    
# Scraping job location form the naukari page
location_tag = driver.find_elements(By.XPATH, '//span[@class="ellipsis fleft locWdth"]')
for i in location_tag[0:10]:
    location = i.text
    job_location.append(location)
    
# Scraping company name from the naukari page
company_tag = driver.find_elements(By.XPATH, '//a[@class="subTitle ellipsis fleft"]')
for i in company_tag[0:10]:
    company = i.text
    company_name.append(company)
    


# In[27]:


print(len(job_title),len(job_location),len(company_name))


# In[28]:


df = pd.DataFrame({'Title' : job_title, 'Location': job_location, 'Company': company_name})
df


# In[29]:


# Answer No.2

driver = webdriver.Chrome(r'C:\Users\rehan\Downloads\chromedriver_win32\chromedriver.exe')

driver.get('https://www.naukri.com/')


# In[30]:


designation = driver.find_element(By.CLASS_NAME, 'suggestor-input')
designation.send_keys('Data Scientist')

location = driver.find_element(By.XPATH,"/html/body/div[1]/div[7]/div/div/div[5]/div/div/div/div[1]/div/input")
location.send_keys('Bangalore')


search = driver.find_element(By.CLASS_NAME, 'qsbSubmit')
search.click()


# In[31]:


job_title = []
job_location = []
company_name = []


# In[32]:


# Scraping job title from the naukari page
title_tag = driver.find_elements(By.XPATH, '//a[@class="title ellipsis"]')
for i in title_tag[0:10]:
    title = i.text
    job_title.append(title)
    
# Scraping job location form the naukari page
location_tag = driver.find_elements(By.XPATH, '//span[@class="ellipsis fleft locWdth"]')
for i in location_tag[0:10]:
    location = i.text
    job_location.append(location)
    
# Scraping company name from the naukari page
company_tag = driver.find_elements(By.XPATH, '//a[@class="subTitle ellipsis fleft"]')
for i in company_tag[0:10]:
    company = i.text
    company_name.append(company)
    


# In[33]:


print(len(job_title),len(job_location),len(company_name))


# In[34]:


df = pd.DataFrame({'Title' : job_title, 'Location': job_location, 'Company': company_name})
df


# In[35]:


# Answer No.3

driver = webdriver.Chrome(r'C:\Users\rehan\Downloads\chromedriver_win32\chromedriver.exe')

driver.get('https://www.naukri.com/')


# In[36]:


designation = driver.find_element(By.CLASS_NAME, 'suggestor-input')
designation.send_keys('Data Scientist')

search = driver.find_element(By.CLASS_NAME, 'qsbSubmit')
search.click()


# In[37]:


loc_filter = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div/section[1]/div[2]/div[5]/div[2]/div[2]/label/i")
loc_filter.click()


# In[38]:


salary_filter = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div/section[1]/div[2]/div[6]/div[2]/div[2]/label/i")
salary_filter.click()


# In[39]:


job_title = []
job_location = []
company_name = []
experience = []


# In[40]:


# Scraping job title from the naukari page
title_tag = driver.find_elements(By.XPATH, '//a[@class="title ellipsis"]')
for i in title_tag[0:10]:
    title = i.text
    job_title.append(title)
    
# Scraping job location form the naukari page
location_tag = driver.find_elements(By.XPATH, '//span[@class="ellipsis fleft locWdth"]')
for i in location_tag[0:10]:
    location = i.text
    job_location.append(location)
    
# Scraping company name from the naukari page
company_tag = driver.find_elements(By.XPATH, '//a[@class="subTitle ellipsis fleft"]')
for i in company_tag[0:10]:
    company = i.text
    company_name.append(company)
    
    
exp_tag = driver.find_elements(By.XPATH, '//span[@class="ellipsis fleft expwdth"]')
for i in exp_tag[0:10]:
    expr = i.text
    experience.append(expr)
    


# In[41]:


print(len(job_title),len(job_location),len(company_name), len(experience))


# In[42]:


df = pd.DataFrame({'Title' : job_title, 'Location': job_location, 'Company': company_name, 'Experience': experience})
df


# In[43]:


# Answer No. 4

driver = webdriver.Chrome(r'C:\Users\rehan\Downloads\chromedriver_win32\chromedriver.exe')

driver.get('https://flipkart.com/')


# In[44]:


product = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input')
product.send_keys('Sunglasses')


# In[47]:


submit = driver.find_element(By.CLASS_NAME,"L0Z3Pu")
submit.click()


# In[48]:


brand_name = []
prod_disc = []
price = []
Rating =[]


# In[49]:


start=0
end=3
for page in range(start, end):
    brand = driver.find_elements(By.XPATH, '//div[@class="_2WkVRV"]')
    for i in brand[0:99]:
        brnd = i.text
        brand_name.append(brnd)
        
#     try:
#         product_disc = driver.find_elements(By.XPATH, '//a[@class="IRpwTa"]')
#         for i in product_disc[0:99]:
#             pd = i.text
#             prod_disc.append(pd)
        
#             if len(prod_disc) < 99:
#                 raise ValueError("Insufficient data retrieved")
#     except ValueError as e:
#         print(f"Error: {e}")
#     # If there is insufficient data, filter the existing data
#         prod_disc = [i for i in product_disc if i.text != "99"]

# Product discription is not fetching the sufficient data
        
    mrp = driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
    for i in mrp[0:99]:
        rupee = i.text
        price.append(rupee)
        
    rate = driver.find_elements(By.XPATH,'//div[@class="_3Ay6Sb"]')
    for i in rate[0:99]:
        rt = i.text
        Rating.append(rt)
    next_page = driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
    next_page.click()
    time.sleep(4)


# In[50]:


df = pd.DataFrame({'Brand' : brand_name, 'Price': price})
df


# In[51]:


# Answer no.5

driver = webdriver.Chrome(r'C:\Users\rehan\Downloads\chromedriver_win32\chromedriver.exe')

driver.get('https://www.flipkart.com/apple-iphone-11-black-64-gb/product-reviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&marketplace=FLIPKART')


# In[52]:


# Initialize empty lists

Rating =[]
Summary = []
Full_review = []


# In[53]:


start = 0
end = 10
for page in range(start, end+1):
    rating_ = driver.find_elements(By.XPATH, '//div[@class="_3LWZlK _1BLPMq"]')
    for i in rating_:
        rate = i.text
        Rating.append(rate)

    summary_ = driver.find_elements(By.XPATH, '//p[@class="_2-N8zT"]')
    for i in summary_:
        summ = i.text
        Summary.append(summ)

    review_ = driver.find_elements(By.XPATH, '//div[@class="t-ZTKy"]')
    for i in review_:
        rview = i.text
        Full_review.append(rview)

    try:
        next_page = driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
        next_page.click()
        time.sleep(3)
    except:
        print("Reached last page")
        break


# In[54]:


df = pd.DataFrame({'Rating' : Rating, 'Summary': Summary, 'Full Review': Full_review})
df


# In[57]:


# Answer no.6

driver = webdriver.Chrome(r'C:\Users\rehan\Downloads\chromedriver_win32\chromedriver.exe')

driver.get('https://flipkart.com/')

sneaker = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input')
sneaker.send_keys('Sneakers')


# In[58]:


submit = driver.find_element(By.CLASS_NAME,"L0Z3Pu")
submit.click()


# In[59]:


Brand = []
Discription = []
Price = []


# In[60]:


start = 0
end = 2
for page in range(start, end+1):
    brand_ = driver.find_elements(By.XPATH, '//div[@class="_2WkVRV"]')
    for i in brand_:
        bnd = i.text
        Brand.append(bnd)

    disc_ = driver.find_elements(By.XPATH, '//a[@class="IRpwTa"]')
    for i in disc_:
        discr = i.text
        Discription.append(discr)

    price_ = driver.find_elements(By.XPATH, '//div[@class="_30jeq3"]')
    for i in price_:
        pric = i.text
        Price.append(pric)

    try:
        next_page = driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
        next_page.click()
        time.sleep(3)
    except:
        print("Reached last page")
        break


# In[61]:


print(len(Brand),len(Discription), len(Price))


# In[62]:


df = pd.DataFrame({'Brand' : Brand, 'Price': Price})
df


# In[63]:


# Answer no.7

driver = webdriver.Chrome(r'C:\Users\rehan\Downloads\chromedriver_win32\chromedriver.exe')

driver.get('https://www.amazon.in/')


# In[64]:


laptop = driver.find_element(By.XPATH, "/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input")
laptop.send_keys('Laptop')

submit = driver.find_element(By.XPATH,'/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input')
submit.click()

Filter = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[6]/ul[7]/li[13]/span/a/div/label/i")
Filter.click()


# In[65]:


Title = []
Rating = []
Price = []


# In[66]:


title_tag = driver.find_elements(By.XPATH, '//span[@class="a-size-medium a-color-base a-text-normal"]')
for i in title_tag[0:10]:
    title_ = i.text
    Title.append(title_)
    
rating_tag = driver.find_elements(By.XPATH, '//i[@class="a-icon a-icon-star-small a-star-small-4 aok-align-bottom"]')
for i in rating_tag[0:20]:
    rate = i.text
    Rating.append(rate)
    
price_tag = driver.find_elements(By.XPATH, '//span[@class="a-price-whole"]')
for i in price_tag[0:10]:
    mrp = i.text
    Price.append(mrp)
    


# In[67]:


df = pd.DataFrame({'Title' : Title, 'Price': Price})
df


# In[6]:


# Answer no.8

driver = webdriver.Chrome(r'C:\Users\rehan\Downloads\chromedriver_win32\chromedriver.exe')

driver.get('https://www.azquotes.com/top_quotes.html')


# In[5]:


search = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div/div[2]/div[1]/div/form/input[3]")
search.click()


# In[7]:


Quote = []
Author = []
Genre = []


# In[8]:


start = 0
end = 10
for page in range(start, end+1):
    quote_ = driver.find_elements(By.XPATH, '//a[@class="title"]')
    for i in quote_:
        qt = i.text
        Quote.append(qt)

    author_ = driver.find_elements(By.XPATH, '//div[@class="author"]')
    for i in author_:
        au = i.text
        Author.append(au)

    genre_ = driver.find_elements(By.XPATH, '//div[@class="tags"]')
    for i in genre_:
        gnr = i.text
        Genre.append(gnr)

    try:
        next_page = driver.find_element(By.XPATH,'//li[@class="next"]')
        next_page.click()
        time.sleep(3)
    except:
        print("Reached last page")
        break


# In[9]:


df = pd.DataFrame({'Quote' : Quote, 'Author': Author, 'Genre': Genre})
df


# In[10]:


# Answer no.10

driver = webdriver.Chrome(r'C:\Users\rehan\Downloads\chromedriver_win32\chromedriver.exe')

driver.get('https://www.motor1.com/features/308149/most-expensive-new-cars-ever/')


# In[11]:


car_name = []
price = []


# In[12]:


auto = driver.find_elements(By.TAG_NAME, 'h3')
for i in auto:
    car1 = i.text
    car_name.append(car1)

price_ = driver.find_elements(By.TAG_NAME, 'strong')
for i in price_:
    pr = i.text
    price.append(pr)


# In[13]:


car_name


# In[ ]:


df = pd.DataFrame({'Car Name': car_name, 'Price': price})
print(df)


# In[ ]:




