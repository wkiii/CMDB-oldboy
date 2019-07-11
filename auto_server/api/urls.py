from django.conf.urls import url
from api import views

urlpatterns = [
    # url(r'^asset/', views.asset),
    url(r'^asset/', views.Asset.as_view()),
    url(r'^text/', views.Text.as_view())
]
