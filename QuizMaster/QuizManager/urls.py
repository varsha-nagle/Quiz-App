from django.urls import path
from .views import index, login_view, register_view, home_view, rules_view, quiz_page

urlpatterns = [
    path('', index, name='index'),
    path('login/', login_view, name="login"),
    path('register/', register_view, name="register"),
    path('home/', home_view, name="home"),
    path('rules/', rules_view, name="rules"),
    path('quiz/', quiz_page, name="quiz_page"),
    # other urlpatterns
]