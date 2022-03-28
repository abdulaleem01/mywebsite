from unicodedata import name
from django.urls import   path
from basic_app import views

app_name = 'pp'

urlpatterns=[
    path('photography/',views.photography,name='photography'),
    path('website/',views.website,name='website'),
    path('photography1/',views.photography2,name='photography2'),
    path('photography2/',views.photography3,name='photography3'),

    
]