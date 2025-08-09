from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_stock_item/', views.add_stock_item, name='add_stock_item'),
    path('view_stock_items/', views.view_stock_items, name='view_stock_items'),
    path('low_stock_alerts/', views.low_stock_alerts, name='low_stock_alerts'),
    path('delete_stock_items/', views.delete_stock_items, name='delete_stock_items'),
    path('edit_stock_item/<item_id>/', views.edit_stock_item, name='edit_stock_item'),  # Added edit route
    path('history/', views.history, name='history'),
    path('logout/', views.logout, name='logout'),
]
