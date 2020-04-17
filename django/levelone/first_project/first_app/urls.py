#url mapping by creating urls.py file in the application FOLDER
from django.conf.urls import url
from first_app import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
]
