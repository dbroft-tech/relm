from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('events/', views.events, name='events'),
    path('sermons/', views.sermons, name='sermons'),
    path('contact/', views.contact, name='contact'),
    path('staff/', views.staff, name='staff'),
    path('prayer-request/', views.prayer_request, name='prayer_request'),
    path('donate/', views.donate, name='donate'),
    path('newsletter/', views.newsletter, name='newsletter'),
    path('api/events/', views.event_api, name='event_api'),
] 