from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('rocks/', views.rocks_index, name='index'),
    path('rocks/<int:rock_id>', views.rocks_detail, name='detail'),
    path('rocks/create', views.RockCreate.as_view(), name='rocks_create'),
    path('rocks/<int:pk>/update/', views.RockUpdate.as_view(), name='rocks_update'),
    path('rocks/<int:pk>/delete/', views.RockDelete.as_view(), name='rocks_delete'),
    path('rocks/<int:rock_id>/add_observation/', views.add_observation, name='add_observation'),
    path('rocks/<int:rock_id>/assoc_mineral/<int:mineral_id>/', views.assoc_mineral, name='assoc_mineral'),
    path('minerals/', views.MineralList.as_view(), name='minerals_index'),
    path('minerals/<int:pk>/', views.MineralDetail.as_view(), name='minerals_detail'),
    path('minerals/create/', views.MineralCreate.as_view(), name='minerals_create'),
    path('minerals/<int:pk>/update/', views.MineralUpdate.as_view(), name='minerals_update'),
    path('minerals/<int:pk>/delete/', views.MineralDelete.as_view(), name='minerals_delete'),
]