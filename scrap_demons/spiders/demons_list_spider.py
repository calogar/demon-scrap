import scrapy

class DemonsListSpider(scrapy.Spider):
    name = 'demons_list' # Must be unique
    start_urls = [ 'http://megamitensei.wikia.com/wiki/List_of_Shin_Megami_Tensei_Demons' ]

    def get_level(self, data_list):
        '''Strips the level from useless stuff.'''
        if len(data_list) == 0:
            return ""
        else:
            return data_list[1].rstrip('\n')

    def parse(self, response):
        # Parses responses for each request
        tables = response.css(".table.smt1")
        for table in tables:
            rows = table.css("tr")
            for row in rows:
                yield {
                    "name": row.css("td a::text").extract_first(),
                    "level": self.get_level(row.css("td::text").extract()),
                }
