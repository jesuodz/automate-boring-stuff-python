from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^api/blog/',
        views.get_post_REQ,
        name='get_post_articles'
    )
]
