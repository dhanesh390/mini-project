# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
import os
from offer.models import Offer
print('1.1 items: ', os.getcwd())
# from e_product.offer.models import Offer


class FlipkartCrawlerItem(DjangoItem):
    django_model = Offer

