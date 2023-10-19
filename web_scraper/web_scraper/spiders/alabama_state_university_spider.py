import scrapy


class AlabamaStateUniversitySpiderSpider(scrapy.Spider):
    name = "alabama_state_university_spider"
    allowed_domains = ["www.alasu.edu"]
    start_urls = ["https://www.alasu.edu/directory"]

    def parse(self, response):
        faculty = response.css('table.table tbody tr')

        for member in faculty:
            department = member.css('td.views-field-field-dr-department::text').getall()[3][1:-1]
            if(('Music' in department) or ('Theatre' in department) or ('Dance' in department) 
               or ('Visual Arts' in department) or ('Band' in department)):
                yield{
                    'first-name' : member.css('td.views-field-field-dr-first-name::text').getall()[3][1:-1],
                    'last-name' : member.css('td.views-field-field-dr-last-name::text').getall()[3][1:-1],
                    'phone' : member.css('td.views-field-field-dr-phone::text').getall()[3][1:-1],
                    'title' : member.css('td.views-field-field-dr-title::text').getall()[3][1:-1],
                    'department' : member.css('td.views-field-field-dr-department::text').getall()[3][1:-1],
                    'email' : member.css('td.views-field-field-dr-email::text').getall()[3][1:-1]
                }

        next_page = response.css('nav.pager-nav ul.pagination li.pager__item--next a::attr(href)').get()

        if(next_page is not None):
            next_page_url = 'https://www.alasu.edu/directory' + next_page
            yield response.follow(next_page_url, callback=self.parse)
