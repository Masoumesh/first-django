"""mysiteProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from mysiteApp.sitemaps import StaticViewSitemap
from blog.sitemaps import BlogSitemap
from debug_toolbar.toolbar import debug_toolbar_urls



sitemaps = {
    'static': StaticViewSitemap,
    'blog': BlogSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mysiteApp.urls')),
    path('blog/', include('blog.urls')),
    path('accounts/', include('accounts.urls')),
    
    path('sitemap.xml', sitemap,{'sitemaps':sitemaps}, 
         name='django.contrib.sitemaps.views.sitemap'),
    re_path('robots.txt', include('robots.urls')),
    path('captcha/', include('captcha.urls')),
] + debug_toolbar_urls()

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)