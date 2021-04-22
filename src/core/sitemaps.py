from django.contrib.sitemaps import Sitemap
from itertools import chain
from django.urls import reverse
from .models import Services


class StaticViewSitemap(Sitemap):
    protocol = 'https'

    def items(self):
        return [
            'home-page',
            'services-page',
            'about-page',
            'contact-page',
            'vision-page',
        ]

    def location(self, item):
        return reverse(item)


class NewsSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def items(self):
        site_services = Services.status_objects.all()
        site_list = list(
            chain(site_services)
        )
        return site_list

    def lastmod(self, obj):
        return obj.slug
