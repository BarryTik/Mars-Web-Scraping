#Dependencies
from bs4 import BeautifulSoup as bs
import pymongo
from splinter import Browser
import pandas as pd
import time
def scrape_mars():
    executable_path = {'executable_path':'C:\chromedrv\chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless = False)
    

    ## Define variables
    featured_image_url = ""
    news_p = ""
    news_title = ""

    ## Scraping Mars news
    try:
        url = 'https://mars.nasa.gov/news/'
        browser.visit(url)
        time.sleep(2)
        html = browser.html
        soup = bs(html,'html.parser')
        news_title = soup.find('div', class_ = 'content_title').a.text
        news_p = soup.find('div', class_ = 'article_teaser_body').text
    except:
        print("Mars news not found")

    ## Scraping Mars Image
    try:
        url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
        browser.visit(url)
        time.sleep(2)
        browser.click_link_by_partial_text('FULL IMAGE')
        time.sleep(2)
        html= browser.html
        soup = bs(html, 'html.parser')

        featured_image = soup.find('div', class_="fancybox-inner").img['src']
        featured_image_url = f"https://www.jpl.nasa.gov{featured_image}"
    except:
        print("Mars image not found")

    ## Scraping Mars Weather
    try:
        url = 'https://twitter.com/marswxreport?lang=en'
        browser.visit(url)
        time.sleep(2)
        html = browser.html
        soup = bs(html, 'html.parser')
        mars_weather = soup.find('p',class_='TweetTextSize').text
    except:
        print("Mars weather not found")
    
    ## Scraping Mars Facts
    try:
        url='https://space-facts.com/mars/'
        mars_table = pd.read_html(url)
        mars_table_html = mars_table[0].to_html().replace('\n','')
    except:
        ("Mars Facts not found")
    
    ## Scraping Mars Hemispheres
    try:
        hemisphere_image_urls = []
        base_url = 'https://astrogeology.usgs.gov'
        url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
        hemispheres = ['Cerberus','Schiaparelli','Syrtis Major','Valles Marineris']

        for hemisphere in hemispheres:
            browser.visit(url)
            browser.click_link_by_partial_text(hemisphere)
            browser.click_link_by_partial_text('Open')
            soup = bs(browser.html,'html.parser')
            partial_url = soup.find('img',class_='wide-image')['src']
            image_url = f"{base_url}{partial_url}"
            hemisphere_image_urls.append({'title':f"{hemisphere} Hemisphere","img_url":image_url})
    except:
        ("Mars Hemispheres not found")
    ## Final output
    scraped_data = {"news_title":news_title,"news_p":news_p,"featured_image_url":featured_image_url,"mars_weather":mars_weather,"mars_table_html":mars_table_html,"hemisphere_image_urls":hemisphere_image_urls}

    return scraped_data

print(scrape_mars())