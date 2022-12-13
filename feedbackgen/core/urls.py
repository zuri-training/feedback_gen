from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name="index"),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
    #path('feedback', views.feedback, name='feedback'),
    path('signup/', views.signup_view, name='signup'),
    path('faq/', views.faq, name='faq'),
    path('pricing/', views.pricing, name='pricing')
]