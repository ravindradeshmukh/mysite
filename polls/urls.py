from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

#from django.utils.encoding import python_2_unicode_compatible

from . import views

app_name='polls'
urlpatterns=[ 
	url(r'^$', views.index, name='index'),
	url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
	url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
] #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



