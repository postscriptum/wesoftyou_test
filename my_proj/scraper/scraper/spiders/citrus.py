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
		code = response.css('div.product__sku span::text').get()[5:]
		category = response.url[8:].split('/')[1]
		price = response.css('div.price span span::text').get()
		if price is None:
			price = response.css('div.price span::text').get()
		cashback = response.css('div.bonus__value span::text').get()
		if cashback is None:
			cashback = 0
		else:
			cashback = int(cashback[:-4].replace(' ', ''))
		full_desc = response.css('div.product__description').get()
		tech = {}
		for tech_item in response.css('div.showcase__characteristics div.item__description'):
			tech[tech_item.css('span.item__title::text').get()] = tech_item.css('span.item__value::text').get()
		photo_links = response.css('div.thumbs img::attr(src)').getall()
		yield {
		    'code': code,
		    'category': category,
		    'link': response.url,
		    'price': int(price.replace(' ', '')) if price else 0,
		    'cashback': cashback,
		    'full_desc': full_desc,
		    'tech': tech,
		    'photo_links': photo_links
		}
