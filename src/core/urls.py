from .sitemaps import StaticViewSitemap, NewsSitemap
from django.contrib.sitemaps.views import sitemap
from django.urls import path
from . import views
sitemaps = {
    'static': StaticViewSitemap,
    'news': NewsSitemap,
}

urlpatterns = [
    path('', views.HomePage, name='home-page'),
    path('about/', views.AboutPage, name='about-page'),
    path('contact/', views.ContactPage, name='contact-page'),
    path('core-values/', views.CoreValues, name='core-page'),
    path('services/', views.ServicesPage, name='services-page'),
    path('service/<slug:slug>/', views.ServicesPageDetail, name='service-detail-page'),
    path('category/<slug:slug>/', views.CategoryDetail, name='category-detail-page'),

    # sitemap
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
]

handler404 = views.page_not_found
