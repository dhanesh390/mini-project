import scrapy
import os

import json
from scrapy.spiders import CrawlSpider

# from ..items import FlipkartCrawlerItem

print('1: ', os.getcwd())


class FlipKartSpider(CrawlSpider):
    name = 'flipkart'
    allowed_domains = ['flipkart.com']
    headers = {
        "authority": "ssl.doas.state.ga.us",
        "pragma": "no-cache",
        "cache-control": "no-cache",
        "sec-ch-ua": "\"Chromium\";v=\"92\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"92\"",
        "accept": "application/json, text/javascript, */*; q=0.01",
        "x-requested-with": "XMLHttpRequest",
        "sec-ch-ua-mobile": "?0",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "origin": "https://ssl.doas.state.ga.us",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://ssl.doas.state.ga.us/gpr/",
        "accept-language": "en-US,en;q=0.9"
    }

    body = 'draw=1&columns%5B0%5D%5Bdata%5D=function&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=false&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=function&columns%5B1%5D%5Bname%5D=&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=true&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=title&columns%5B2%5D%5Bname%5D=&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=agencyName&columns%5B3%5D%5Bname%5D=&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=true&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=postingDateStr&columns%5B4%5D%5Bname%5D=&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=true&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B5%5D%5Bdata%5D=closingDateStr&columns%5B5%5D%5Bname%5D=&columns%5B5%5D%5Bsearchable%5D=true&columns%5B5%5D%5Borderable%5D=true&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B6%5D%5Bdata%5D=function&columns%5B6%5D%5Bname%5D=&columns%5B6%5D%5Bsearchable%5D=true&columns%5B6%5D%5Borderable%5D=false&columns%5B6%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B6%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B7%5D%5Bdata%5D=status&columns%5B7%5D%5Bname%5D=&columns%5B7%5D%5Bsearchable%5D=true&columns%5B7%5D%5Borderable%5D=false&columns%5B7%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B7%5D%5Bsearch%5D%5Bregex%5D=false&order%5B0%5D%5Bcolumn%5D=5&order%5B0%5D%5Bdir%5D=asc&start=0&length=50&search%5Bvalue%5D=&search%5Bregex%5D=false&responseType=ALL&eventStatus=OPEN&eventIdTitle=&govType=ALL&govEntity=&eventProcessType=ALL&dateRangeType=&rangeStartDate=&rangeEndDate=&isReset=false&persisted=&refreshSearchData=false'

    # start_urls = [
    #     'https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3Drealme&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&param=7564&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIlNob3AgTm93Il0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&otracker=clp_metro_expandable_1_3.metroExpandable.METRO_EXPANDABLE_Shop%2BNow_mobile-phones-store_Q1PDG4YW86MF_wp2&fm=neo%2Fmerchandising&iid=M_4fcaa499-c7a8-4e11-85c2-4ac7ee87cb42_3.Q1PDG4YW86MF&ppt=hp&ppn=homepage&ssid=kiklrsqqrk0000001673236915550&page=%s'.replace(
    #         '%s', str(page)) for page in range(0, 10)]
    def start_requests(self):
        url = 'https://www.flipkart.com/search?q=oneplus+nord+ce+2'
        print('3: ')
        yield scrapy.Request(url=url, method='POST', headers=self.headers, body=self.body, callback=self.parse)

    def parse(self, response):
        print('2: ')
        details = FlipkartCrawlerItem()
        response = json.loads(response.body)
        for i in response.get('data'):
            print('0: 1: ', i)
            yield details
        # # product_name = response.xpath('//div[@class="_4rR01T"]/text()').extract()
        # # data = response.css("div.st-about-employee-pop-up")
        # # data = response.xpath("//div[@class='team-popup-wrap st-about-employee-pop-up']")
        # # original_price = response.css('div._3I9_wc _27UcVY').extract()
        # # original_price = response.xpath('//div[@class="_3I9_wc _27UcVY"]/text()').extract()
        # # offer_percentage = response.css('div._3Ay6Sb').extract()
        # # offer_percentage = response.xpath('//div[@class="_3Ay6Sb"]/text()').extract()
        # # offer_price = response.css('div._30jeq3 _1_WHN1').extract()
        # # offer_price = response.xpath('//div[@class="_30jeq3 _1_WHN1"]/text()').extract()
        #
        # row_data = zip(product_name, original_price, offer_percentage, offer_price)
        # for item in row_data:
        #
        #     # details = {'actual_price': item[1],
        #     #            'offer_percentage': item[2], 'vendor_price': item[3]}
        #
        #     details['actual_price'] = ''.join(original_price).strip()
        #     details['offer_percentage'] = ''.join(offer_percentage).strip()
        #     details['offer_price'] = ''.join(offer_price).strip()
        #     yield details

        # for item in row_data:
        #     yield {'Product_Name': item[0].strip(), 'Product_Price': item[1].strip(),
        #     'offer_percentage': item[2].strip(), 'offer_price': item[3].strip() }
        # pass
