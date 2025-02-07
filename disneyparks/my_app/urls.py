from django.urls import path
from . import views



urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('parks/', views.park_index, name='park-index'),
    path('parks/<int:park_id>', views.park_detail, name='park-detail'),
    path('parks/create/', views.ParkCreate.as_view(), name='park-create'),
    path('parks/<int:pk>/update/', views.ParkUpdate.as_view(), name='park-update'),
    path('parks/<int:pk>/delete/', views.ParkDelete.as_view(), name='park-delete'),


# ride routes
    path('rides/create/', views.RideCreate.as_view(), name='ride-create'),
    path('rides/<int:pk>/', views.RideDetail.as_view(), name='ride-detail'),
    path('rides/', views.RideList.as_view(), name='ride-index'),
    path('rides/<int:pk>/update/', views.RideUpdate.as_view(), name='ride-update'),
    path('rides/<int:pk>/delete/', views.RideDelete.as_view(), name='ride-delete'),


    # path('parks/<int:park_id>/add-ride', views.add_ride, name='add-ride'),


    path('accounts/signup/', views.signup, name='signup'),

    
]
