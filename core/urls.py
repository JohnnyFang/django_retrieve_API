from django.urls import path

from core import views

app_name = 'core'

urlpatterns = [
    path('user/', views.CreateUserView.as_view(), name='create_user'),
    path('token/', views.CreateTokenView.as_view(), name='crete_token')
]
