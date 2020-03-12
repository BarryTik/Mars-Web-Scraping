# Mars Web Scraping

This web page scrapes several websites to collect a set of interesting facts and images relating to the planet Mars.

mission_to_mars.py uses [Splinter](https://splinter.readthedocs.io/en/latest/ "Splinter information") to control a browser and [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/ "Beautiful Soup information") and [Pandas](https://pandas.pydata.org/pandas-docs/version/0.23.4/generated/pandas.read_html.html "Pandas.read_html documentation") to scrape information from several websites containing the desired information.
scrape_mars.py calls mission_to_mars.py and loads the scraped information into a MongoDB database. It then serves a web page using [Flask](https://palletsprojects.com/p/flask/ "Flask information") which passes information into index.html using [Jinja](https://palletsprojects.com/p/jinja/ "Jinja information"). Clicking the "Scrape new data" button executes mission_to_mars.py again and gathers new images and text. 
The website features a static simulated background image of the [Mojave Crater](https://www.jpl.nasa.gov/spaceimages/details.php?id=PIA17447 "Source") on Mars.
![Screenshot of the website](Mission_to_Mars/screenshot.jpg)
