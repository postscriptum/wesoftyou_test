1. Scraper

The Scrapy framework is used. To run the Citrus spider:

```
cd <project_dir>/my_proj/scraper
scrapy crawl citrus
```

The scraped data are saved to Postgres DB. Duplicates are dropped.

2. API

It's used Django REST framework.  
To get all data:

```
GET /gadgets/

{
    "count": 486,
    "next": "http://127.0.0.1:8000/gadgets/?page=2",
    "previous": null,
    "results": [
        {
            "code": "633125",
            "category": "smartfony",
            "link": "https://www.citrus.ua/smartfony/iphone-xr-128gb-black-apple-633125.html",
            "price": 19999,
            "cashback": 1000,
            "full_desc": "<div class=\"container ... Узнай больше о мобильном гейминге!</div></div>",
            "tech": {
                "Размер экрана": "Безрамочный дисплей, 6,1\"",
                "Объем оперативной памяти": "3 Гб",
                "Количество ядер": "6 ядер",
                "Основная камера, Мп": "12,0 Мп",
                "Фронтальная камера, Мп": "7,0 Мп",
                "Процессор": "Apple A12"
            },
            "photo_links": [
                "https://i1.ytimg.com/vi/tG7vx7-3sl0/sddefault.jpg",
                "https://i1.ytimg.com/vi/f5HEGkNZhR4/sddefault.jpg",
                "https://i1.ytimg.com/vi/wEAExvdJo5c/sddefault.jpg",
                "https://i1.ytimg.com/vi/3k-wMK1SBrs/sddefault.jpg"
            ]
        },
        ...
    ]
}
```

Also such filter parameters are supported:  
- min_price and max_price
- min_cash and max_cash
- ram
- cores

Sample requests with filtering:

```
GET /gadgets/?min_price=10000&max_price=20000
GET /gadgets/?min_cash=1000
GET /gadgets/?ram=4
GET /gadgets/?cores=2
GET /gadgets/?cores=4&max_price=15000
```
