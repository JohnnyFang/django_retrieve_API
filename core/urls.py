from django.urls import path

from core import views

app_name = 'core'

urlpatterns = [
    path('create/user/', views.CreateUserView.as_view(), name='create_user'),
    path('create/token/', views.CreateTokenView.as_view(), name='crete_token')
]
