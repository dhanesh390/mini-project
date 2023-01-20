from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings


from scaper.scraper import settings as my_settings
from scrapy.utils.project import get_project_settings


from e_product.flipkartcrawler.flipkartcrawler.spiders.flipkart_spider import FlipKartSpider


class Command(BaseCommand):
    help = 'Release spider'

    def handle(self, *args, **options):
        crawler_settings = Settings()
        crawler_settings.setmodule(my_settings)

        # process = CrawlerProcess(get_project_settings())
        process = CrawlerProcess(settings=crawler_settings)

        process.crawl(FlipKartSpider)
        process.start()
