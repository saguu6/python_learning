from django.conf.urls import url
from AppTwo import views

urlpatterns = [
    url(r'^help',views.help,name="help"),
]
