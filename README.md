# merch-store-scraper
A Python web scraper that crawls through the t-shirt section of the popular death metal band merch company Comatose Music and saves all the output to a CSV file.
I used the Python web-crawling framework Scrapy for this project. 
The spider is created and the Shirts section of the website www.comatosemusic.com/ is fetched using the scrapy shell.
I then inspect the page's HTML and locate the product divs, which I then use to extract the Name, Price, and URL of each product.
I also locate the HTML tag for the "Next Page" button.
Using all the information I've gathered, I then loop through each product div on each page, crawling through every item and gathering 
the Name, Price, and URL of each one. The information is outputted as a CSV file and finally organized for presentation.
