from django.contrib import admin
from django.urls import path,include
from home import views
#django admn header customization
admin.site.site_header="Welcome to the Sridhar Admin"
admin.site.site_title="Welcome to Srizinga's world"
admin.site.index_title="Welcome to the portal"
urlpatterns = [
    path('', views.home),
    path('about', views.about),
    path('skills', views.skills),
    path('contact', views.contact)
]