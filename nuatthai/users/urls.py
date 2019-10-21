from django.urls import path
from . import views

urlpatterns = [
        path('register/', views.register, name='register'),
        path('_06ReservationPage01/', views._06ReservationPage01, name='_06ReservationPage01'),
        path('_07ReservationPage02/', views._07ReservationPage02, name='_07ReservationPage02'),
        path('_10EditAccount/', views._10EditAccount, name='_10EditAccount'),
        path('_13AdminLogInPage/', views._13AdminLogInPage, name='_13AdminLogInPage'),
        path('_14AdminMainPage/', views._14AdminMainPage, name='_14AdminMainPage'),
]
