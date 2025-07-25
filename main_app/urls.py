from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    # Routes will be added here
    path('about/', views.about, name='about'),
    path('', views.home, name='home'),
    # route for a single cat
    path('cats/<int:cat_id>/', views.cat_detail, name='cat-detail'),
    # route for cats index
    path('cats/', views.cat_index, name='cat-index'),
]
