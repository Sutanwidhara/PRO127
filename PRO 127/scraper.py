from selenium import webdriver
from selenium.webdriver.common.by import By
"""bs4 (BeautifulSoup version 4) is a Python module, which is famously used for parsing or separating text as HTML and then performing actions on it, such as finding specific HTML tags with a particular class/id or listing out all the <li> tags inside the ul tags, etc"""
"""Selenium is a browser automation Python module, that means, it can help us to open a browser, click on web pages, fill in some forms on the web page and perform other browser operations automatically"""
from bs4 import BeautifulSoup
import time
import pandas as pd

# NASA Exoplanet URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

# Webdriver
browser = webdriver.Chrome("D:/Setup/chromedriver_win32/chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

planets_data = []

# Define Exoplanet Data Scrapping Method
def scrape():

    for i in range(0,10):
        print(f'Scrapping page {i+1} ...' )

        ## ADD CODE HERE ##
        #bs4
        soup = BeautifulSoup(browser.page_source,"html.parser")
        for ul_tag in soup.find_all("ul",attrs={"class","brightest star"}):
            li_tags = ul_tag.find_all("li")
            temp_list = []
            for index , li_tag in enumerate(li_tags):
                if  index == 0 :
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else :
                    try : 
                        temp_list.append(li_tag.contents[0])
                    except :
                        temp_list.append("")
            planets_data.append(temp_list)
        browser.find_element(by=By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()

        



        
# Calling Method    
scrape()

# Define Header
headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date"]

# Define pandas DataFrame   
planet_df = pd.DataFrame(planets_data,columns=headers)

# Convert to CSV
planet_df.to_csv("scraped.csv",index=True,index_label="id")
    


