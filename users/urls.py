from django.urls import path
from users.views import ProfileDetailView
from . import views

urlpatterns = [
    path('update/', views.update, name="update"),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name="profile"),
    path('register/', views.register, name="register"),
]
