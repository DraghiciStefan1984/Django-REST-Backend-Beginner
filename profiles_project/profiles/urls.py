from django.urls import path
from profiles import views

urlpatterns = [
    path('hello/', views.HelloApiView.as_view())
]
