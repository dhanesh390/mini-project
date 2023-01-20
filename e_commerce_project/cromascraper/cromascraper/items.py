# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from offer.models import Offer


class CromascraperItem(scrapy.Item):
    django_model = Offer
