from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('reservation/', views.reservation_home, name='reservation-home'),
    path('_05ReservationSearchPage/', views._05ReservationSearchPage, name='_05ReservationSearchPage'),
    path('_08SummaryPage/', views._08SummaryPage, name='_08SummaryPage'),
    path('_09CompletedPage/', views._09CompletedPage, name='_09CompletedPage'),
    path('_11AdminStaffHomePage/', views._11AdminStaffHomePage, name='_11AdminStaffHomePage'),
    path('_12StaffHomePage/', views._12StaffHomePage, name='_12StaffHomePage'),
]
