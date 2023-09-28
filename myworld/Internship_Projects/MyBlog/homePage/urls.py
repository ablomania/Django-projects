from . import views
from django.urls import path


urlpatterns = [
    path('home/', views.homepage, name = 'home'),
    path('account/', views.createaccount, name = 'account'),
    path('reader/<int:id>', views.read, name= 'read'),
    path('articles/', views.allarticles, name = 'articles'),
    path('about/', views.contact, name='contact'),
    path('details/<int:id>', views.details, name= 'details'),
]