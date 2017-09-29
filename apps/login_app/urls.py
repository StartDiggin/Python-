from django.conf.urls import url
from . import views
from django.http import HttpResponse
def test(request):
    # return HttpResponse("It works project level")
    return HttpResponse("It works app level")



urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^dashboard$', views.dashboard),
    url(r'^logout$', views.logout),
]
