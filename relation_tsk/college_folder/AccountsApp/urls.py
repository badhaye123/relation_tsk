from django.urls import path

from .views import register_user, login_view, logout_view

urlpatterns = [
    path('reg/', register_user, name='reg'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]