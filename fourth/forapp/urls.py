from django.urls import path
from forapp import views


#template tagging
app_name = 'forapp'
urlpatterns = [
    path('rut/',views.rut,name= 'rut'),
    path('other',views.other , name = 'other'),
]
