from django.conf.urls import url
from . import views

from django.http import HttpResponse
def test(request):
    # return HttpResponse("It works project level")
    return HttpResponse("It works app level")


urlpatterns = [
    url(r'^$', views.index),
    url(r'^addpoke/(?P<id>\d+)$', views.addpoke),
    url(r'^logout$', views.logout)
]
# url(r'^givehighfiveto/(?P<id>\d+)$',
