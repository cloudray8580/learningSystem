from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.index, name='index'), # myserver/
    url(r'^markdown$',views.getMarkdownText, name='markdown'), #myserver/markdown
]