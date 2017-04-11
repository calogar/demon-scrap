# Wikipedia Demon Scraping

This is a <a href="https://scrapy.org/" target="_blank">Scrapy</a> project built with the objective of scraping (extracting information) from Wikipedia pages about videogames of the Shin Megami Tensei saga, so it can be used to develop simulations and test applications.

The scraping code is located in the `scrap_demons` subfolder and classified into **spiders**. To execute each spider, we can do it from console command:

```
scrapy crawl spidername -o myresult.json
```

Where **spidername** is the name of the specific Spider which is assigned to the name propery on each class.

It's also useful to use the command:

```
scrapy shell "myurl"
```

Where **myurl** is the actual URL of the page we are scraping. With this command, we can enter a shell mode where we can test CSS and Xpath selectors to easly develop the spiders.