from django.conf.urls import url

from . import views as core_views

urlpatterns = [
	url('^page1/$', core_views.Page1.as_view(), name="page1"),
	url('^page2/$', core_views.Page2.as_view(), name="page2"),
]
