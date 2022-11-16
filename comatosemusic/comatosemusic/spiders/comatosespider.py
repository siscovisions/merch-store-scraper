import scrapy


class ComatosespiderSpider(scrapy.Spider):
    # Name of the spider
    name = 'comatosespider'

    # Url of the t-shirts page
    start_urls = ['https://www.comatosemusic.com/store/index.php?cPath=48']

    def parse(self, response):
        # Loop through the products and extract the name, price, & url
        products = response.css('div.col')       
        for product in products:
            # Place all the data here that we want as our output
            yield{
                'name': product.css('h5 a::text').get(),
                'price': product.css('h6.card-subtitle').get().replace('<h6 class="card-subtitle mb-2 text-muted"><del>', '').replace('</del> <span class="text-danger">', ' ').replace('</span></h6>', ''),
                'url': product.css('h5.card-title a').attrib['href']
            }
        
        next_page = response.css('[aria-label=" Next Page "] ::attr(href)').get()

        if next_page is not None:
            next_page_url = next_page
            yield response.follow(next_page_url, callback=self.parse)


#PRICE
#price = product.css('h6.card-subtitle').get()