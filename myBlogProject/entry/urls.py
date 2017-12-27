from django.conf.urls import url
from entry.views import entry


app_name = 'entryApp'

urlpatterns = [
    url(r'^$',entry,name='entry'),
]