from django.urls import path

from core import views

app_name = 'core'

urlpatterns = [
    path('token/', views.CreateTokenView.as_view(), name='token')
]