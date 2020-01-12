from django.urls import path
from templateApp import views

# TEMPLATE TAGGING
app_name =  'templateApp'

urlpatterns = [
    path('relative/',views.relative,name = 'relative'),
    path('other/',views.other,name = 'other')
]