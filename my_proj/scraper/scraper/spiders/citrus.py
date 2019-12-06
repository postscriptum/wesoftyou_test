import scrapy


class CitrusSpider(scrapy.Spider):
	name = 'citrus'
	start_urls = [
	    'https://www.citrus.ua/smartfony/brand-apple/',
	    'https://www.citrus.ua/noutbuki-i-ultrabuki/?prices[max]=25000'
	]

	def parse(self, response):
		for item_link in response.css('div.product-card__body li.item a::attr(href)').getall():
			yield response.follow(item_link, callback=self.parse_item)
		next_page = response.css('div.pagination-container li:last-child a::attr(href)').get()
		if next_page is not None:
			yield response.follow(next_page, callback=self.parse)

	def parse_item(self, response):
		# print('ITEM: ', response.url)
		pass
