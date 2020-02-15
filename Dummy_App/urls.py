from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
	path('user/login/', views.Login.as_view(), name='user-login'),
	
]
