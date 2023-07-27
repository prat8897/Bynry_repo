from django.urls import path
from . import views

app_name = 'service_request'

urlpatterns = [
    path('submit/', views.submit_service_request, name='submit'),
    path('tracking/', views.track_service_request, name='tracking'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('signup/', views.signup_view, name='signup'),
    path('account_info/', views.account_info_view, name='account_info'),
]
