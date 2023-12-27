from django.urls import path
from .views import index, login_view, register_view

urlpatterns = [
    path('', index, name='index'),
    path('login/', login_view, name="login"),
    path('register/', register_view, name="register")
    # other urlpatterns
]